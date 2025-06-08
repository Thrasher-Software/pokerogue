# PokéRogue Move Maker

A utility script to help generate TypeScript code for new moves in PokéRogue.

## Features

- Interactive command-line interface
- Support for creating AttackMove, StatusMove, and SelfStatusMove types
- Add move attributes (like StatusEffectAttr, MultiHitAttr, etc.)
- Add move traits (like punchingMove, soundBased, etc.)
- Generate formatted TypeScript code ready to paste into move.ts

## Setup

1. Make sure you have Python 3.6+ installed
2. Create and activate a virtual environment:

```bash
# From the pokerogue directory
cd movemaker
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Usage

1. With the virtual environment activated, run the script:

```bash
# From the movemaker directory
python movemaker.py

# Or from the pokerogue directory
python movemaker/movemaker.py

# Or if you've made it executable
./movemaker/movemaker.py
```

2. Follow the interactive prompts to define your move
3. Copy the generated code and paste it into the `allMoves.push()` array in `src/data/moves/move.ts`

## Example

Here's an example of creating a simple Fire-type attack move with a chance to burn:

1. Select move type: `AttackMove`
2. Enter move ID: `FLAME_BURST`
3. Select type: `FIRE`
4. Select category: `SPECIAL`
5. Enter power: `70`
6. Enter accuracy: `100`
7. Enter PP: `15`
8. Enter effect chance: `10`
9. Enter priority: `0`
10. Enter generation: `5`
11. Add attribute: `StatusEffectAttr` with parameter `StatusEffect.BURN`
12. Add trait: `makesContact(false)`

This will generate code similar to:

```typescript
  new AttackMove(
    Moves.FLAME_BURST,
    PokemonType.FIRE,
    MoveCategory.SPECIAL,
    70,
    100,
    15,
    10,
    0,
    5,
  ).attr(StatusEffectAttr, StatusEffect.BURN).makesContact(false),
```

## Tips

- The `-1` value for accuracy means the move never misses
- For effect chance, `-1` means the effect is guaranteed
- You can specify multiple attributes and traits for a single move
- For status moves, the power parameter will automatically be set to `-1`
