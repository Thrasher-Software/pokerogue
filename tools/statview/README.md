# PokeRogue Species Stat Viewer

A Python command-line tool for viewing Pokemon species statistics from the PokeRogue TypeScript data files.

## Features

- **Interactive CLI**: Search and browse Pokemon data with a simple command-line interface
- **Colored Output**: Beautiful terminal formatting with type-specific colors
- **Comprehensive Stats**: View all base stats, abilities, types, and other species information
- **Search Functionality**: Search by Pokemon name or Pokedex ID
- **Range Listing**: List Pokemon in specific ID ranges
- **Real-time Parsing**: Directly parses the TypeScript source files for up-to-date data

## Installation

No external dependencies required! This script uses only Python's standard library.

```bash
# Make sure you have Python 3.6+ installed
python3 --version

# Navigate to the statview directory
cd pokerogue/tools/statview

# Make the script executable (optional)
chmod +x main.py
```

## Usage

### Basic Usage

```bash
# Run the interactive viewer
python3 main.py

# Or if you made it executable
./main.py
```

### Commands

Once in the interactive mode, you can use these commands:

- **Search by name**: `bulbasaur`, `pikachu`, `charizard`
- **Search by ID**: `1`, `25`, `150`
- **List ranges**: `list 1-10`, `list 150-160`
- **List first 20**: `list`
- **Quit**: `quit`, `exit`, or `q`

### Example Session

```
PokeRogue Species Stat Viewer
Loading Pokemon data...
Loaded 1025 Pokemon species
Usage: Enter Pokemon name or ID, 'list <start>-<end>', or 'quit'

> bulbasaur

#001 Bulbasaur
Seed Pokémon | Gen 1
Type: GRASS / POISON
Height: 0.7m | Weight: 6.9kg
Abilities: Overgrow | Hidden: Chlorophyll

Base Stats (Total: 318)
      HP:  45 ██████████████████░░░░░░░░░░░░
  Attack:  49 ██████████████████████░░░░░░░░░
 Defense:  49 ██████████████████████░░░░░░░░░
 Sp. Atk:  65 ██████████████████████████████
 Sp. Def:  65 ██████████████████████████████
   Speed:  45 ██████████████████░░░░░░░░░░░░

Catch Rate: 45 | Base Friendship: 50
Base EXP: 64 | Growth Rate: Medium Slow
Gender Ratio: 87.5% ♂ / 12.5% ♀

> list 1-5

#001 Bulbasaur
#002 Ivysaur
#003 Venusaur
#004 Charmander
#005 Charmeleon

> quit
```

## Features in Detail

### Color Coding

- **Types**: Each Pokemon type is displayed in a distinct color (Fire = Red, Water = Blue, etc.)
- **Rarities**: Legendary, Mythical, and Sub-Legendary Pokemon are highlighted
- **Stats**: Base stats are shown with colored bars for easy comparison

### Stat Display

The tool shows comprehensive Pokemon information including:

- **Basic Info**: Name, ID, generation, species category
- **Types**: Primary and secondary types with color coding
- **Physical**: Height and weight
- **Abilities**: All abilities including hidden abilities
- **Base Stats**: All 6 base stats with visual bars
- **Battle Info**: Catch rate, base friendship, base experience
- **Breeding**: Growth rate and gender ratios

### Search Capabilities

- **Fuzzy Name Search**: Partial name matching (e.g., "char" finds Charmander, Charmeleon, Charizard)
- **ID Search**: Direct lookup by Pokedex number
- **Multiple Results**: Shows list when multiple matches found
- **Range Listing**: Browse Pokemon in numerical ranges

## File Structure

```
pokerogue/tools/statview/
├── main.py           # Main script
├── requirements.txt  # Python dependencies (none required)
└── README.md        # This file
```

## Technical Details

The script parses the TypeScript source files directly:

- `src/data/pokemon-species.ts` - Main Pokemon data
- `src/enums/species.ts` - Species ID mappings
- `src/enums/abilities.ts` - Ability mappings
- `src/enums/pokemon-type.ts` - Type mappings

It uses regex parsing to extract Pokemon data from the TypeScript constructors and enum definitions, then formats the output for terminal display.

## Troubleshooting

### Common Issues

1. **File Not Found**: Make sure you're running from the correct directory and the TypeScript files exist
2. **No Color Output**: Some terminals don't support ANSI colors - the script will still work but without colors
3. **Python Version**: Requires Python 3.6+ for f-string support

### Performance

The script loads all Pokemon data into memory on startup, which takes a few seconds but enables fast searching afterwards.

## Contributing

Feel free to enhance the script with additional features:

- Export to JSON/CSV
- Compare Pokemon stats
- Filter by generation, type, or other criteria
- Enhanced search with regex support
- Integration with move data

## License

This tool is part of the PokeRogue project and follows the same license terms.