# TexturePacker CLI Guide for PokeRogue

This guide provides comprehensive instructions for regenerating sprite atlases in PokeRogue using TexturePacker's command-line interface.

## Quick Start: Interactive Shell Script

For the easiest experience, use the interactive shell script located at `public/tools/update_spritesheets.sh`:

```bash
# Navigate to the PokeRogue root directory
cd /path/to/pokerogue

# Run the interactive script
./public/tools/update_spritesheets.sh
```

The script provides:
- **Interactive menu system** - Select spritesheets to update via numbered options
- **Automatic error checking** - Verifies TexturePacker installation and directory structure
- **Progress feedback** - Color-coded output showing success/failure status
- **Comprehensive coverage** - All Pokemon generations, items, types, statuses, and localizations
- **Batch operations** - Update all spritesheets at once or by category

### Script Features:
- Update individual Pokemon generations (0-9) or all at once
- Update Pokemon variant icons
- Update items, types, and status effect spritesheets
- Support for all localized versions (15+ languages)
- Built-in validation and error handling
- No need to remember complex command syntax

**Note**: If you prefer manual commands or need to understand the underlying TexturePacker syntax, continue reading the detailed command reference below.

## Overview

PokeRogue uses TexturePacker to combine individual sprite images into optimized sprite sheets (atlases) with accompanying JSON coordinate data. This is essential for performance and efficient loading of sprites in the game.

## Prerequisites

1. **TexturePacker Installation**: Download and install TexturePacker from [https://www.codeandweb.com/texturepacker](https://www.codeandweb.com/texturepacker)
2. **Command Line Access**: Ensure TexturePacker is available in your system PATH
3. **Project Structure**: Understand the PokeRogue directory structure
4. **TexturePacker License**: This isn't strictly required but PokeRogue uses advanced features and sprites won't render correctly without a license. Obtain a license from [https://www.codeandweb.com/texturepacker](https://www.codeandweb.com/texturepacker)

## Command Structure Explanation

### Basic TexturePacker Syntax
```bash
TexturePacker [input_directory] [config_file] --sheet [output_image] --data [output_json] [options]
```

### Parameter Breakdown

- **Input Directory**: Directory containing individual sprite PNG files
- **Config File**: `.tps` file with packing settings (dimensions, format, etc.)
- `--sheet`: Output sprite sheet image file
- `--data`: Output JSON file with sprite coordinates
- `--replace .png=`: Removes `.png` extension from sprite names in JSON

### Example Command Analysis
```bash
cd pokerogue/public/images/pokemon/icons/9/
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_9.png --data ../../../pokemon_icons_9.json --replace .png=
```

**Step by step:**
1. Navigate to Generation 9 icons directory
2. Use current directory (`./`) as input (contains individual icon PNGs)
3. Use configuration file one level up (`../configuration.tps`)
4. Output sprite sheet 3 levels up (`../../../pokemon_icons_9.png`)
5. Output JSON data 3 levels up (`../../../pokemon_icons_9.json`)
6. Strip `.png` extensions from sprite names

## Manual Command Reference

The following sections provide the complete manual TexturePacker commands. These are automatically handled by the interactive script above, but are documented here for reference and custom usage.

### Pokémon Icon Atlases

#### Generation 0 (Regional Variants)
```bash
cd pokerogue/public/images/pokemon/icons/0/
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_0.png --data ../../../pokemon_icons_0.json --replace .png=
```

#### Generation 1
```bash
cd pokerogue/public/images/pokemon/icons/1/
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_1.png --data ../../../pokemon_icons_1.json --replace .png=
```

#### Generation 2
```bash
cd pokerogue/public/images/pokemon/icons/2/
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_2.png --data ../../../pokemon_icons_2.json --replace .png=
```

#### Generation 3
```bash
cd pokerogue/public/images/pokemon/icons/3/
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_3.png --data ../../../pokemon_icons_3.json --replace .png=
```

#### Generation 4
```bash
cd pokerogue/public/images/pokemon/icons/4/
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_4.png --data ../../../pokemon_icons_4.json --replace .png=
```

#### Generation 5
```bash
cd pokerogue/public/images/pokemon/icons/5/
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_5.png --data ../../../pokemon_icons_5.json --replace .png=
```

#### Generation 6
```bash
cd pokerogue/public/images/pokemon/icons/6/
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_6.png --data ../../../pokemon_icons_6.json --replace .png=
```

#### Generation 7
```bash
cd pokerogue/public/images/pokemon/icons/7/
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_7.png --data ../../../pokemon_icons_7.json --replace .png=
```

#### Generation 8
```bash
cd pokerogue/public/images/pokemon/icons/8/
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_8.png --data ../../../pokemon_icons_8.json --replace .png=
```

#### Generation 9
```bash
cd pokerogue/public/images/pokemon/icons/9/
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_9.png --data ../../../pokemon_icons_9.json --replace .png=
```

### Items Atlas
```bash
cd pokerogue/public/images/items/
TexturePacker ./ configuration.tps --sheet ../items.png --data ../items.json --replace .png=
```

### Type Badges Atlases

#### English (Default)
```bash
cd pokerogue/public/images/
# Note: Assumes types directory and configuration exist
TexturePacker ./types/ types_configuration.tps --sheet types.png --data types.json --replace .png=
```

#### Localized Type Badges
```bash
# German
TexturePacker ./types_de/ types_configuration.tps --sheet types_de.png --data types_de.json --replace .png=

# French  
TexturePacker ./types_fr/ types_configuration.tps --sheet types_fr.png --data types_fr.json --replace .png=

# Spanish (Spain)
TexturePacker ./types_es-ES/ types_configuration.tps --sheet types_es-ES.png --data types_es-ES.json --replace .png=

# Spanish (Mexico)
TexturePacker ./types_es-MX/ types_configuration.tps --sheet types_es-MX.png --data types_es-MX.json --replace .png=

# Italian
TexturePacker ./types_it/ types_configuration.tps --sheet types_it.png --data types_it.json --replace .png=

# Portuguese (Brazil)
TexturePacker ./types_pt-BR/ types_configuration.tps --sheet types_pt-BR.png --data types_pt-BR.json --replace .png=

# Japanese
TexturePacker ./types_ja/ types_configuration.tps --sheet types_ja.png --data types_ja.json --replace .png=

# Korean
TexturePacker ./types_ko/ types_configuration.tps --sheet types_ko.png --data types_ko.json --replace .png=

# Chinese (Simplified)
TexturePacker ./types_zh-CN/ types_configuration.tps --sheet types_zh-CN.png --data types_zh-CN.json --replace .png=

# Chinese (Traditional)
TexturePacker ./types_zh-TW/ types_configuration.tps --sheet types_zh-TW.png --data types_zh-TW.json --replace .png=

# Russian
TexturePacker ./types_ru/ types_configuration.tps --sheet types_ru.png --data types_ru.json --replace .png=

# Turkish
TexturePacker ./types_tr/ types_configuration.tps --sheet types_tr.png --data types_tr.json --replace .png=

# Romanian
TexturePacker ./types_ro/ types_configuration.tps --sheet types_ro.png --data types_ro.json --replace .png=

# Catalan
TexturePacker ./types_ca/ types_configuration.tps --sheet types_ca.png --data types_ca.json --replace .png=

# Danish
TexturePacker ./types_da/ types_configuration.tps --sheet types_da.png --data types_da.json --replace .png=
```

### Status Effects Atlases

#### English (Default)
```bash
cd pokerogue/public/images/
TexturePacker ./statuses/ statuses_configuration.tps --sheet statuses.png --data statuses.json --replace .png=
```

#### Localized Status Effects
```bash
# German
TexturePacker ./statuses_de/ statuses_configuration.tps --sheet statuses_de.png --data statuses_de.json --replace .png=

# French
TexturePacker ./statuses_fr/ statuses_configuration.tps --sheet statuses_fr.png --data statuses_fr.json --replace .png=

# Spanish (Spain)
TexturePacker ./statuses_es-ES/ statuses_configuration.tps --sheet statuses_es-ES.png --data statuses_es-ES.json --replace .png=

# Spanish (Mexico)
TexturePacker ./statuses_es-MX/ statuses_configuration.tps --sheet statuses_es-MX.png --data statuses_es-MX.json --replace .png=

# Italian
TexturePacker ./statuses_it/ statuses_configuration.tps --sheet statuses_it.png --data statuses_it.json --replace .png=

# Portuguese (Brazil)
TexturePacker ./statuses_pt-BR/ statuses_configuration.tps --sheet statuses_pt-BR.png --data statuses_pt-BR.json --replace .png=

# Japanese
TexturePacker ./statuses_ja/ statuses_configuration.tps --sheet statuses_ja.png --data statuses_ja.json --replace .png=

# Korean
TexturePacker ./statuses_ko/ statuses_configuration.tps --sheet statuses_ko.png --data statuses_ko.json --replace .png=

# Chinese (Simplified)
TexturePacker ./statuses_zh-CN/ statuses_configuration.tps --sheet statuses_zh-CN.png --data statuses_zh-CN.json --replace .png=

# Chinese (Traditional)
TexturePacker ./statuses_zh-TW/ statuses_configuration.tps --sheet statuses_zh-TW.png --data statuses_zh-TW.json --replace .png=

# Russian
TexturePacker ./statuses_ru/ statuses_configuration.tps --sheet statuses_ru.png --data statuses_ru.json --replace .png=

# Turkish
TexturePacker ./statuses_tr/ statuses_configuration.tps --sheet statuses_tr.png --data statuses_tr.json --replace .png=

# Romanian
TexturePacker ./statuses_ro/ statuses_configuration.tps --sheet statuses_ro.png --data statuses_ro.json --replace .png=

# Catalan
TexturePacker ./statuses_ca/ statuses_configuration.tps --sheet statuses_ca.png --data statuses_ca.json --replace .png=

# Danish
TexturePacker ./statuses_da/ statuses_configuration.tps --sheet statuses_da.png --data statuses_da.json --replace .png=
```

### Other Atlases

#### Categories Atlas
```bash
cd pokerogue/public/images/
TexturePacker ./categories/ categories_configuration.tps --sheet categories.png --data categories.json --replace .png=
```

#### Pokéball Atlas
```bash
cd pokerogue/public/images/
TexturePacker ./pb/ pb_configuration.tps --sheet pb.png --data pb.json --replace .png=
```

## Batch Commands

### Regenerate All Pokémon Icon Atlases
```bash
#!/bin/bash
# Save as regenerate_pokemon_icons.sh

cd pokerogue/public/images/pokemon/icons/

# Generation 0
cd 0/
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_0.png --data ../../../pokemon_icons_0.json --replace .png=
cd ..

# Generation 1
cd 1/
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_1.png --data ../../../pokemon_icons_1.json --replace .png=
cd ..

# Generation 2
cd 2/
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_2.png --data ../../../pokemon_icons_2.json --replace .png=
cd ..

# Generation 3
cd 3/
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_3.png --data ../../../pokemon_icons_3.json --replace .png=
cd ..

# Generation 4
cd 4/
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_4.png --data ../../../pokemon_icons_4.json --replace .png=
cd ..

# Generation 5
cd 5/
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_5.png --data ../../../pokemon_icons_5.json --replace .png=
cd ..

# Generation 6
cd 6/
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_6.png --data ../../../pokemon_icons_6.json --replace .png=
cd ..

# Generation 7
cd 7/
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_7.png --data ../../../pokemon_icons_7.json --replace .png=
cd ..

# Generation 8
cd 8/
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_8.png --data ../../../pokemon_icons_8.json --replace .png=
cd ..

# Generation 9
cd 9/
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_9.png --data ../../../pokemon_icons_9.json --replace .png=
cd ..

echo "All Pokémon icon atlases regenerated!"
```

### Windows Batch Version
```Batch
@echo off
REM Save as regenerate_pokemon_icons.bat

cd /d "pokerogue\public\images\pokemon\icons\"

REM Generation 0
cd 0
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_0.png --data ../../../pokemon_icons_0.json --replace .png=
cd ..

REM Generation 1
cd 1
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_1.png --data ../../../pokemon_icons_1.json --replace .png=
cd ..

REM Generation 2
cd 2
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_2.png --data ../../../pokemon_icons_2.json --replace .png=
cd ..

REM Generation 3
cd 3
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_3.png --data ../../../pokemon_icons_3.json --replace .png=
cd ..

REM Generation 4
cd 4
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_4.png --data ../../../pokemon_icons_4.json --replace .png=
cd ..

REM Generation 5
cd 5
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_5.png --data ../../../pokemon_icons_5.json --replace .png=
cd ..

REM Generation 6
cd 6
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_6.png --data ../../../pokemon_icons_6.json --replace .png=
cd ..

REM Generation 7
cd 7
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_7.png --data ../../../pokemon_icons_7.json --replace .png=
cd ..

REM Generation 8
cd 8
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_8.png --data ../../../pokemon_icons_8.json --replace .png=
cd ..

REM Generation 9
cd 9
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_9.png --data ../../../pokemon_icons_9.json --replace .png=
cd ..

echo All Pokemon icon atlases regenerated!
pause
```

## Troubleshooting

### Common Issues

#### TexturePacker Not Found
```bash
# Error: 'TexturePacker' is not recognized as an internal or external command
```
**Solution**: Ensure TexturePacker is installed and added to your system PATH.

#### Configuration File Missing
```bash
# Error: Could not load settings file
```
**Solution**: Verify the `.tps` configuration file exists in the specified path.

#### Path Issues
```bash
# Error: No input files found
```
**Solution**: Check that you're in the correct directory and the input path contains PNG files.

#### Permission Errors
```bash
# Error: Could not write to output file
```
**Solution**: Ensure you have write permissions to the output directory.

### Verification Steps

After regenerating atlases:

1. **Check File Sizes**: Ensure output PNG and JSON files were created and have reasonable file sizes
2. **Validate JSON**: Open JSON files to verify they contain sprite coordinate data
3. **Test in Game**: Load the game and verify sprites display correctly
4. **Browser Cache**: Clear browser cache if testing locally (Ctrl+F5)

### Best Practices

1. **Backup First**: Always backup existing atlases before regenerating
2. **Test Incrementally**: Regenerate one atlas at a time when making changes
3. **Consistent Naming**: Ensure individual sprite files follow the expected naming convention
4. **Size Constraints**: Be aware of texture size limits (usually 512x1024 for icons)
5. **Version Control**: Commit atlas changes separately from code changes

## Configuration File Details

The `configuration.tps` file contains settings for:
- Maximum texture size (512x1024 for icons)
- Output format (PNG8 for compression)
- Packing algorithm (MaxRects for efficiency)
- Border padding and sprite trimming
- JSON output format (Phaser framework compatible)

## When to Regenerate Atlases

- **Adding new Pokémon**: Always regenerate the appropriate generation's icon atlas
- **Adding new items**: Regenerate the items atlas
- **Sprite updates**: When individual sprite files are modified
- **Localization**: When adding new language-specific sprites
- **Optimization**: Periodically to improve packing efficiency

## Integration with PokeRogue

The generated atlases are loaded by PokeRogue's sprite management system:
- PNG files provide the visual sprite data
- JSON files provide coordinate mapping for extracting individual sprites
- The `--replace .png=` parameter ensures sprite names match code references

Remember to test thoroughly after regenerating atlases to ensure all sprites load correctly in the game!

## Interactive Script Usage Guide

The interactive shell script at `public/tools/update_spritesheets.sh` provides a user-friendly interface for all TexturePacker operations. Here's how to use it effectively:

### Running the Script

```bash
# Make sure you're in the PokeRogue root directory
cd /path/to/pokerogue

# Run the script
./public/tools/update_spritesheets.sh
```

### Main Menu Options

1. **Update Pokemon Icons** - Access submenu for individual generations or batch updates
2. **Update Items** - Regenerate the items spritesheet
3. **Update Types (English)** - Update English type badges
4. **Update Statuses (English)** - Update English status effect icons
5. **Update Localized Spritesheets** - Access language-specific sprite updates
6. **Update All English Spritesheets** - Batch update all non-localized spritesheets

### Pokemon Icons Submenu

- Individual generations (0-9) for targeted updates
- "All Generations" for complete Pokemon icon refresh
- "All Variants" for variant-specific icons
- Generation 0 includes regional variants

### Localization Submenu

Supports all 15 languages with separate Types and Statuses options:
- German (de), French (fr), Spanish Spain (es-ES), Spanish Mexico (es-MX)
- Italian (it), Portuguese Brazil (pt-BR), Japanese (ja), Korean (ko)
- Chinese Simplified (zh-CN), Chinese Traditional (zh-TW)
- Russian (ru), Turkish (tr), Romanian (ro), Catalan (ca), Danish (da)

### Script Features

- **Automatic Validation**: Checks TexturePacker installation and directory structure
- **Error Handling**: Graceful failure with informative messages
- **Progress Feedback**: Color-coded output (green=success, red=error, blue=processing)
- **File Verification**: Ensures PNG files exist before processing
- **Safe Navigation**: Automatically returns to previous directory after operations

### Common Workflows

**Adding new Pokemon to Generation 8:**
1. Add PNG files to `public/images/pokemon/icons/8/`
2. Run script → Pokemon Icons → Generation 8
3. Verify output files were updated

**Updating all spritesheets after major changes:**
1. Run script → Update All English Spritesheets
2. Run script → Update Localized Spritesheets → (select each language as needed)

**Troubleshooting with the script:**
- Script will show specific error messages if TexturePacker isn't found
- Warnings appear if no PNG files are found in expected directories
- All operations are logged with clear success/failure indicators

The interactive script eliminates the need to remember complex command syntax while providing the same functionality as manual TexturePacker commands.