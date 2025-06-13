# Debugging Artorias Type Display Issue

This document outlines the debugging steps and findings for the Artorias (Species ID: 8902) type display issue in the starter selection UI.

## Issue Summary

**Problem**: When selecting Artorias in the starter selection screen, the UI shows incorrect typing (Grass/Flying like Rowlet) instead of the correct Steel/Dark typing.

**Confirmed Facts**:
- Artorias is correctly defined as Steel/Dark in pokemon-species.ts
- Battle system recognizes correct typing
- Another developer confirmed the UI is always using data from the last highlighted pokemon
- Icon displays correctly after atlas regeneration
- Moves don't appear in battle, but typing renders correctly there

## Debugging Steps Taken

### 1. Species Definition Verification
- ✅ Artorias (Species.ARTORIAS = 8902) correctly defined as Steel/Dark
- ✅ Species enum properly includes ARTORIAS = 8902
- ✅ Species is marked as obtainable and has starter costs

### 2. UI State Management Analysis
- 🔍 Identified potential race condition in `setSpecies` method
- 🔍 Found multiple references to `this.lastSpecies` instead of current species parameter
- 🔍 Fixed `switchMoveHandler` to use correct species parameter
- 🔍 Fixed `setSpeciesDetails` to use passed species instead of `this.lastSpecies`

### 3. Key Findings

#### Race Condition in UI Updates
The main issue appears to be related to timing of UI updates:

1. `setCursor()` calls `setSpecies(species)`
2. `setSpecies()` calls `setSpeciesDetails()`
3. `this.lastSpecies = species` is set near the end of `setSpecies()`
4. Some UI elements use `this.lastSpecies` instead of the current species

#### Fixed Code Locations
1. **switchMoveHandler** (line 3496): Changed from `this.lastSpecies` to `species`
2. **setSpeciesDetails** ability handling: Changed from `this.lastSpecies` to `species` parameter
3. **Candy tooltip**: Changed from `this.lastSpecies` to `species` parameter

## Potential Root Causes

### Theory 1: Array Indexing Issue
The starter selection UI might be using incorrect array indexing when mapping cursor position to species data.

### Theory 2: Container Synchronization
The `filteredStarterContainers` array might be out of sync with the species data, causing the wrong species to be selected.

### Theory 3: Async Update Timing
UI updates might be happening asynchronously, causing stale data to be displayed.

## Testing Recommendations

### 1. Add Debug Logging
Add temporary console.log statements in key methods:

```javascript
// In setCursor method
console.log(`setCursor: cursor=${cursor}, species=${species?.name}, id=${species?.speciesId}`);

// In setSpecies method  
console.log(`setSpecies: ${species?.name} (${species?.speciesId})`);

// In setTypeIcons method
console.log(`setTypeIcons: type1=${type1 ? PokemonType[type1] : 'null'}, type2=${type2 ? PokemonType[type2] : 'null'}`);
```

### 2. Verify Array Integrity
Check that `filteredStarterContainers[cursor].species` matches the expected species:

```javascript
// In setCursor method
const expectedSpecies = this.filteredStarterContainers[cursor]?.species;
console.log(`Expected: ${expectedSpecies?.name}, Got: ${species?.name}`);
```

### 3. Test Cursor Position Mapping
Verify the cursor position correctly maps to Artorias:

```javascript
// When cursor is on Artorias
console.log(`Cursor: ${this.cursor}, FilteredContainer: ${this.filteredStarterContainers[this.cursor]?.species?.name}`);
```

## Next Steps

1. **Implement debug logging** to trace exact data flow
2. **Test cursor movement** specifically to/from Artorias
3. **Verify container array integrity** during filtering and sorting
4. **Check for any Artorias-specific edge cases** in the filtering logic
5. **Test with different sort orders** to see if issue persists

## Files Modified

- `pokerogue/src/ui/starter-select-ui-handler.ts` - Fixed species parameter usage in multiple locations

## Files to Investigate Further

- `pokerogue/src/ui/starter-container.ts` - Container implementation
- `pokerogue/src/ui/filter-bar.ts` - Filtering logic that creates filteredStarterContainers
- `pokerogue/src/data/balance/starters.ts` - Starter costs and validation

## Expected Outcome

After implementing the fixes and debug logging, the type display should correctly show Steel/Dark for Artorias in the starter selection UI, matching the battle system behavior.