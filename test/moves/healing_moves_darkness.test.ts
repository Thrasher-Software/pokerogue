import { Abilities } from "#app/enums/abilities";
import { Moves } from "#enums/moves";
import { Species } from "#enums/species";
import { WeatherType } from "#enums/weather-type";
import GameManager from "#test/testUtils/gameManager";
import Phaser from "phaser";
import { afterEach, beforeAll, beforeEach, describe, expect, it } from "vitest";

describe("Healing Moves - Darkness Weather", () => {
  let phaserGame: Phaser.Game;
  let game: GameManager;

  beforeAll(() => {
    phaserGame = new Phaser.Game({
      type: Phaser.HEADLESS,
    });
  });

  afterEach(() => {
    game.phaseInterceptor.restoreOg();
  });

  beforeEach(() => {
    game = new GameManager(phaserGame);
    game.override
      .weather(WeatherType.DARKNESS)
      .battleStyle("single")
      .ability(Abilities.BALL_FETCH)
      .enemyAbility(Abilities.BALL_FETCH)
      .enemySpecies(Species.MAGIKARP)
      .enemyMoveset([Moves.SPLASH]);
  });

  it("Synthesis should heal 1/3 max HP in darkness", async () => {
    game.override.moveset([Moves.SYNTHESIS]);
    await game.classicMode.startBattle([Species.BULBASAUR]);

    const pokemon = game.scene.getPlayerPokemon()!;
    const maxHp = pokemon.getMaxHp();

    // Damage the pokemon first
    pokemon.hp = Math.floor(maxHp * 0.1);
    const hpBeforeHeal = pokemon.hp;

    game.move.select(Moves.SYNTHESIS);
    await game.toNextTurn();

    const expectedHeal = Math.floor(maxHp / 3);
    const actualHeal = pokemon.hp - hpBeforeHeal;

    expect(actualHeal).toBe(expectedHeal);
  });

  it("Morning Sun should heal 1/3 max HP in darkness", async () => {
    game.override.moveset([Moves.MORNING_SUN]);
    await game.classicMode.startBattle([Species.SUNFLORA]);

    const pokemon = game.scene.getPlayerPokemon()!;
    const maxHp = pokemon.getMaxHp();

    // Damage the pokemon first
    pokemon.hp = Math.floor(maxHp * 0.1);
    const hpBeforeHeal = pokemon.hp;

    game.move.select(Moves.MORNING_SUN);
    await game.toNextTurn();

    const expectedHeal = Math.floor(maxHp / 3);
    const actualHeal = pokemon.hp - hpBeforeHeal;

    expect(actualHeal).toBe(expectedHeal);
  });

  it("Moonlight should heal 2/3 max HP in darkness", async () => {
    game.override.moveset([Moves.MOONLIGHT]);
    await game.classicMode.startBattle([Species.CLEFAIRY]);

    const pokemon = game.scene.getPlayerPokemon()!;
    const maxHp = pokemon.getMaxHp();

    // Damage the pokemon first
    pokemon.hp = Math.floor(maxHp * 0.1);
    const hpBeforeHeal = pokemon.hp;

    game.move.select(Moves.MOONLIGHT);
    await game.toNextTurn();

    const expectedHeal = Math.floor(maxHp * 2 / 3);
    const actualHeal = pokemon.hp - hpBeforeHeal;

    expect(actualHeal).toBe(expectedHeal);
  });

  it("healing moves should work normally in other weather conditions", async () => {
    game.override
      .weather(WeatherType.SUNNY)
      .moveset([Moves.SYNTHESIS]);

    await game.classicMode.startBattle([Species.BULBASAUR]);

    const pokemon = game.scene.getPlayerPokemon()!;
    const maxHp = pokemon.getMaxHp();

    // Damage the pokemon first
    pokemon.hp = Math.floor(maxHp * 0.1);
    const hpBeforeHeal = pokemon.hp;

    game.move.select(Moves.SYNTHESIS);
    await game.toNextTurn();

    // In sunny weather, plant heal moves should restore 2/3 HP
    const expectedHeal = Math.floor(maxHp * 2 / 3);
    const actualHeal = pokemon.hp - hpBeforeHeal;

    expect(actualHeal).toBe(expectedHeal);
  });

  it("should not heal beyond max HP in darkness", async () => {
    game.override.moveset([Moves.MOONLIGHT]);
    await game.classicMode.startBattle([Species.CLEFAIRY]);

    const pokemon = game.scene.getPlayerPokemon()!;
    const maxHp = pokemon.getMaxHp();

    // Damage the pokemon slightly (less than 2/3 max HP)
    pokemon.hp = Math.floor(maxHp * 0.8);

    game.move.select(Moves.MOONLIGHT);
    await game.toNextTurn();

    // Should heal to max HP, not exceed it
    expect(pokemon.hp).toBe(maxHp);
  });
});
