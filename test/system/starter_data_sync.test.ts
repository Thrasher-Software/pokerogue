import GameManager from "#test/testUtils/gameManager";
import { Species } from "#enums/species";
import Phaser from "phaser";
import { beforeAll, beforeEach, afterEach, describe, it, expect } from "vitest";

describe("System - Starter Data Sync", () => {
  let phaserGame: Phaser.Game;
  let game: GameManager;

  beforeAll(() => {
    phaserGame = new Phaser.Game({ type: Phaser.HEADLESS });
  });

  beforeEach(() => {
    game = new GameManager(phaserGame);
  });

  afterEach(() => {
    game.phaseInterceptor.restoreOg();
  });

  it("adds missing starter data entries when loading", async () => {
    const save = game.scene.gameData.getSystemSaveData();
    delete save.starterData[Species.ARTORIAS];
    delete save.dexData[Species.ARTORIAS];

    await game.scene.gameData.initSystem(JSON.stringify(save));

    expect(game.scene.gameData.starterData[Species.ARTORIAS]).toBeDefined();
    expect(game.scene.gameData.dexData[Species.ARTORIAS]).toBeDefined();
  });
});
