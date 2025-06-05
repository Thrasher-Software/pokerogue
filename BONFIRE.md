By the way, you run this with:

'''
npm run start:dev
'''


So it's the end of may 2025.
A few changes I'm considering:

- Access Egg Gacha from Main Menu
- Maybe a new trainer?
- Maybe a new event?

Egg Gacha

UI: src/ui/egg-gacha-ui-handler.ts

Egg List: src/data/egg.ts

06/03/2025

I've been talking with AJ some and we're thinking about a new event.
Maybe something where you come across Big Hat Logan or Crucible Knight Ordovis?
Logan could give you a new move inspired by Dark Souls or something, Ordovis would do something similar to that.
Maybe you could fight them?

I grepped for Hyper Beam and found the below, maybe we could use it for a new move:

jake-eaker:~/pokerogue$ grep -r "HYPER_BEAM"
src/data/balance/pokemon-level-moves.ts:    [ 64, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 52, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 55, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 60, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 74, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 80, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 44, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 54, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 60, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 42, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 52, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 52, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 81, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ EVOLVE_MOVE, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 74, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 82, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 72, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 72, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 72, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 90, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 73, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 64, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 65, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 80, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 48, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 54, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 56, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 76, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 1, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 56, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 66, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 85, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 84, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 96, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 66, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 80, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 72, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 72, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 91, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 98, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 66, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:    [ 91, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:      [ 73, Moves.HYPER_BEAM ],
src/data/balance/pokemon-level-moves.ts:      [ 80, Moves.HYPER_BEAM ],
src/data/balance/tms.ts:  [Moves.HYPER_BEAM]: [
src/data/balance/tms.ts:  [Moves.HYPER_BEAM]: ModifierTier.ULTRA,
src/data/moves/move.ts:        Moves.HYPER_BEAM,
src/data/moves/move.ts:    new AttackMove(Moves.HYPER_BEAM, PokemonType.NORMAL, MoveCategory.SPECIAL, 150, 90, 5, -1, 0, 1)
src/phases/move-phase.ts:   * the pokemon is on a recharge turn (ie: {@link Moves.HYPER_BEAM Hyper Beam}), or a 2-turn move was interrupted (ie: {@link Moves.FLY Fly}).
src/enums/moves.ts:  HYPER_BEAM,
test/abilities/parental_bond.test.ts:    game.override.moveset([Moves.HYPER_BEAM]);
test/abilities/parental_bond.test.ts:    game.move.select(Moves.HYPER_BEAM);
test/moves/instruct.test.ts:    game.override.moveset([Moves.INSTRUCT]).enemyMoveset([Moves.SONIC_BOOM, Moves.HYPER_BEAM]);
test/moves/instruct.test.ts:    await game.move.selectEnemyMove(Moves.HYPER_BEAM);
test/moves/metronome.test.ts:    vi.spyOn(randomMoveAttr, "getMoveOverride").mockReturnValue(Moves.HYPER_BEAM);
test/moves/metronome.test.ts:    vi.spyOn(allMoves[Moves.HYPER_BEAM], "accuracy", "get").mockReturnValue(100);
test/moves/hyper_beam.test.ts:    game.override.moveset([Moves.HYPER_BEAM, Moves.TACKLE]);
test/moves/hyper_beam.test.ts:    vi.spyOn(allMoves[Moves.HYPER_BEAM], "accuracy", "get").mockReturnValue(100);
test/moves/hyper_beam.test.ts:    game.move.select(Moves.HYPER_BEAM);

Ok, so I've added Waterfowl Dance to the below, see grep:

jake-eaker:~/pokerogue$ grep -r "WATERFOWL_DANCE"
src/data/balance/tms.ts:  //[Moves.WATERFOWL_DANCE]: [
src/data/balance/tms.ts:  //[Moves.WATERFOWL_DANCE]: ModifierTier.ULTRA,
src/data/moves/move.ts:    //new AttackMove(Moves.WATERFOWL_DANCE, PokemonType.STEEL, MoveCategory.PHYSICAL, 25, 100, 5, 0, 0, 9)
src/enums/moves.ts:  //WATERFOWL_DANCE,

I will still need to set up animations and indicate which pokemon can learn the move.
Then, I will need to set up the event in which you learn the move.


6/4/2025
Status: ✅ Move implemented, learned in-game, and functional in battle.
✅ What’s done:

    WATERFOWL_DANCE enum added and confirmed indexed correctly.

    Move behavior defined in move.ts under initMoves() using AttackMove.

    Assigned move to Bulbasaur (and later Charmander) for quick testing via level 1 in pokemon-level-moves.ts.

    Animation JSON (waterfowl-dance.json) added — copied from fury-attack.json.

    Animation file is named correctly and picked up automatically.

    Verified in battle: move appears, animates, and damages correctly.

⚠️ Known Issues / TODOs:

    Recoil not currently applying. recklessMove() is called, but result not observed.

        Check whether RecoilAttr is also needed.

        Investigate how recoil is processed — possibly add logging or check how Double-Edge or Wild Charge are implemented.

    Move name string not localized.

        Displays as waterfowlDance.name.

        Requires adding display name + description to moves.ts or i18n strings depending on how localization is handled.

🧠 Dev Notes:

    Enum placement matters. Had collision with MALIGNANT_CHAIN until enum order and move init order were corrected.

    Autoincrementing IDs from enum ordering — keep this in mind when moving things around.

    Tested against wild Pokémon: animation runs, hits land, power/accuracy confirmed working.

✨ Next Steps:

    ✅ Fix recoil behavior (start with checking how RecoilAttr is used).

    ✅ Fix move name display.

    🧪 Add learnable logic via Malenia encounter (WIP, event scaffolding started).

    🎨 Consider a custom animation using PRAS-Slash frames (styling flourish).
