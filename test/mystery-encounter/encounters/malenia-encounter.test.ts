import { Biome } from "#app/enums/biome";
import { MysteryEncounterType } from "#app/enums/mystery-encounter-type";
import { Species } from "#app/enums/species";
import GameManager from "#test/testUtils/gameManager";
import { afterEach, beforeAll, beforeEach, describe, expect, it, vi } from "vitest";
import * as MysteryEncounters from "#app/data/mystery-encounters/mystery-encounters";
import { MaleniaEncounter } from "#app/data/mystery-encounters/encounters/malenia-encounter";

const defaultParty = [Species.LAPRAS];
const defaultBiome = Biome.PLAINS;
const defaultWave = 1;

describe("Malenia Encounter", () => {
  let phaserGame: Phaser.Game;
  let game: GameManager;

  beforeAll(() => {
    phaserGame = new Phaser.Game({ type: Phaser.HEADLESS });
  });

  beforeEach(async () => {
    game = new GameManager(phaserGame);
    game.override.mysteryEncounterChance(100);
    game.override.startingWave(defaultWave);
    game.override.startingBiome(defaultBiome);
    game.override.disableTrainerWaves();

    vi.spyOn(MysteryEncounters, "mysteryEncountersByBiome", "get").mockReturnValue(
      new Map<Biome, MysteryEncounterType[]>([[defaultBiome, [MysteryEncounterType.MALENIA]]]),
    );
  });

  afterEach(() => {
    game.phaseInterceptor.restoreOg();
    vi.clearAllMocks();
    vi.resetAllMocks();
  });

  it("should spawn Malenia encounter on wave 1", async () => {
    await game.runToMysteryEncounter(MysteryEncounterType.MALENIA, defaultParty);

    expect(MaleniaEncounter.encounterType).toBe(MysteryEncounterType.MALENIA);
    expect(game.scene.currentBattle.mysteryEncounter?.encounterType).toBe(MysteryEncounterType.MALENIA);
  });
});
