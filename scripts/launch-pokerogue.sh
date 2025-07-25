#!/bin/bash

# PokéRogue Launcher for Unix/Linux/macOS
# This script automates the setup and launching of PokéRogue

set -e  # Exit on any error

echo "========================================"
echo "    PokéRogue Launcher for Unix/Linux"
echo "========================================"
echo

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✓${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

print_error() {
    echo -e "${RED}ERROR:${NC} $1"
}

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to get browser process count
get_browser_count() {
    ps aux | grep -E "(chrome|firefox|safari|edge)" | grep -v grep | wc -l
}

# Trap to cleanup on exit
cleanup() {
    if [ ! -z "$SERVER_PID" ]; then
        echo
        echo "Stopping development server..."
        kill $SERVER_PID 2>/dev/null || true
        # Also kill any remaining node processes
        pkill -f "npm run start:dev" 2>/dev/null || true
        pkill -f "vite.*development" 2>/dev/null || true
    fi
    echo "Server stopped. Goodbye!"
}

trap cleanup EXIT

# Check if Git is installed
echo "[1/8] Checking if Git is installed..."
if ! command_exists git; then
    print_error "Git is not installed or not in PATH."
    echo "Please install Git:"
    echo "  Ubuntu/Debian: sudo apt-get install git"
    echo "  CentOS/RHEL: sudo yum install git"
    echo "  macOS: Install Xcode Command Line Tools or use Homebrew"
    exit 1
fi
print_status "Git is installed"

# Check if Node.js is installed
echo "[2/8] Checking if Node.js is installed..."
if ! command_exists node; then
    print_error "Node.js is not installed or not in PATH."
    echo "Please install Node.js from https://nodejs.org/"
    echo "Or use a package manager:"
    echo "  Ubuntu/Debian: curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash - && sudo apt-get install -y nodejs"
    echo "  macOS: brew install node"
    exit 1
fi
print_status "Node.js is installed"

# Check Node.js version
NODE_VERSION=$(node --version)
echo "  Node.js version: $NODE_VERSION"

# Check if npm is available
if ! command_exists npm; then
    print_error "npm is not installed or not in PATH."
    exit 1
fi

# Attempt to cd into pokerogue directory
echo "[3/8] Looking for pokerogue directory..."
if [ -d "pokerogue" ]; then
    print_status "Found pokerogue directory"
    cd pokerogue
else
    print_warning "pokerogue directory not found"
    echo
    read -p "Would you like to download PokéRogue? (y/n): " CLONE_CHOICE
    if [[ $CLONE_CHOICE =~ ^[Yy]$ ]]; then
        echo "Cloning PokéRogue repository..."
        git clone https://github.com/Thrasher-Software/pokerogue.git
        if [ $? -ne 0 ]; then
            print_error "Failed to clone repository"
            exit 1
        fi
        cd pokerogue
    else
        echo "Repository not cloned. Exiting..."
        exit 1
    fi
fi

# Git fetch to check for updates
echo "[4/8] Checking for updates..."
git fetch origin 2>/dev/null || print_warning "Failed to fetch updates from origin"

# Check if there are updates available
UPDATE_COUNT=$(git rev-list HEAD..origin/main --count 2>/dev/null || echo "0")

if [ "$UPDATE_COUNT" -gt 0 ]; then
    echo "[5/8] $UPDATE_COUNT update(s) available"
    read -p "Would you like to download the latest updates? (y/n): " UPDATE_CHOICE
    if [[ $UPDATE_CHOICE =~ ^[Yy]$ ]]; then
        echo "Downloading updates..."
        git pull origin main
        if [ $? -eq 0 ]; then
            print_status "Updates downloaded successfully"
        else
            print_warning "Failed to pull updates"
        fi
    else
        echo "Skipping updates"
    fi
else
    echo "[5/8] $(print_status "Already up to date")"
fi

# Install/update dependencies
echo "[6/8] Installing dependencies..."
npm install
if [ $? -ne 0 ]; then
    print_error "Failed to install dependencies"
    exit 1
fi

# Start the development server
echo "[7/8] Starting PokéRogue development server..."
echo
echo "Starting server on http://localhost:8000"
echo "Press Ctrl+C to stop the server"
echo

# Start the server in background
npm run start:dev &
SERVER_PID=$!

# Wait a moment for server to start
sleep 3

# Launch browser
echo "[8/8] Opening browser..."

# Detect the operating system and open browser accordingly
if command_exists xdg-open; then
    # Linux
    xdg-open http://localhost:8000 >/dev/null 2>&1 &
elif command_exists open; then
    # macOS
    open http://localhost:8000 >/dev/null 2>&1 &
elif command_exists start; then
    # Windows (if running in WSL or similar)
    start http://localhost:8000 >/dev/null 2>&1 &
else
    echo "Could not automatically open browser. Please navigate to: http://localhost:8000"
fi

echo
echo "========================================"
echo "   PokéRogue is now running!"
echo "   Browser: http://localhost:8000"
echo "   Press Ctrl+C to stop the server"
echo "========================================"
echo

# Keep the script running and wait for the server process
wait $SERVER_PID
