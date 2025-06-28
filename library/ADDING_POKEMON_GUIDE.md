# Adding a New Pokémon to PokeRogue

This guide covers the complete process of adding a new Pokémon to PokeRogue.

## Overview

Adding a Pokémon involves several components:
- Species definition (stats, types, abilities)
- Sprite assets (icons, battle sprites, back sprites, shiny versions for each)
- Move sets and battle data
- Starter integration
- UI atlas regeneration

## Prerequisites

- Node.js and npm installed
- TexturePacker installed (for regenerating sprite atlases)
- Basic understanding of TypeScript
- Sprite assets prepared (40x30 icons, battle sprites, back sprites, shiny versions for each)

## Step 1: Choose Species ID

Choose an ID that doesn't conflict with existing Pokémon:
- Regular Pokémon: 1-1025
- IDs above 2000 are separated into blocks for regional forms.
- To add a new Pokemon, you can place it directly after the Pecharunt in the enum and when you define the species data. This will place your pokemon at number 1026.

## Step 2: Add Species Enum Entry

Edit `src/enums/species.ts`:

```typescript
export enum Species {
  // ... existing entries
  PECHARUNT,
  YOUR_POKEMON, // Replace with your chosen ID
}
```

## Step 3: Define Species Data

Add your Pokémon to `src/data/pokemon-species.ts` in the `initSpecies()` function:

```typescript
new PokemonSpecies(
  Species.YOUR_POKEMON,
  9, // Generation (1-9)
  false, // isSubLegendary
  false, // isLegendary
  false, // isMythical
  "Your Category", // Species category
  PokemonType.TYPE1, // Primary type
  PokemonType.TYPE2, // Secondary type (or null for single type)
  1.6, // Height in meters
  70, // Weight in kg
  Abilities.ABILITY1, // Primary ability
  Abilities.ABILITY2, // Secondary ability
  Abilities.HIDDEN_ABILITY, // Hidden ability
  490, // Base stat total
  65, // HP
  125, // Attack
  100, // Defense
  60, // Special Attack
  70, // Special Defense
  70, // Speed
  45, // Catch rate
  35, // Friendship
  172, // Experience yield
  GrowthRate.MEDIUM_FAST, // Growth rate
  50, // Gender ratio (50 = 50% male, null = genderless)
  false, // Can change form
),
```

## Step 4: Add Starter Cost

Edit `src/data/balance/starters.ts`:

```typescript
export const speciesStarterCosts: Partial<Record<Species, number>> = {
  // ... existing entries
  [Species.YOUR_POKEMON]: 1, // Cost in starter points (1-10)
};
```

## Step 5: Configure Level Moves

Edit `src/data/balance/pokemon-level-moves.ts`:

```typescript
export const pokemonSpeciesLevelMoves: PokemonSpeciesLevelMoves = {
  // ... existing entries
  [Species.YOUR_POKEMON]: [
    [1, Moves.TACKLE],
    [1, Moves.LEER],
    [8, Moves.BITE],
    [12, Moves.ROAR],
    // ... add more moves
  ],
};
```

## Step 6: Configure Egg Moves (Optional)

Edit `src/data/balance/egg-moves.ts`:

```typescript
export const speciesEggMoves: Partial<Record<Species, Moves[]>> = {
  // ... existing entries
  [Species.YOUR_POKEMON]: [
    Moves.MOVE1,
    Moves.MOVE2,
    // ... add egg moves
  ],
};
```

## Step 7: Set Egg Tier

Edit `src/data/balance/species-egg-tiers.ts`:

```typescript
export const speciesEggTiers: Partial<Record<Species, EggTier>> = {
  // ... existing entries
  [Species.YOUR_POKEMON]: EggTier.RARE, // COMMON, RARE, EPIC, LEGENDARY
};
```

## Step 8: Configure Passive Abilities (Optional)

Edit `src/data/balance/passives.ts`:

```typescript
export const starterPassiveAbilities: Partial<Record<Species, Partial<Record<number, Abilities>>>> = {
  // ... existing entries
  [Species.YOUR_POKEMON]: { 0: Abilities.YOUR_PASSIVE },
};
```

## Step 9: Add to Default Starters (Optional)

Edit `src/system/game-data.ts`:

```typescript
export const defaultStarterSpecies: Species[] = [
  // ... existing starters
  Species.YOUR_POKEMON,
];
```

## Step 10: Prepare Sprite Assets

Create the following sprite files:

### Icons (40x30 pixels)
- `public/images/pokemon/icons/[generation]/[ID].png` - Regular icon
- `public/images/pokemon/icons/[generation]/[ID]s.png` - Shiny icon

### Battle Sprites
- `public/images/pokemon/[ID].png` - Front battle sprite
- `public/images/pokemon/back/[ID].png` - Back battle sprite
- `public/images/pokemon/back/shiny/[ID].png` - Shiny back sprite

Example for ID 1026 in Generation 9:
```
public/images/pokemon/icons/9/1026.png
public/images/pokemon/icons/9/1026s.png
public/images/pokemon/1026.png
public/images/pokemon/back/1026.png
public/images/pokemon/back/shiny/1026.png
```

## Step 11: Regenerate Icon Atlas

**Critical Step**: After adding icon sprites, regenerate the atlas:

```bash
# Navigate to the generation's icon directory
cd public/images/pokemon/icons/[generation]/

# Run TexturePacker (Linux/Mac)
cd pokerogue/public/images/pokemon/icons/9/
TexturePacker ./ ../configuration.tps --sheet ../../../pokemon_icons_9.png --data ../../../pokemon_icons_9.json --replace .png=


# Windows
icons.bat
```

This updates:
- `pokemon_icons_[generation].png` - The sprite sheet
- `pokemon_icons_[generation].json` - The coordinate data

## Step 12: Add Cry
You must add the cry audio file for the Pokemon. You don't have to make a new cry, you can can copy an existing one in public/audio/cry and rename it to match the new pokemons number. For example, if your new Pokemon is #1500 per its enum, you would name this file 1500.m4a.

If you don't add the cry, you will be able to play with the pokemon but the game will stall if the pokemon faints because the cry is required for the pokemon to faint.

## Step 13: Add Pokemon to Biomes
Even if you don't want the pokemon to be found in any biomes, you must still add it to the catchable pokemon array in 'src/data/balance/biomes.ts' Ctrl+F for:

```typescript
export function initBiomes() {
  const pokemonBiomes = [
```

And add your pokemon accordingly. Here is an example of Pecharunt as an example of a pokemon that does not appear in any biomes as well as an example of a custom pokemon below that appears in a few biomes:

```typescript
    [Species.PECHARUNT, PokemonType.POISON, PokemonType.GHOST, []],
    [Species.KOYA, PokemonType.PSYCHIC, PokemonType.NORMAL, []],
    [
      Species.ARTORIAS,
      PokemonType.STEEL,
      PokemonType.DARK,
      [
        [Biome.BADLANDS, BiomePoolTier.SUPER_RARE, [TimeOfDay.NIGHT]],
        [Biome.CAVE, BiomePoolTier.RARE],
        [Biome.DESERT, BiomePoolTier.SUPER_RARE],
        [Biome.GRAVEYARD, BiomePoolTier.RARE, [TimeOfDay.NIGHT]],
        [Biome.RUINS, BiomePoolTier.RARE],
        [Biome.WASTELAND, BiomePoolTier.RARE],
      ],
    ],
```

## Step 1x: Build and Test

```bash
# Start development server
npm run start:dev
```

## Step 1x: Test Integration

1. **Clear browser cache** (Ctrl+F5)
2. **Check starter selection** - Pokémon should appear with correct icon
3. **Verify typing display** - Should show correct types
4. **Test in battle** - Sprites and moves should work
5. **Check moveset** - Ensure moves are appropriate for the typing

## File Checklist

Before submitting, verify these files are modified:

- [ ] `src/enums/species.ts` - Species enum entry
- [ ] `src/data/pokemon-species.ts` - Species definition
- [ ] `src/data/balance/starters.ts` - Starter cost
- [ ] `src/data/balance/pokemon-level-moves.ts` - Level moves
- [ ] `src/data/balance/egg-moves.ts` - Egg moves (optional)
- [ ] `src/data/balance/species-egg-tiers.ts` - Egg tier
- [ ] `src/data/balance/passives.ts` - Passive abilities (optional)
- [ ] `src/system/game-data.ts` - Default starters (optional)
- [ ] All sprite assets created
- [ ] Atlas files regenerated

## Testing Checklist

- [ ] Pokémon appears in starter selection
- [ ] Correct icon displays (regular and shiny)
- [ ] Correct typing shows in UI
- [ ] Moves are appropriate for typing
- [ ] Battle sprites work correctly
- [ ] Back sprites work correctly
- [ ] No console errors
- [ ] Game doesn't crash

## Support

If you encounter issues:
1. Check browser console for errors
2. Verify all files are properly formatted
3. Ensure TexturePacker regenerated atlases correctly
4. Clear all browser data and test again

If you have any issues feel free to ping me. I'd like to thank the kind folks in the PokeRgoue Discord server for helping me with this.
