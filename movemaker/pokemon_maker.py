#!/usr/bin/env python3

import os
import sys
from typing import Dict, List, Optional, Tuple

# Constants
POKEMON_TYPES = [
    "NORMAL", "FIRE", "WATER", "ELECTRIC", "GRASS", "ICE", "FIGHTING", "POISON",
    "GROUND", "FLYING", "PSYCHIC", "BUG", "ROCK", "GHOST", "DRAGON", "DARK",
    "STEEL", "FAIRY", "STELLAR"
]

GROWTH_RATES = [
    "ERRATIC", "FAST", "MEDIUM_FAST", "MEDIUM_SLOW", "SLOW", "FLUCTUATING"
]

# Common abilities for quick selection
COMMON_ABILITIES = [
    "NONE", "STENCH", "DRIZZLE", "SPEED_BOOST", "BATTLE_ARMOR", "STURDY",
    "DAMP", "LIMBER", "SAND_VEIL", "STATIC", "VOLT_ABSORB", "WATER_ABSORB",
    "OBLIVIOUS", "CLOUD_NINE", "COMPOUND_EYES", "INSOMNIA", "COLOR_CHANGE",
    "IMMUNITY", "FLASH_FIRE", "SHIELD_DUST", "OWN_TEMPO", "SUCTION_CUPS",
    "INTIMIDATE", "SHADOW_TAG", "ROUGH_SKIN", "WONDER_GUARD", "LEVITATE",
    "EFFECT_SPORE", "SYNCHRONIZE", "CLEAR_BODY", "NATURAL_CURE", "LIGHTNING_ROD",
    "SERENE_GRACE", "SWIFT_SWIM", "CHLOROPHYLL", "ILLUMINATE", "TRACE",
    "HUGE_POWER", "POISON_POINT", "INNER_FOCUS", "MAGMA_ARMOR", "WATER_VEIL",
    "MAGNET_PULL", "SOUNDPROOF", "RAIN_DISH", "SAND_STREAM", "PRESSURE",
    "THICK_FAT", "EARLY_BIRD", "FLAME_BODY", "RUN_AWAY", "KEEN_EYE",
    "HYPER_CUTTER", "PICKUP", "TRUANT", "HUSTLE", "CUTE_CHARM", "PLUS",
    "MINUS", "FORECAST", "STICKY_HOLD", "SHED_SKIN", "GUTS", "MARVEL_SCALE",
    "LIQUID_OOZE", "OVERGROW", "BLAZE", "TORRENT", "SWARM", "ROCK_HEAD",
    "DROUGHT", "ARENA_TRAP", "VITAL_SPIRIT", "WHITE_SMOKE", "PURE_POWER",
    "SHELL_ARMOR", "AIR_LOCK", "TANGLED_FEET", "MOTOR_DRIVE", "RIVALRY",
    "STEADFAST", "SNOW_CLOAK", "GLUTTONY", "ANGER_POINT", "UNBURDEN",
    "HEATPROOF", "SIMPLE", "DRY_SKIN", "DOWNLOAD", "IRON_FIST", "POISON_HEAL",
    "ADAPTABILITY", "SKILL_LINK", "HYDRATION", "SOLAR_POWER", "QUICK_FEET",
    "NORMALIZE", "SNIPER", "MAGIC_GUARD", "NO_GUARD", "STALL", "TECHNICIAN",
    "LEAF_GUARD", "KLUTZ", "MOLD_BREAKER", "SUPER_LUCK", "AFTERMATH",
    "ANTICIPATION", "FOREWARN", "UNAWARE", "TINTED_LENS", "FILTER",
    "SOLID_ROCK", "ICE_BODY", "SNOW_WARNING", "HONEY_GATHER", "FRISK",
    "RECKLESS", "MULTITYPE", "FLOWER_GIFT", "BAD_DREAMS", "BIG_PECKS"
]

class PokemonMaker:
    def __init__(self):
        self.clear_state()

    def clear_state(self):
        self.species_name = ""
        self.generation = 1
        self.is_sublegendary = False
        self.is_legendary = False
        self.is_mythical = False
        self.category = ""
        self.type1 = ""
        self.type2 = None
        self.height = 0.0
        self.weight = 0.0
        self.ability1 = ""
        self.ability2 = ""
        self.hidden_ability = ""
        self.stat_total = 0
        self.hp = 0
        self.attack = 0
        self.defense = 0
        self.sp_attack = 0
        self.sp_defense = 0
        self.speed = 0
        self.catch_rate = 0
        self.base_friendship = 0
        self.base_exp = 0
        self.growth_rate = ""
        self.gender_ratio = 50
        self.can_change_form = False

    def print_welcome(self):
        print("="*60)
        print(" PokéRogue Pokemon Species Maker")
        print("="*60)
        print("This tool helps you generate TypeScript code for Pokemon species")
        print("that can be pasted into the game's pokemon-species.ts file.")
        print("-"*60)

    def get_species_name(self):
        print("\nEnter the Pokemon species name (e.g., STEVE, PIKACHU):")
        while True:
            name = input("> ").strip().upper()
            if name and name.replace("_", "").isalnum():
                self.species_name = name
                break
            else:
                print("Please enter a valid species name (letters, numbers, underscores only).")

    def get_generation(self):
        print("\nEnter generation (1-9):")
        while True:
            try:
                gen = int(input("> "))
                if 1 <= gen <= 9:
                    self.generation = gen
                    break
                else:
                    print("Generation must be between 1 and 9.")
            except ValueError:
                print("Please enter a number.")

    def get_legendary_status(self):
        print("\nIs this Pokemon legendary/mythical? (affects rarity)")
        print("1. Regular Pokemon")
        print("2. Sub-legendary")
        print("3. Legendary")
        print("4. Mythical")

        while True:
            choice = input("Enter your choice (1-4): ")
            if choice == "1":
                self.is_sublegendary = False
                self.is_legendary = False
                self.is_mythical = False
                break
            elif choice == "2":
                self.is_sublegendary = True
                self.is_legendary = False
                self.is_mythical = False
                break
            elif choice == "3":
                self.is_sublegendary = False
                self.is_legendary = True
                self.is_mythical = False
                break
            elif choice == "4":
                self.is_sublegendary = False
                self.is_legendary = False
                self.is_mythical = True
                break
            else:
                print("Invalid choice. Please try again.")

    def get_category(self):
        print("\nEnter Pokemon category (e.g., 'Brown Thraser Pokémon', 'Mouse Pokémon'):")
        self.category = input("> ").strip()

    def get_types(self):
        print("\nSelect primary type:")
        for i, ptype in enumerate(POKEMON_TYPES, 1):
            print(f"{i:2d}. {ptype}")

        while True:
            choice = input(f"Enter your choice (1-{len(POKEMON_TYPES)}): ")
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(POKEMON_TYPES):
                    self.type1 = POKEMON_TYPES[idx]
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number.")

        print(f"\nPrimary type: {self.type1}")
        print("Select secondary type (or press Enter for single type):")
        for i, ptype in enumerate(POKEMON_TYPES, 1):
            print(f"{i:2d}. {ptype}")

        while True:
            choice = input(f"Enter your choice (1-{len(POKEMON_TYPES)}, or Enter for none): ").strip()
            if choice == "":
                self.type2 = None
                break
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(POKEMON_TYPES):
                    if POKEMON_TYPES[idx] != self.type1:
                        self.type2 = POKEMON_TYPES[idx]
                        break
                    else:
                        print("Secondary type cannot be the same as primary type.")
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number or press Enter for none.")

    def get_physical_stats(self):
        print("\nEnter height in meters (e.g., 0.3, 1.8):")
        while True:
            try:
                height = float(input("> "))
                if height > 0:
                    self.height = height
                    break
                else:
                    print("Height must be positive.")
            except ValueError:
                print("Please enter a valid number.")

        print("\nEnter weight in kg (e.g., 1.8, 70.5):")
        while True:
            try:
                weight = float(input("> "))
                if weight > 0:
                    self.weight = weight
                    break
                else:
                    print("Weight must be positive.")
            except ValueError:
                print("Please enter a valid number.")

    def get_abilities(self):
        print("\nSelect abilities from common list or enter custom:")
        print("Common abilities (enter number):")
        for i, ability in enumerate(COMMON_ABILITIES[:20], 1):  # Show first 20
            print(f"{i:2d}. {ability}")
        print("... (and more)")
        print("\nOr type 'custom' to enter ability names manually")

        def get_ability(prompt):
            while True:
                print(f"\n{prompt}")
                choice = input("> ").strip()

                if choice.upper() == "CUSTOM":
                    ability = input("Enter ability name (e.g., KEEN_EYE): ").strip().upper()
                    return ability
                elif choice.isdigit():
                    idx = int(choice) - 1
                    if 0 <= idx < len(COMMON_ABILITIES):
                        return COMMON_ABILITIES[idx]
                    else:
                        print("Invalid choice.")
                else:
                    # Assume it's a custom ability name
                    return choice.upper()

        self.ability1 = get_ability("Primary ability:")
        self.ability2 = get_ability("Secondary ability:")
        self.hidden_ability = get_ability("Hidden ability:")

    def get_base_stats(self):
        print("\nEnter base stats (HP, Attack, Defense, Sp.Attack, Sp.Defense, Speed):")
        print("Tip: Most Pokemon have base stat totals between 300-600")

        def get_stat(stat_name, min_val=1, max_val=255):
            while True:
                try:
                    value = int(input(f"{stat_name} (1-255): "))
                    if min_val <= value <= max_val:
                        return value
                    else:
                        print(f"{stat_name} must be between {min_val} and {max_val}.")
                except ValueError:
                    print("Please enter a number.")

        self.hp = get_stat("HP")
        self.attack = get_stat("Attack")
        self.defense = get_stat("Defense")
        self.sp_attack = get_stat("Sp. Attack")
        self.sp_defense = get_stat("Sp. Defense")
        self.speed = get_stat("Speed")

        self.stat_total = self.hp + self.attack + self.defense + self.sp_attack + self.sp_defense + self.speed
        print(f"\nTotal base stats: {self.stat_total}")

    def get_game_stats(self):
        print("\nEnter catch rate (1-255, lower = harder to catch):")
        print("Examples: Legendary ~3, Rare ~45, Common ~255")
        while True:
            try:
                rate = int(input("> "))
                if 1 <= rate <= 255:
                    self.catch_rate = rate
                    break
                else:
                    print("Catch rate must be between 1 and 255.")
            except ValueError:
                print("Please enter a number.")

        print("\nEnter base friendship (0-255, usually 35-100):")
        while True:
            try:
                friendship = int(input("> "))
                if 0 <= friendship <= 255:
                    self.base_friendship = friendship
                    break
                else:
                    print("Base friendship must be between 0 and 255.")
            except ValueError:
                print("Please enter a number.")

        print("\nEnter base experience yield (50-300 typical range):")
        while True:
            try:
                exp = int(input("> "))
                if exp > 0:
                    self.base_exp = exp
                    break
                else:
                    print("Base experience must be positive.")
            except ValueError:
                print("Please enter a number.")

    def get_growth_rate(self):
        print("\nSelect growth rate:")
        for i, rate in enumerate(GROWTH_RATES, 1):
            print(f"{i}. {rate}")

        while True:
            choice = input(f"Enter your choice (1-{len(GROWTH_RATES)}): ")
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(GROWTH_RATES):
                    self.growth_rate = GROWTH_RATES[idx]
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number.")

    def get_gender_ratio(self):
        print("\nEnter gender ratio (% male, or 'null' for genderless):")
        print("Examples: 50 (50% male), 25 (25% male, 75% female), 100 (100% male)")
        while True:
            choice = input("> ").strip().lower()
            if choice == "null" or choice == "none":
                self.gender_ratio = None
                break
            try:
                ratio = int(choice)
                if 0 <= ratio <= 100:
                    self.gender_ratio = ratio
                    break
                else:
                    print("Gender ratio must be between 0 and 100, or 'null'.")
            except ValueError:
                print("Please enter a number or 'null'.")

    def get_form_change(self):
        print("\nCan this Pokemon change forms? (y/n):")
        while True:
            choice = input("> ").strip().lower()
            if choice in ['y', 'yes']:
                self.can_change_form = True
                break
            elif choice in ['n', 'no']:
                self.can_change_form = False
                break
            else:
                print("Please enter 'y' or 'n'.")

    def generate_code(self):
        type2_str = f"PokemonType.{self.type2}" if self.type2 else "null"
        gender_str = str(self.gender_ratio) if self.gender_ratio is not None else "null"

        code = f"""    new PokemonSpecies(
      Species.{self.species_name},
      {self.generation}, // Generation
      {str(self.is_sublegendary).lower()}, // Sub-legendary
      {str(self.is_legendary).lower()}, // Legendary
      {str(self.is_mythical).lower()}, // Mythical
      "{self.category}",
      PokemonType.{self.type1},
      {type2_str},
      {self.height}, // Height in meters
      {self.weight}, // Weight in kg
      Abilities.{self.ability1}, // Primary ability
      Abilities.{self.ability2}, // Secondary ability
      Abilities.{self.hidden_ability}, // Hidden ability
      {self.stat_total}, // Base stat total
      {self.hp}, // HP
      {self.attack}, // Attack
      {self.defense}, // Defense
      {self.sp_attack}, // Sp. Attack
      {self.sp_defense}, // Sp. Defense
      {self.speed}, // Speed
      {self.catch_rate}, // Catch rate
      {self.base_friendship}, // Base friendship
      {self.base_exp}, // Base experience
      GrowthRate.{self.growth_rate}, // Growth rate
      {gender_str}, // Gender ratio (% male)
      {str(self.can_change_form).lower()}, // Can change form
    ),"""

        return code

    def display_summary(self):
        print("\n" + "="*60)
        print(" POKEMON SUMMARY")
        print("="*60)
        print(f"Species: {self.species_name}")
        print(f"Generation: {self.generation}")
        print(f"Category: {self.category}")
        print(f"Type: {self.type1}" + (f"/{self.type2}" if self.type2 else ""))
        print(f"Height: {self.height}m, Weight: {self.weight}kg")
        print(f"Abilities: {self.ability1}, {self.ability2}, {self.hidden_ability} (Hidden)")
        print(f"Base Stats: {self.hp}/{self.attack}/{self.defense}/{self.sp_attack}/{self.sp_defense}/{self.speed} (Total: {self.stat_total})")
        print(f"Catch Rate: {self.catch_rate}, Friendship: {self.base_friendship}, Exp: {self.base_exp}")
        print(f"Growth Rate: {self.growth_rate}")
        print(f"Gender Ratio: {self.gender_ratio}% male" if self.gender_ratio is not None else "Genderless")

        status = []
        if self.is_sublegendary: status.append("Sub-legendary")
        if self.is_legendary: status.append("Legendary")
        if self.is_mythical: status.append("Mythical")
        if self.can_change_form: status.append("Form-changing")
        if status:
            print(f"Special: {', '.join(status)}")
        print("-"*60)

    def run(self):
        self.print_welcome()

        try:
            self.get_species_name()
            self.get_generation()
            self.get_legendary_status()
            self.get_category()
            self.get_types()
            self.get_physical_stats()
            self.get_abilities()
            self.get_base_stats()
            self.get_game_stats()
            self.get_growth_rate()
            self.get_gender_ratio()
            self.get_form_change()

            self.display_summary()

            print("\nGenerated TypeScript code:")
            print("="*60)
            print(self.generate_code())
            print("="*60)

            print("\nAdditional steps needed:")
            print("1. Add Species.{} to src/enums/species.ts".format(self.species_name))
            print("2. Add the above code to src/data/pokemon-species.ts in initSpecies()")
            print("3. Configure starter cost in src/data/balance/starters.ts")
            print("4. Set up moves in src/data/balance/pokemon-level-moves.ts")
            print("5. Add sprite assets and regenerate atlases")
            print("\nSee ADDING_POKEMON_GUIDE.md for detailed instructions!")

        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
            sys.exit(0)
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            sys.exit(1)

def main():
    maker = PokemonMaker()

    while True:
        maker.run()

        print("\n" + "="*60)
        choice = input("Generate another Pokemon? (y/n): ").strip().lower()
        if choice not in ['y', 'yes']:
            break

        maker.clear_state()
        print("\n")

    print("Thank you for using Pokemon Maker!")

if __name__ == "__main__":
    main()
