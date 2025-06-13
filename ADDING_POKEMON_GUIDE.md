# Adding a New Pokémon to PokeRogue

This guide covers the complete process of adding a new Pokémon to PokeRogue, based on the experience of adding Artorias (ID: 8902).

## Overview

Adding a Pokémon involves several components:
- Species definition (stats, types, abilities)
- Sprite assets (icons, battle sprites, back sprites)
- Move sets and battle data
- Starter integration
- UI atlas regeneration

## Prerequisites

- Node.js and npm installed
- TexturePacker installed (for regenerating sprite atlases)
- Basic understanding of TypeScript
- Sprite assets prepared (40x30 icons, battle sprites, back sprites)

## Step 1: Choose Species ID

Choose an ID that doesn't conflict with existing Pokémon:
- Regular Pokémon: 1-1025
- Custom/Fan Pokémon: 8000+ range recommended
- Check existing IDs in `src/enums/species.ts`

## Step 2: Add Species Enum Entry

Edit `src/enums/species.ts`:

```typescript
export enum Species {
  // ... existing entries
  YOUR_POKEMON = 8902, // Replace with your chosen ID
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

**Important**: Ensure moves match your Pokémon's typing and theme.

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

Example for ID 8902 in Generation 9:
```
public/images/pokemon/icons/9/8902.png
public/images/pokemon/icons/9/8902s.png
public/images/pokemon/8902.png
public/images/pokemon/back/8902.png
public/images/pokemon/back/shiny/8902.png
```

## Step 11: Regenerate Icon Atlas

**Critical Step**: After adding icon sprites, regenerate the atlas:

```bash
# Navigate to the generation's icon directory
cd public/images/pokemon/icons/[generation]/

# Run TexturePacker (Linux/Mac)
TexturePacker ./  ../configuration.tps --sheet ../../../pokemon_icons_[generation].png --data ../../../pokemon_icons_[generation].json --replace .png=

# Windows
icons.bat
```

This updates:
- `pokemon_icons_[generation].png` - The sprite sheet
- `pokemon_icons_[generation].json` - The coordinate data

## Step 12: Build and Test

```bash
# Clean build
rm -rf dist/
npm run build

# Start development server
npm run start
```

## Step 13: Test Integration

1. **Clear browser cache** (Ctrl+F5)
2. **Check starter selection** - Pokémon should appear with correct icon
3. **Verify typing display** - Should show correct types
4. **Test in battle** - Sprites and moves should work
5. **Check moveset** - Ensure moves are appropriate for the typing

## Common Issues and Solutions

### Issue: Wrong typing displayed in starter selection
**Cause**: Moveset doesn't match Pokémon typing
**Solution**: Ensure level moves match your Pokémon's types in `pokemon-level-moves.ts`

### Issue: Sprite not showing/wrong sprite
**Cause**: Atlas not regenerated or wrong coordinates
**Solution**: Re-run TexturePacker to regenerate atlas files

### Issue: Game crashes on starter selection
**Cause**: Missing sprite assets or starter data
**Solution**: Verify all required files exist and clear browser localStorage

### Issue: "starterData undefined" error
**Cause**: Browser cache with old data
**Solution**: Clear all browser data and restart game

### Issue: No moves in battle
**Cause**: Empty or incorrectly formatted moveset
**Solution**: Check `pokemon-level-moves.ts` for proper move array format

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

## Advanced Configuration

### Custom Forms
For Pokémon with multiple forms, add form definitions in the species constructor.

### Evolution Chains
Add evolution data in `src/data/balance/pokemon-evolutions.ts`.

### Type Effectiveness
Custom type interactions can be added in the type effectiveness system.

### Custom Abilities
New abilities can be defined in the abilities system.

## Testing Checklist

- [ ] Pokémon appears in starter selection
- [ ] Correct icon displays (regular and shiny)
- [ ] Correct typing shows in UI
- [ ] Moves are appropriate for typing
- [ ] Battle sprites work correctly
- [ ] Back sprites work correctly
- [ ] No console errors
- [ ] Game doesn't crash

## Notes

- Always regenerate atlases after adding/changing icon sprites
- Clear browser cache when testing changes
- Keep species IDs consistent across all files
- Ensure moveset matches Pokémon typing for proper UI display
- Test thoroughly before considering complete

## Support

If you encounter issues:
1. Check browser console for errors
2. Verify all files are properly formatted
3. Ensure TexturePacker regenerated atlases correctly
4. Clear all browser data and test again