#!/bin/bash

# TexturePacker Spritesheet Update Script for PokeRogue
# This script provides an interactive menu to update spritesheets using TexturePacker CLI

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Function to print colored output
print_color() {
    echo -e "${1}${2}${NC}"
}

# Function to print header
print_header() {
    echo
    print_color $CYAN "=================================="
    print_color $CYAN "  PokeRogue Spritesheet Updater"
    print_color $CYAN "=================================="
    echo
}

# Function to check if TexturePacker is installed
check_texturepacker() {
    if ! command -v TexturePacker &> /dev/null; then
        print_color $RED "ERROR: TexturePacker is not installed or not in PATH"
        print_color $YELLOW "Please install TexturePacker from: https://www.codeandweb.com/texturepacker"
        print_color $YELLOW "Make sure it's added to your system PATH"
        exit 1
    fi
    print_color $GREEN "✓ TexturePacker is available"
}

# Function to check if we're in the correct directory
check_directory() {
    if [[ ! -d "public/images" ]]; then
        print_color $RED "ERROR: Please run this script from the PokeRogue root directory"
        print_color $YELLOW "Expected to find 'public/images' directory"
        exit 1
    fi
    print_color $GREEN "✓ Directory structure is correct"
}

# Function to update Pokemon icons for a specific generation
update_pokemon_generation() {
    local gen=$1
    local gen_dir="public/images/pokemon/icons/${gen}"

    if [[ ! -d "$gen_dir" ]]; then
        print_color $RED "ERROR: Generation $gen directory not found: $gen_dir"
        return 1
    fi

    print_color $BLUE "Updating Pokemon Generation $gen icons..."

    cd "$gen_dir"

    # Check if there are PNG files to process
    if ! ls *.png &> /dev/null; then
        print_color $YELLOW "WARNING: No PNG files found in $gen_dir"
        cd - &> /dev/null
        return 1
    fi

    # Run TexturePacker
    TexturePacker ./ ../configuration.tps \
        --sheet "../../../pokemon_icons_${gen}.png" \
        --data "../../../pokemon_icons_${gen}.json" \
        --replace .png=

    cd - &> /dev/null

    print_color $GREEN "✓ Pokemon Generation $gen icons updated successfully"
    return 0
}

# Function to update Pokemon variant icons
update_pokemon_variants() {
    local gen=$1
    local variant_dir="public/images/pokemon/icons/variant/${gen}"

    if [[ ! -d "$variant_dir" ]]; then
        print_color $RED "ERROR: Generation $gen variant directory not found: $variant_dir"
        return 1
    fi

    print_color $BLUE "Updating Pokemon Generation $gen variant icons..."

    cd "$variant_dir"

    # Check if there are PNG files to process
    if ! ls *.png &> /dev/null; then
        print_color $YELLOW "WARNING: No PNG files found in $variant_dir"
        cd - &> /dev/null
        return 1
    fi

    # Run TexturePacker
    TexturePacker ./ ../configuration.tps \
        --sheet "../../../../pokemon_icons_${gen}v.png" \
        --data "../../../../pokemon_icons_${gen}v.json" \
        --replace .png=

    cd - &> /dev/null

    print_color $GREEN "✓ Pokemon Generation $gen variant icons updated successfully"
    return 0
}

# Function to update items spritesheet
update_items() {
    local items_dir="public/images/items"

    print_color $BLUE "Updating Items spritesheet..."

    cd "$items_dir"

    # Check if there are PNG files to process
    if ! ls *.png &> /dev/null; then
        print_color $YELLOW "WARNING: No PNG files found in $items_dir"
        cd - &> /dev/null
        return 1
    fi

    # Run TexturePacker
    TexturePacker ./ configuration.tps \
        --sheet "../items.png" \
        --data "../items.json" \
        --replace .png=

    cd - &> /dev/null

    print_color $GREEN "✓ Items spritesheet updated successfully"
    return 0
}

# Function to update types spritesheet
update_types() {
    local locale=${1:-""}
    local types_dir="public/images"
    local suffix=""

    if [[ -n "$locale" ]]; then
        suffix="_${locale}"
        types_dir="public/images/types${suffix}"
    else
        types_dir="public/images/types"
    fi

    if [[ ! -d "$types_dir" ]]; then
        print_color $RED "ERROR: Types directory not found: $types_dir"
        return 1
    fi

    print_color $BLUE "Updating Types spritesheet${suffix}..."

    cd "$types_dir"

    # Check if there are PNG files to process
    if ! ls *.png &> /dev/null; then
        print_color $YELLOW "WARNING: No PNG files found in $types_dir"
        cd - &> /dev/null
        return 1
    fi

    # Run TexturePacker
    if [[ -n "$locale" ]]; then
        TexturePacker ./ ../types_configuration.tps \
            --sheet "../types${suffix}.png" \
            --data "../types${suffix}.json" \
            --replace .png=
    else
        TexturePacker ./ types_configuration.tps \
            --sheet "types.png" \
            --data "types.json" \
            --replace .png=
    fi

    cd - &> /dev/null

    print_color $GREEN "✓ Types spritesheet${suffix} updated successfully"
    return 0
}

# Function to update statuses spritesheet
update_statuses() {
    local locale=${1:-""}
    local statuses_dir="public/images"
    local suffix=""

    if [[ -n "$locale" ]]; then
        suffix="_${locale}"
        statuses_dir="public/images/statuses${suffix}"
    else
        statuses_dir="public/images/statuses"
    fi

    if [[ ! -d "$statuses_dir" ]]; then
        print_color $RED "ERROR: Statuses directory not found: $statuses_dir"
        return 1
    fi

    print_color $BLUE "Updating Statuses spritesheet${suffix}..."

    cd "$statuses_dir"

    # Check if there are PNG files to process
    if ! ls *.png &> /dev/null; then
        print_color $YELLOW "WARNING: No PNG files found in $statuses_dir"
        cd - &> /dev/null
        return 1
    fi

    # Run TexturePacker
    if [[ -n "$locale" ]]; then
        TexturePacker ./ ../statuses_configuration.tps \
            --sheet "../statuses${suffix}.png" \
            --data "../statuses${suffix}.json" \
            --replace .png=
    else
        TexturePacker ./ statuses_configuration.tps \
            --sheet "statuses.png" \
            --data "statuses.json" \
            --replace .png=
    fi

    cd - &> /dev/null

    print_color $GREEN "✓ Statuses spritesheet${suffix} updated successfully"
    return 0
}

# Function to update all Pokemon generations
update_all_pokemon() {
    print_color $BLUE "Updating all Pokemon generation icons..."
    local failed=0

    for gen in {0..9}; do
        if ! update_pokemon_generation "$gen"; then
            ((failed++))
        fi
    done

    if [[ $failed -eq 0 ]]; then
        print_color $GREEN "✓ All Pokemon generation icons updated successfully"
    else
        print_color $YELLOW "⚠ $failed generation(s) failed to update"
    fi
}

# Function to update all Pokemon variants
update_all_pokemon_variants() {
    print_color $BLUE "Updating all Pokemon variant icons..."
    local failed=0

    for gen in {1..9}; do
        if ! update_pokemon_variants "$gen"; then
            ((failed++))
        fi
    done

    if [[ $failed -eq 0 ]]; then
        print_color $GREEN "✓ All Pokemon variant icons updated successfully"
    else
        print_color $YELLOW "⚠ $failed variant generation(s) failed to update"
    fi
}

# Function to show Pokemon generation menu
show_pokemon_menu() {
    while true; do
        echo
        print_color $CYAN "Pokemon Icons Menu"
        print_color $CYAN "=================="
        echo "1)  Generation 0 (Regional Variants)"
        echo "2)  Generation 1"
        echo "3)  Generation 2"
        echo "4)  Generation 3"
        echo "5)  Generation 4"
        echo "6)  Generation 5"
        echo "7)  Generation 6"
        echo "8)  Generation 7"
        echo "9)  Generation 8"
        echo "10) Generation 9"
        echo "11) All Generations"
        echo "12) All Variants"
        echo "0)  Back to Main Menu"
        echo

        read -p "Select generation to update (0-12): " choice

        case $choice in
            1) update_pokemon_generation "0" ;;
            2) update_pokemon_generation "1" ;;
            3) update_pokemon_generation "2" ;;
            4) update_pokemon_generation "3" ;;
            5) update_pokemon_generation "4" ;;
            6) update_pokemon_generation "5" ;;
            7) update_pokemon_generation "6" ;;
            8) update_pokemon_generation "7" ;;
            9) update_pokemon_generation "8" ;;
            10) update_pokemon_generation "9" ;;
            11) update_all_pokemon ;;
            12) update_all_pokemon_variants ;;
            0) break ;;
            *) print_color $RED "Invalid choice. Please try again." ;;
        esac
    done
}

# Function to show localization menu
show_localization_menu() {
    while true; do
        echo
        print_color $CYAN "Localization Menu"
        print_color $CYAN "================="
        echo "1)  German (de)"
        echo "2)  French (fr)"
        echo "3)  Spanish Spain (es-ES)"
        echo "4)  Spanish Mexico (es-MX)"
        echo "5)  Italian (it)"
        echo "6)  Portuguese Brazil (pt-BR)"
        echo "7)  Japanese (ja)"
        echo "8)  Korean (ko)"
        echo "9)  Chinese Simplified (zh-CN)"
        echo "10) Chinese Traditional (zh-TW)"
        echo "11) Russian (ru)"
        echo "12) Turkish (tr)"
        echo "13) Romanian (ro)"
        echo "14) Catalan (ca)"
        echo "15) Danish (da)"
        echo "0)  Back to Main Menu"
        echo

        read -p "Select language (0-15): " choice

        case $choice in
            1)
                echo "Select spritesheet type:"
                echo "1) Types"
                echo "2) Statuses"
                read -p "Choice: " type_choice
                case $type_choice in
                    1) update_types "de" ;;
                    2) update_statuses "de" ;;
                    *) print_color $RED "Invalid choice." ;;
                esac
                ;;
            2)
                echo "Select spritesheet type:"
                echo "1) Types"
                echo "2) Statuses"
                read -p "Choice: " type_choice
                case $type_choice in
                    1) update_types "fr" ;;
                    2) update_statuses "fr" ;;
                    *) print_color $RED "Invalid choice." ;;
                esac
                ;;
            3)
                echo "Select spritesheet type:"
                echo "1) Types"
                echo "2) Statuses"
                read -p "Choice: " type_choice
                case $type_choice in
                    1) update_types "es-ES" ;;
                    2) update_statuses "es-ES" ;;
                    *) print_color $RED "Invalid choice." ;;
                esac
                ;;
            4)
                echo "Select spritesheet type:"
                echo "1) Types"
                echo "2) Statuses"
                read -p "Choice: " type_choice
                case $type_choice in
                    1) update_types "es-MX" ;;
                    2) update_statuses "es-MX" ;;
                    *) print_color $RED "Invalid choice." ;;
                esac
                ;;
            5)
                echo "Select spritesheet type:"
                echo "1) Types"
                echo "2) Statuses"
                read -p "Choice: " type_choice
                case $type_choice in
                    1) update_types "it" ;;
                    2) update_statuses "it" ;;
                    *) print_color $RED "Invalid choice." ;;
                esac
                ;;
            6)
                echo "Select spritesheet type:"
                echo "1) Types"
                echo "2) Statuses"
                read -p "Choice: " type_choice
                case $type_choice in
                    1) update_types "pt-BR" ;;
                    2) update_statuses "pt-BR" ;;
                    *) print_color $RED "Invalid choice." ;;
                esac
                ;;
            7)
                echo "Select spritesheet type:"
                echo "1) Types"
                echo "2) Statuses"
                read -p "Choice: " type_choice
                case $type_choice in
                    1) update_types "ja" ;;
                    2) update_statuses "ja" ;;
                    *) print_color $RED "Invalid choice." ;;
                esac
                ;;
            8)
                echo "Select spritesheet type:"
                echo "1) Types"
                echo "2) Statuses"
                read -p "Choice: " type_choice
                case $type_choice in
                    1) update_types "ko" ;;
                    2) update_statuses "ko" ;;
                    *) print_color $RED "Invalid choice." ;;
                esac
                ;;
            9)
                echo "Select spritesheet type:"
                echo "1) Types"
                echo "2) Statuses"
                read -p "Choice: " type_choice
                case $type_choice in
                    1) update_types "zh-CN" ;;
                    2) update_statuses "zh-CN" ;;
                    *) print_color $RED "Invalid choice." ;;
                esac
                ;;
            10)
                echo "Select spritesheet type:"
                echo "1) Types"
                echo "2) Statuses"
                read -p "Choice: " type_choice
                case $type_choice in
                    1) update_types "zh-TW" ;;
                    2) update_statuses "zh-TW" ;;
                    *) print_color $RED "Invalid choice." ;;
                esac
                ;;
            11)
                echo "Select spritesheet type:"
                echo "1) Types"
                echo "2) Statuses"
                read -p "Choice: " type_choice
                case $type_choice in
                    1) update_types "ru" ;;
                    2) update_statuses "ru" ;;
                    *) print_color $RED "Invalid choice." ;;
                esac
                ;;
            12)
                echo "Select spritesheet type:"
                echo "1) Types"
                echo "2) Statuses"
                read -p "Choice: " type_choice
                case $type_choice in
                    1) update_types "tr" ;;
                    2) update_statuses "tr" ;;
                    *) print_color $RED "Invalid choice." ;;
                esac
                ;;
            13)
                echo "Select spritesheet type:"
                echo "1) Types"
                echo "2) Statuses"
                read -p "Choice: " type_choice
                case $type_choice in
                    1) update_types "ro" ;;
                    2) update_statuses "ro" ;;
                    *) print_color $RED "Invalid choice." ;;
                esac
                ;;
            14)
                echo "Select spritesheet type:"
                echo "1) Types"
                echo "2) Statuses"
                read -p "Choice: " type_choice
                case $type_choice in
                    1) update_types "ca" ;;
                    2) update_statuses "ca" ;;
                    *) print_color $RED "Invalid choice." ;;
                esac
                ;;
            15)
                echo "Select spritesheet type:"
                echo "1) Types"
                echo "2) Statuses"
                read -p "Choice: " type_choice
                case $type_choice in
                    1) update_types "da" ;;
                    2) update_statuses "da" ;;
                    *) print_color $RED "Invalid choice." ;;
                esac
                ;;
            0) break ;;
            *) print_color $RED "Invalid choice. Please try again." ;;
        esac
    done
}

# Main menu function
show_main_menu() {
    while true; do
        print_header
        echo "1) Update Pokemon Icons"
        echo "2) Update Items"
        echo "3) Update Types (English)"
        echo "4) Update Statuses (English)"
        echo "5) Update Localized Spritesheets"
        echo "6) Update All English Spritesheets"
        echo "0) Exit"
        echo

        read -p "Select an option (0-6): " choice

        case $choice in
            1) show_pokemon_menu ;;
            2) update_items ;;
            3) update_types ;;
            4) update_statuses ;;
            5) show_localization_menu ;;
            6)
                print_color $BLUE "Updating all English spritesheets..."
                update_all_pokemon
                update_items
                update_types
                update_statuses
                print_color $GREEN "✓ All English spritesheets updated!"
                ;;
            0)
                print_color $GREEN "Goodbye!"
                exit 0
                ;;
            *) print_color $RED "Invalid choice. Please try again." ;;
        esac

        echo
        read -p "Press Enter to continue..."
    done
}

# Main execution
main() {
    # Check prerequisites
    check_texturepacker
    check_directory

    # Show main menu
    show_main_menu
}

# Run main function
main "$@"
