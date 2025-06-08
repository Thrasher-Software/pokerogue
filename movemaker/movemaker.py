#!/usr/bin/env python3

import os
import sys
from typing import Dict, List, Optional, Tuple, Union

# Constants
POKEMON_TYPES = [
    "NORMAL", "FIRE", "WATER", "ELECTRIC", "GRASS", "ICE", "FIGHTING", "POISON",
    "GROUND", "FLYING", "PSYCHIC", "BUG", "ROCK", "GHOST", "DRAGON", "DARK", 
    "STEEL", "FAIRY", "STELLAR"
]

MOVE_CATEGORIES = [
    "PHYSICAL", "SPECIAL", "STATUS"
]

MOVE_TARGETS = [
    "SELECTED", "ALL_NEAR_ENEMIES", "ALL_NEAR_OTHERS", "RANDOM_NEAR_ENEMY",
    "ALLY", "SELF", "ALL_NEAR_ALLIES", "USER_AND_ALLIES", "ALL"
]

COMMON_ATTRIBUTES = [
    "HighCritAttr", "CritOnlyAttr", "MultiHitAttr", "StatusEffectAttr", 
    "RecoilAttr", "HealAttr", "ConfuseAttr", "FlinchAttr", "StatStageChangeAttr",
    "AddBattlerTagAttr", "DelayedAttackAttr", "VariablePowerAttr", "TrapAttr",
    "RemoveHeldItemAttr", "WeatherChangeAttr", "TerrainChangeAttr", "ForceSwitchOutAttr"
]

MOVE_TRAITS = [
    "makesContact", "ignoresProtect", "soundBased", "hidesUser", "hidesTarget",
    "bitingMove", "pulseMove", "punchingMove", "slicingMove", "recklessMove",
    "ballBombMove", "powderMove", "danceMove", "windMove", "triageMove",
    "ignoresAbilities", "checkAllHits", "ignoresSubstitute", "redirectCounter",
    "reflectable"
]

STATUS_EFFECTS = [
    "BURN", "FREEZE", "PARALYSIS", "POISON", "TOXIC", "SLEEP", "CONFUSION"
]

class MoveMaker:
    def __init__(self):
        self.clear_state()
        
    def clear_state(self):
        self.move_type = ""
        self.move_id = ""
        self.pokemon_type = ""
        self.category = ""
        self.power = 0
        self.accuracy = 0
        self.pp = 0
        self.chance = 0
        self.priority = 0
        self.generation = 0
        self.target = None
        self.attributes = []
        self.traits = []
        
    def print_welcome(self):
        print("="*60)
        print(" PokéRogue Move Maker")
        print("="*60)
        print("This tool helps you generate TypeScript code for Pokémon moves")
        print("that can be pasted into the game's code.")
        print("-"*60)
        
    def get_move_type(self):
        print("\nSelect move type:")
        print("1. AttackMove")
        print("2. StatusMove")
        print("3. SelfStatusMove")
        
        while True:
            choice = input("Enter your choice (1-3): ")
            if choice == "1":
                self.move_type = "AttackMove"
                break
            elif choice == "2":
                self.move_type = "StatusMove"
                break
            elif choice == "3":
                self.move_type = "SelfStatusMove"
                break
            else:
                print("Invalid choice. Please try again.")
                
    def get_move_id(self):
        print("\nEnter move ID from the Moves enum (e.g., FLAMETHROWER, TACKLE):")
        self.move_id = input("> ").strip().upper()
        
    def get_pokemon_type(self):
        print("\nSelect Pokémon type:")
        for i, ptype in enumerate(POKEMON_TYPES, 1):
            print(f"{i}. {ptype}")
            
        while True:
            choice = input(f"Enter your choice (1-{len(POKEMON_TYPES)}): ")
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(POKEMON_TYPES):
                    self.pokemon_type = POKEMON_TYPES[idx]
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number.")
                
    def get_category(self):
        if self.move_type == "AttackMove":
            print("\nSelect move category:")
            print("1. PHYSICAL")
            print("2. SPECIAL")
            
            while True:
                choice = input("Enter your choice (1-2): ")
                if choice == "1":
                    self.category = "PHYSICAL"
                    break
                elif choice == "2":
                    self.category = "SPECIAL"
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            self.category = "STATUS"
            
    def get_power(self):
        if self.move_type == "AttackMove":
            while True:
                try:
                    self.power = int(input("\nEnter move power (0-255): "))
                    if 0 <= self.power <= 255:
                        break
                    else:
                        print("Power must be between 0 and 255.")
                except ValueError:
                    print("Please enter a number.")
        else:
            self.power = -1
            
    def get_accuracy(self):
        print("\nEnter move accuracy (0-100, -1 for never miss):")
        while True:
            try:
                self.accuracy = int(input("> "))
                if -1 <= self.accuracy <= 100:
                    break
                else:
                    print("Accuracy must be between -1 and 100.")
            except ValueError:
                print("Please enter a number.")
                
    def get_pp(self):
        print("\nEnter move PP (5-40):")
        while True:
            try:
                self.pp = int(input("> "))
                if 5 <= self.pp <= 40:
                    break
                else:
                    print("PP must be between 5 and 40.")
            except ValueError:
                print("Please enter a number.")
                
    def get_chance(self):
        print("\nEnter effect chance (0-100, -1 for guaranteed):")
        while True:
            try:
                self.chance = int(input("> "))
                if -1 <= self.chance <= 100:
                    break
                else:
                    print("Chance must be between -1 and 100.")
            except ValueError:
                print("Please enter a number.")
                
    def get_priority(self):
        print("\nEnter move priority (-7 to 5, 0 is normal):")
        while True:
            try:
                self.priority = int(input("> "))
                if -7 <= self.priority <= 5:
                    break
                else:
                    print("Priority must be between -7 and 5.")
            except ValueError:
                print("Please enter a number.")
                
    def get_generation(self):
        print("\nEnter move generation (1-9):")
        while True:
            try:
                self.generation = int(input("> "))
                if 1 <= self.generation <= 9:
                    break
                else:
                    print("Generation must be between 1 and 9.")
            except ValueError:
                print("Please enter a number.")
                
    def get_target(self):
        print("\nDo you want to specify a target? (y/n):")
        if input("> ").lower().startswith("y"):
            print("\nSelect move target:")
            for i, target in enumerate(MOVE_TARGETS, 1):
                print(f"{i}. {target}")
                
            while True:
                choice = input(f"Enter your choice (1-{len(MOVE_TARGETS)}): ")
                try:
                    idx = int(choice) - 1
                    if 0 <= idx < len(MOVE_TARGETS):
                        self.target = MOVE_TARGETS[idx]
                        break
                    else:
                        print("Invalid choice. Please try again.")
                except ValueError:
                    print("Please enter a number.")
        else:
            self.target = None
            
    def get_attributes(self):
        print("\nDo you want to add attributes to the move? (y/n):")
        if input("> ").lower().startswith("y"):
            while True:
                print("\nCommon attributes:")
                for i, attr in enumerate(COMMON_ATTRIBUTES, 1):
                    print(f"{i}. {attr}")
                print(f"{len(COMMON_ATTRIBUTES) + 1}. Custom attribute")
                print(f"{len(COMMON_ATTRIBUTES) + 2}. Done adding attributes")
                
                choice = input(f"Enter your choice (1-{len(COMMON_ATTRIBUTES) + 2}): ")
                try:
                    idx = int(choice)
                    if 1 <= idx <= len(COMMON_ATTRIBUTES):
                        self.add_attribute(COMMON_ATTRIBUTES[idx - 1])
                    elif idx == len(COMMON_ATTRIBUTES) + 1:
                        self.add_custom_attribute()
                    elif idx == len(COMMON_ATTRIBUTES) + 2:
                        break
                    else:
                        print("Invalid choice. Please try again.")
                except ValueError:
                    print("Please enter a number.")
                    
    def add_attribute(self, attr_name):
        attr_params = []
        
        if attr_name == "StatusEffectAttr":
            print("\nSelect status effect:")
            for i, effect in enumerate(STATUS_EFFECTS, 1):
                print(f"{i}. {effect}")
                
            while True:
                choice = input(f"Enter your choice (1-{len(STATUS_EFFECTS)}): ")
                try:
                    idx = int(choice) - 1
                    if 0 <= idx < len(STATUS_EFFECTS):
                        effect = f"StatusEffect.{STATUS_EFFECTS[idx]}"
                        attr_params.append(effect)
                        break
                    else:
                        print("Invalid choice. Please try again.")
                except ValueError:
                    print("Please enter a number.")
        
        elif attr_name == "StatStageChangeAttr":
            stats = input("\nEnter stats (comma separated, e.g., Stat.ATK, Stat.DEF): ").strip()
            stages = input("Enter stages (number, e.g., 1, 2, -1): ").strip()
            attr_params.append(f"[{stats}]")
            attr_params.append(stages)
            
            print("Show message? (y/n):")
            if input("> ").lower().startswith("y"):
                attr_params.append("true")
            else:
                attr_params.append("false")
                
        elif attr_name == "RecoilAttr":
            print("Use HP for calculation? (y/n):")
            use_hp = input("> ").lower().startswith("y")
            attr_params.append(str(use_hp).lower())
            
            dmg_ratio = input("Enter damage ratio (e.g., 0.25, 0.33): ").strip()
            attr_params.append(dmg_ratio)
        
        elif attr_name == "MultiHitAttr":
            print("\nSelect multi-hit type:")
            print("1. 2 hits")
            print("2. 2-5 hits")
            print("3. 3 hits")
            print("4. Custom")
            
            choice = input("Enter your choice (1-4): ")
            if choice == "1":
                attr_params.append("MultiHitType._2")
            elif choice == "2":
                attr_params.append("MultiHitType._2_TO_5")
            elif choice == "3":
                attr_params.append("MultiHitType._3")
            elif choice == "4":
                custom_type = input("Enter custom multi-hit type: ").strip()
                attr_params.append(custom_type)
                
        elif attr_name == "FlinchAttr":
            # No parameters needed
            pass
            
        else:
            print(f"\nDo you want to add parameters to {attr_name}? (y/n):")
            if input("> ").lower().startswith("y"):
                params = input("Enter parameters (comma separated): ").strip()
                attr_params = params.split(",")
                
        param_str = ", ".join(attr_params)
        if param_str:
            self.attributes.append(f"{attr_name}, {param_str}")
        else:
            self.attributes.append(attr_name)
            
    def add_custom_attribute(self):
        attr_name = input("\nEnter attribute name (e.g., HealAttr): ").strip()
        
        print(f"Do you want to add parameters to {attr_name}? (y/n):")
        if input("> ").lower().startswith("y"):
            params = input("Enter parameters (comma separated): ").strip()
            if params:
                self.attributes.append(f"{attr_name}, {params}")
            else:
                self.attributes.append(attr_name)
        else:
            self.attributes.append(attr_name)
            
    def get_traits(self):
        print("\nDo you want to add traits to the move? (y/n):")
        if input("> ").lower().startswith("y"):
            while True:
                print("\nCommon traits:")
                for i, trait in enumerate(MOVE_TRAITS, 1):
                    print(f"{i}. {trait}")
                print(f"{len(MOVE_TRAITS) + 1}. Done adding traits")
                
                choice = input(f"Enter your choice (1-{len(MOVE_TRAITS) + 1}): ")
                try:
                    idx = int(choice)
                    if 1 <= idx <= len(MOVE_TRAITS):
                        self.traits.append(MOVE_TRAITS[idx - 1])
                        print(f"Added {MOVE_TRAITS[idx - 1]}()")
                    elif idx == len(MOVE_TRAITS) + 1:
                        break
                    else:
                        print("Invalid choice. Please try again.")
                except ValueError:
                    print("Please enter a number.")
                    
    def generate_code(self):
        # Start building the code
        code = []
        code.append("new " + self.move_type + "(")
        code.append(f"  Moves.{self.move_id},")
        code.append(f"  PokemonType.{self.pokemon_type},")
        
        # For AttackMove, include category
        if self.move_type == "AttackMove":
            code.append(f"  MoveCategory.{self.category},")
            code.append(f"  {self.power},")
        
        code.append(f"  {self.accuracy},")
        code.append(f"  {self.pp},")
        code.append(f"  {self.chance},")
        code.append(f"  {self.priority},")
        code.append(f"  {self.generation},")
        code.append(")")
        
        # Add target if specified
        if self.target:
            code[-1] = code[-1] + ".target(MoveTarget." + self.target + ")"
        
        # Add attributes
        for attr in self.attributes:
            if code[-1].endswith(")"):
                code[-1] = code[-1] + ".attr(" + attr + ")"
            else:
                code[-1] = code[-1] + ".attr(" + attr + ")"
                
        # Add traits
        for trait in self.traits:
            if code[-1].endswith(")"):
                code[-1] = code[-1] + "." + trait + "()"
            else:
                code[-1] = code[-1] + "." + trait + "()"
                
        # Add the final comma and indent properly
        code[0] = "  " + code[0]
        for i in range(1, len(code)-1):
            code[i] = "  " + code[i]
        
        if len(code) == 1:
            code[0] = code[0] + ","
        else:
            for i in range(len(code)-1):
                code[i] = code[i] + ""
            code[-1] = code[-1] + ","
            
        return "\n".join(code)
        
    def run(self):
        self.print_welcome()
        self.get_move_type()
        self.get_move_id()
        self.get_pokemon_type()
        self.get_category()
        self.get_power()
        self.get_accuracy()
        self.get_pp()
        self.get_chance()
        self.get_priority()
        self.get_generation()
        self.get_target()
        self.get_attributes()
        self.get_traits()
        
        print("\n" + "="*60)
        print(" Generated TypeScript Code")
        print("="*60)
        
        code = self.generate_code()
        print(code)
        
        print("\nThis code can be pasted into the allMoves.push() array in move.ts")
        
        # Ask if user wants to save to file
        print("\nDo you want to save this to a file? (y/n):")
        if input("> ").lower().startswith("y"):
            filename = input("Enter filename (default: move_snippet.ts): ") or "move_snippet.ts"
            try:
                with open(filename, "w") as f:
                    f.write(code)
                print(f"Saved to {filename}")
            except Exception as e:
                print(f"Error saving file: {e}")
        
        # Ask if user wants to create another move
        print("\nDo you want to create another move? (y/n):")
        return input("> ").lower().startswith("y")

if __name__ == "__main__":
    maker = MoveMaker()
    
    while True:
        create_another = maker.run()
        if not create_another:
            print("\nThank you for using PokéRogue Move Maker!")
            break
        maker.clear_state()