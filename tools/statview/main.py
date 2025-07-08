#!/usr/bin/env python3
"""
Pokemon Species Stat Viewer for PokeRogue

This script parses the TypeScript pokemon-species.ts file and displays
Pokemon stats in a clean, readable format in the terminal.
"""

import re
import sys
import os
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from pathlib import Path

# ANSI color codes for terminal formatting
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    GRAY = '\033[90m'

# Pokemon type colors
TYPE_COLORS = {
    'NORMAL': Colors.WHITE,
    'FIGHTING': Colors.RED,
    'FLYING': Colors.CYAN,
    'POISON': Colors.MAGENTA,
    'GROUND': Colors.YELLOW,
    'ROCK': Colors.YELLOW,
    'BUG': Colors.GREEN,
    'GHOST': Colors.MAGENTA,
    'STEEL': Colors.GRAY,
    'FIRE': Colors.RED,
    'WATER': Colors.BLUE,
    'GRASS': Colors.GREEN,
    'ELECTRIC': Colors.YELLOW,
    'PSYCHIC': Colors.MAGENTA,
    'ICE': Colors.CYAN,
    'DRAGON': Colors.BLUE,
    'DARK': Colors.GRAY,
    'FAIRY': Colors.MAGENTA,
    'STELLAR': Colors.WHITE
}

@dataclass
class PokemonStats:
    id: int
    name: str
    generation: int
    sub_legendary: bool
    legendary: bool
    mythical: bool
    species_name: str
    type1: str
    type2: Optional[str]
    height: float
    weight: float
    ability1: str
    ability2: str
    ability_hidden: str
    base_total: int
    base_hp: int
    base_atk: int
    base_def: int
    base_spatk: int
    base_spdef: int
    base_spd: int
    catch_rate: int
    base_friendship: int
    base_exp: int
    growth_rate: str
    male_percent: Optional[float]
    gender_diffs: bool

class PokemonParser:
    def __init__(self, species_file_path: str):
        self.species_file_path = species_file_path
        self.species_enum = {}
        self.abilities_enum = {}
        self.types_enum = {}
        self.growth_rates = {}
        self.pokemon_data = []

    def load_enums(self):
        """Load enum mappings from TypeScript files"""
        base_dir = Path(self.species_file_path).parent.parent

        # Load Species enum
        species_file = base_dir / "enums" / "species.ts"
        if species_file.exists():
            with open(species_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Parse enum values
                matches = re.findall(r'(\w+)\s*=?\s*(\d+)?,?', content)
                current_value = 1
                for match in matches:
                    name, value = match
                    if name in ['enum', 'Species', 'export']:
                        continue
                    if value:
                        current_value = int(value)
                    self.species_enum[current_value] = name
                    current_value += 1

        # Load Abilities enum
        abilities_file = base_dir / "enums" / "abilities.ts"
        if abilities_file.exists():
            with open(abilities_file, 'r', encoding='utf-8') as f:
                content = f.read()
                matches = re.findall(r'(\w+),?', content)
                for i, match in enumerate(matches):
                    if match in ['enum', 'Abilities', 'export']:
                        continue
                    self.abilities_enum[i] = match

        # Load PokemonType enum
        types_file = base_dir / "enums" / "pokemon-type.ts"
        if types_file.exists():
            with open(types_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Handle the special case where UNKNOWN = -1
                type_matches = re.findall(r'(\w+)\s*=?\s*(-?\d+)?,?', content)
                current_value = -1
                for match in type_matches:
                    name, value = match
                    if name in ['enum', 'PokemonType', 'export']:
                        continue
                    if value:
                        current_value = int(value)
                    self.types_enum[current_value] = name
                    current_value += 1

        # Common growth rates
        self.growth_rates = {
            'SLOW': 'Slow',
            'MEDIUM_SLOW': 'Medium Slow',
            'MEDIUM_FAST': 'Medium Fast',
            'FAST': 'Fast',
            'ERRATIC': 'Erratic',
            'FLUCTUATING': 'Fluctuating'
        }

    def parse_pokemon_data(self):
        """Parse Pokemon data from the species file"""
        with open(self.species_file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find all PokemonSpecies constructor calls
        pattern = r'new PokemonSpecies\s*\(\s*([^)]+)\)'
        matches = re.findall(pattern, content, re.DOTALL)

        for match in matches:
            try:
                # Split parameters and clean them
                params = [p.strip().rstrip(',') for p in match.split(',')]

                if len(params) < 24:  # Minimum required parameters
                    continue

                # Parse species ID
                species_id_match = re.search(r'Species\.(\w+)', params[0])
                if not species_id_match:
                    continue

                species_name = species_id_match.group(1)
                species_id = None

                # Find the ID from our enum
                for id_val, name in self.species_enum.items():
                    if name == species_name:
                        species_id = id_val
                        break

                if species_id is None:
                    continue

                # Parse types
                type1_match = re.search(r'PokemonType\.(\w+)', params[6])
                type2_match = re.search(r'PokemonType\.(\w+)', params[7])

                type1 = type1_match.group(1) if type1_match else 'NORMAL'
                type2 = type2_match.group(1) if type2_match and type2_match.group(1) != 'null' else None

                # Parse abilities
                ability1_match = re.search(r'Abilities\.(\w+)', params[10])
                ability2_match = re.search(r'Abilities\.(\w+)', params[11])
                ability_hidden_match = re.search(r'Abilities\.(\w+)', params[12])

                ability1 = ability1_match.group(1) if ability1_match else 'NONE'
                ability2 = ability2_match.group(1) if ability2_match else 'NONE'
                ability_hidden = ability_hidden_match.group(1) if ability_hidden_match else 'NONE'

                # Parse growth rate
                growth_rate_match = re.search(r'GrowthRate\.(\w+)', params[23])
                growth_rate = growth_rate_match.group(1) if growth_rate_match else 'MEDIUM_FAST'

                # Create Pokemon stats object
                pokemon = PokemonStats(
                    id=species_id,
                    name=species_name.replace('_', ' ').title(),
                    generation=int(params[1]),
                    sub_legendary=params[2] == 'true',
                    legendary=params[3] == 'true',
                    mythical=params[4] == 'true',
                    species_name=params[5].strip('"'),
                    type1=type1,
                    type2=type2,
                    height=float(params[8]),
                    weight=float(params[9]),
                    ability1=ability1,
                    ability2=ability2,
                    ability_hidden=ability_hidden,
                    base_total=int(params[13]),
                    base_hp=int(params[14]),
                    base_atk=int(params[15]),
                    base_def=int(params[16]),
                    base_spatk=int(params[17]),
                    base_spdef=int(params[18]),
                    base_spd=int(params[19]),
                    catch_rate=int(params[20]),
                    base_friendship=int(params[21]),
                    base_exp=int(params[22]),
                    growth_rate=growth_rate,
                    male_percent=float(params[24]) if params[24] != 'null' else None,
                    gender_diffs=params[25] == 'true' if len(params) > 25 else False
                )

                self.pokemon_data.append(pokemon)

            except (ValueError, IndexError) as e:
                continue  # Skip malformed entries

        # Sort by ID
        self.pokemon_data.sort(key=lambda x: x.id)

    def format_pokemon_display(self, pokemon: PokemonStats) -> str:
        """Format a Pokemon's stats for display"""
        output = []

        # Header with name and ID
        rarity = ""
        if pokemon.mythical:
            rarity = f" {Colors.MAGENTA}[MYTHICAL]{Colors.RESET}"
        elif pokemon.legendary:
            rarity = f" {Colors.YELLOW}[LEGENDARY]{Colors.RESET}"
        elif pokemon.sub_legendary:
            rarity = f" {Colors.CYAN}[SUB-LEGENDARY]{Colors.RESET}"

        output.append(f"{Colors.BOLD}{Colors.WHITE}#{pokemon.id:03d} {pokemon.name}{rarity}{Colors.RESET}")
        output.append(f"{Colors.GRAY}{pokemon.species_name} | Gen {pokemon.generation}{Colors.RESET}")

        # Types
        type1_color = TYPE_COLORS.get(pokemon.type1, Colors.WHITE)
        type_str = f"{type1_color}{pokemon.type1}{Colors.RESET}"
        if pokemon.type2:
            type2_color = TYPE_COLORS.get(pokemon.type2, Colors.WHITE)
            type_str += f" / {type2_color}{pokemon.type2}{Colors.RESET}"
        output.append(f"Type: {type_str}")

        # Physical stats
        output.append(f"Height: {pokemon.height}m | Weight: {pokemon.weight}kg")

        # Abilities
        abilities = [pokemon.ability1.replace('_', ' ').title()]
        if pokemon.ability2 != 'NONE':
            abilities.append(pokemon.ability2.replace('_', ' ').title())
        ability_str = f"Abilities: {', '.join(abilities)}"
        if pokemon.ability_hidden != 'NONE':
            ability_str += f" | Hidden: {pokemon.ability_hidden.replace('_', ' ').title()}"
        output.append(ability_str)

        # Base stats
        output.append(f"\n{Colors.BOLD}Base Stats (Total: {pokemon.base_total}){Colors.RESET}")
        stats = [
            ("HP", pokemon.base_hp, Colors.GREEN),
            ("Attack", pokemon.base_atk, Colors.RED),
            ("Defense", pokemon.base_def, Colors.BLUE),
            ("Sp. Atk", pokemon.base_spatk, Colors.MAGENTA),
            ("Sp. Def", pokemon.base_spdef, Colors.CYAN),
            ("Speed", pokemon.base_spd, Colors.YELLOW)
        ]

        for stat_name, value, color in stats:
            bar_length = min(value // 5, 30)  # Scale bar length
            bar = "█" * bar_length + "░" * (30 - bar_length)
            output.append(f"{stat_name:>8}: {color}{value:>3}{Colors.RESET} {Colors.GRAY}{bar}{Colors.RESET}")

        # Additional info
        output.append(f"\nCatch Rate: {pokemon.catch_rate} | Base Friendship: {pokemon.base_friendship}")
        output.append(f"Base EXP: {pokemon.base_exp} | Growth Rate: {self.growth_rates.get(pokemon.growth_rate, pokemon.growth_rate)}")

        # Gender info
        if pokemon.male_percent is not None:
            female_percent = 100 - pokemon.male_percent
            output.append(f"Gender Ratio: {pokemon.male_percent:.1f}% ♂ / {female_percent:.1f}% ♀")
        else:
            output.append("Gender: Genderless")

        return '\n'.join(output)

    def search_pokemon(self, query: str) -> List[PokemonStats]:
        """Search for Pokemon by name or ID"""
        results = []
        query_lower = query.lower()

        # Try to parse as ID first
        try:
            search_id = int(query)
            results.extend([p for p in self.pokemon_data if p.id == search_id])
        except ValueError:
            pass

        # Search by name
        for pokemon in self.pokemon_data:
            if query_lower in pokemon.name.lower():
                results.append(pokemon)

        return results[:10]  # Limit results

    def list_pokemon_range(self, start: int = 1, end: int = 10) -> List[PokemonStats]:
        """List Pokemon in a range"""
        return [p for p in self.pokemon_data if start <= p.id <= end]

def main():
    # Get the script directory and find the species file
    script_dir = Path(__file__).parent
    species_file = script_dir / "../../src/data/pokemon-species.ts"

    if not species_file.exists():
        print(f"{Colors.RED}Error: Could not find pokemon-species.ts at {species_file}{Colors.RESET}")
        sys.exit(1)

    print(f"{Colors.BOLD}{Colors.CYAN}PokeRogue Species Stat Viewer{Colors.RESET}")
    print(f"{Colors.GRAY}Loading Pokemon data...{Colors.RESET}")

    parser = PokemonParser(str(species_file))
    parser.load_enums()
    parser.parse_pokemon_data()

    print(f"{Colors.GREEN}Loaded {len(parser.pokemon_data)} Pokemon species{Colors.RESET}")
    print(f"{Colors.GRAY}Usage: Enter Pokemon name or ID, 'list <start>-<end>', or 'quit'{Colors.RESET}\n")

    while True:
        try:
            query = input(f"{Colors.BOLD}> {Colors.RESET}").strip()

            if query.lower() in ['quit', 'exit', 'q']:
                break

            if query.lower().startswith('list'):
                # Handle range listing
                parts = query.split()
                if len(parts) > 1 and '-' in parts[1]:
                    try:
                        start, end = map(int, parts[1].split('-'))
                        pokemon_list = parser.list_pokemon_range(start, end)
                        for pokemon in pokemon_list:
                            print(f"{Colors.BOLD}#{pokemon.id:03d}{Colors.RESET} {pokemon.name}")
                    except ValueError:
                        print(f"{Colors.RED}Invalid range format. Use: list 1-10{Colors.RESET}")
                else:
                    # List first 20
                    pokemon_list = parser.list_pokemon_range(1, 20)
                    for pokemon in pokemon_list:
                        print(f"{Colors.BOLD}#{pokemon.id:03d}{Colors.RESET} {pokemon.name}")
                continue

            if not query:
                continue

            results = parser.search_pokemon(query)

            if not results:
                print(f"{Colors.RED}No Pokemon found matching '{query}'{Colors.RESET}")
                continue

            if len(results) == 1:
                print(f"\n{parser.format_pokemon_display(results[0])}\n")
            else:
                print(f"\n{Colors.BOLD}Found {len(results)} matches:{Colors.RESET}")
                for pokemon in results:
                    print(f"{Colors.BOLD}#{pokemon.id:03d}{Colors.RESET} {pokemon.name}")
                print(f"{Colors.GRAY}Enter a specific name or ID for detailed stats{Colors.RESET}\n")

        except KeyboardInterrupt:
            print(f"\n{Colors.GRAY}Goodbye!{Colors.RESET}")
            break
        except Exception as e:
            print(f"{Colors.RED}Error: {e}{Colors.RESET}")

if __name__ == "__main__":
    main()
