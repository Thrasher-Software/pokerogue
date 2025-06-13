// Test script for Artorias type display debugging
// Run this in browser console when in starter selection screen

function testArtoriasTypeDisplay() {
    console.log("=== Artorias Type Display Test ===");

    // Get the starter select UI handler
    const scene = globalScene;
    if (!scene || !scene.ui) {
        console.error("Game scene not found");
        return;
    }

    const starterHandler = scene.ui.handlers[7]; // UiMode.STARTER_SELECT = 7
    if (!starterHandler) {
        console.error("Starter select handler not found");
        return;
    }

    console.log("Found starter handler:", starterHandler);

    // Find Artorias in the containers
    const artoriasContainer = starterHandler.filteredStarterContainers.find(
        container => container.species.speciesId === 8902
    );

    if (!artoriasContainer) {
        console.error("Artorias not found in filtered containers");
        console.log("Available species:", starterHandler.filteredStarterContainers.map(c =>
            `${c.species.name} (${c.species.speciesId})`
        ));
        return;
    }

    console.log("Found Artorias container:", artoriasContainer);
    console.log("Artorias species:", artoriasContainer.species);
    console.log("Artorias type1:", artoriasContainer.species.type1);
    console.log("Artorias type2:", artoriasContainer.species.type2);

    // Find Artorias index in filtered containers
    const artoriasIndex = starterHandler.filteredStarterContainers.findIndex(
        container => container.species.speciesId === 8902
    );

    console.log("Artorias index in filtered containers:", artoriasIndex);

    if (artoriasIndex >= 0) {
        console.log("Setting cursor to Artorias...");

        // Store current values for comparison
        const beforeCursor = starterHandler.cursor;
        const beforeLastSpecies = starterHandler.lastSpecies;

        console.log("Before - cursor:", beforeCursor, "lastSpecies:", beforeLastSpecies?.name);

        // Set cursor to Artorias
        starterHandler.setCursor(artoriasIndex);

        // Check after
        const afterCursor = starterHandler.cursor;
        const afterLastSpecies = starterHandler.lastSpecies;
        const currentSpecies = starterHandler.filteredStarterContainers[afterCursor]?.species;

        console.log("After - cursor:", afterCursor, "lastSpecies:", afterLastSpecies?.name);
        console.log("Current species from container:", currentSpecies?.name, currentSpecies?.speciesId);

        // Check type icons
        const type1Icon = starterHandler.type1Icon;
        const type2Icon = starterHandler.type2Icon;

        console.log("Type1 icon visible:", type1Icon.visible, "frame:", type1Icon.frame?.name);
        console.log("Type2 icon visible:", type2Icon.visible, "frame:", type2Icon.frame?.name);

        // Check species form data
        if (currentSpecies) {
            const speciesForm = getPokemonSpeciesForm(currentSpecies.speciesId, 0);
            console.log("Species form type1:", speciesForm.type1, "type2:", speciesForm.type2);
            console.log("Type1 name:", PokemonType[speciesForm.type1]);
            console.log("Type2 name:", speciesForm.type2 !== null ? PokemonType[speciesForm.type2] : "null");
        }

        // Check dex data
        const dexData = scene.gameData.dexData[8902];
        console.log("Artorias dex data:", dexData);

        // Check if species matches
        if (currentSpecies?.speciesId === 8902) {
            console.log("✅ Cursor correctly points to Artorias");

            if (type1Icon.frame?.name === "steel" && type2Icon.frame?.name === "dark") {
                console.log("✅ Type icons show correct Steel/Dark typing");
            } else {
                console.log("❌ Type icons show incorrect typing");
                console.log("Expected: steel/dark, Got:", type1Icon.frame?.name, "/", type2Icon.frame?.name);
            }
        } else {
            console.log("❌ Cursor does not point to Artorias");
            console.log("Expected ID: 8902, Got:", currentSpecies?.speciesId);
        }
    }

    console.log("=== Test Complete ===");
}

function debugFilteredContainers() {
    console.log("=== Filtered Containers Debug ===");

    const scene = globalScene;
    const starterHandler = scene?.ui?.handlers[7];

    if (!starterHandler) {
        console.error("Starter handler not found");
        return;
    }

    console.log("Total filtered containers:", starterHandler.filteredStarterContainers.length);
    console.log("Current cursor:", starterHandler.cursor);
    console.log("Current lastSpecies:", starterHandler.lastSpecies?.name);

    // Show containers around current cursor
    const start = Math.max(0, starterHandler.cursor - 2);
    const end = Math.min(starterHandler.filteredStarterContainers.length, starterHandler.cursor + 3);

    console.log(`Showing containers ${start} to ${end}:`);
    for (let i = start; i < end; i++) {
        const container = starterHandler.filteredStarterContainers[i];
        const marker = i === starterHandler.cursor ? " <-- CURRENT" : "";
        console.log(`[${i}] ${container.species.name} (${container.species.speciesId})${marker}`);
    }
}

// Export functions to global scope for easy access
window.testArtoriasTypeDisplay = testArtoriasTypeDisplay;
window.debugFilteredContainers = debugFilteredContainers;

console.log("Artorias test functions loaded. Use:");
console.log("- testArtoriasTypeDisplay() - Test Artorias type display");
console.log("- debugFilteredContainers() - Debug container array");
