<picture><img src="./public/images/logo.png" width="300" alt="PokéRogue"></picture>

PokéRogue is a browser based Pokémon fangame heavily inspired by the roguelite genre. Battle endlessly while gathering stacking items, exploring many different biomes, fighting trainers, bosses, and more!

# Contributing

## 🛠️ Development

If you have the motivation and experience with Typescript/Javascript (or are willing to learn) please feel free to fork the repository and make pull requests with contributions. If you don't know what to work on but want to help, reference the below **To-Do** section or the **#feature-vote** channel in the discord.

### 💻 Environment Setup

#### Prerequisites

- node: 22.14.0
- npm: [how to install](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

#### Running Locally

1. Clone the repo and in the root directory run `npm install`
    - *if you run into any errors, reach out in the **#dev-corner** channel in discord*
2. Run `npm run start:dev` to locally run the project in `localhost:8000`

#### Linting

We're using Biome as our common linter and formatter. It will run automatically during the pre-commit hook but if you would like to manually run it, use the `npm run biome` script. To view the complete rules, check out the [biome.jsonc](./biome.jsonc) file.

### 📚 Documentation

You can find the auto-generated documentation [here](https://pagefaultgames.github.io/pokerogue/main/index.html).
For information on enemy AI, check out the [enemy-ai.md](./docs/enemy-ai.md) file.
For detailed guidelines on documenting your code, refer to the [comments.md](./docs/comments.md) file.

### ❔ FAQ

**How do I test a new _______?**

- In the `src/overrides.ts` file there are overrides for most values you'll need to change for testing

**How do I create new moves?**

- A Python script has been created to help generate move code. You can find it in the `movemaker` directory.
- Set up a virtual environment: `cd movemaker && python3 -m venv venv && source venv/bin/activate`
- Run the script: `python movemaker.py`
- Follow the prompts to create a move, and paste the generated code into `src/data/moves/move.ts`
- See the [movemaker README](./movemaker/README.md) for more details

**How do I retrieve the translations?**

- The translations were moved to the [dedicated translation repository](https://github.com/pagefaultgames/pokerogue-locales) and are now applied as a submodule in this project.
- The command to retrieve the translations is `git submodule update --init --recursive`. If you still struggle to get it working, please reach out to #dev-corner channel in Discord.

## 🪧 To Do

Check out [Github Issues](https://github.com/pagefaultgames/pokerogue/issues) to see how can you help us!

# 📝 Credits
>
> If this project contains assets you have produced and you do not see your name, **please** reach out, either [here on GitHub](https://github.com/pagefaultgames/pokerogue/issues/new) or via [Discord](https://discord.gg/pokerogue).

Thank you to all the wonderful people that have contributed to the PokéRogue project! You can find the credits [here](./CREDITS.md).
