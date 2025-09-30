# RogueLifePy codebase overview

## High-level architecture
RogueLifePy is a desktop game built with PySide6. The application boots from `start.py`, where the Qt `QApplication` is created, core modules are initialized, data files are loaded, and the main window plus supporting tools are shown before the event loop begins.【F:start.py†L1-L58】

The project favors a modular design: each feature (main menu, gameplay loop, data ingestion, debugging tools, etc.) lives in its own module under the repository root, and most UI is described through Qt Designer generated classes in the `ui/` package (for example, `ui.ui_form_main` and `ui.ui_form_game`).【F:RLMain.py†L13-L38】【F:RLGame.py†L16-L48】

## Startup flow
When you run `start.py`, the game performs the following steps before control enters the Qt event loop:

1. Initialize global state (icons, registries, timers) via `global_var.init()`.【F:global_var.py†L49-L116】
2. Bring up the debugging console, configuration manager, player model, update dialog, and utility menu helpers so they can react to later events.【F:start.py†L26-L47】
3. Load every JSON file under `data/`, validate them, de-duplicate via SHA1 hashes, and dispatch the parsed payloads to the appropriate loaders (config, items, events, challenges, actions, and player saves).【F:RLDataFiles.py†L18-L146】
4. Instantiate each major window (`RLMain`, `RLGame`, editor, command console), finish timing metrics, show the main window, and optionally trigger an update check against GitHub.【F:start.py†L34-L55】

Understanding this sequence is key when you introduce new subsystems—you typically need to hook their initialization here.

## Primary UI layers
* **Main menu (`RLMain`)** – Hosts the landing experience, handles eggs/about dialogs, and routes players into gameplay or the feature menu. It toggles menu affordances based on config flags and centralizes quit confirmation.【F:RLMain.py†L18-L165】
* **Game screen (`RLGame`)** – Implements the core gameplay loop: presenting events, managing action selections, rolling dice (with animations), and branching to success/failure results. It also exposes menus for collections, adjustments, and developer tooling when enabled.【F:RLGame.py†L21-L200】
* **Utility menu (`RLUtility.RLMenu`)** – Provides meta-features such as opening data folders, importing/syncing JSON content from GitHub, manual update checks, and shortcuts to the debug console, command prompt, and editor.【F:RLUtility.py†L25-L200】
* **Debug console (`RLDebug`)** – Centralized logging surface that mirrors output to both the window and stdout (optionally to `debug_output.log`). Every subsystem uses it to report progress, warnings, and errors with consistent tagging.【F:RLDebug.py†L13-L137】

Qt Designer generated UI classes (`ui_form_main`, `ui_form_game`, `ui_form_utility`, etc.) define widget layouts, while the Python controllers above wire up behavior and state.

## Data-driven content pipeline
Almost all game content is externalized into JSON files under `data/`. During startup the loader dispatches each file by `type`, allowing you to extend the game without touching the UI controllers.【F:RLDataFiles.py†L18-L146】 Key loaders include:

* **Configuration (`RLConfigs`)** – Applies global feature flags (debug console, editor, update ignores, discovered eggs) with user confirmation when overriding existing settings.【F:RLConfigs.py†L7-L119】
* **Items (`RLItems`)** – Builds collectible objects from JSON, tracks rarity weights for random selection, and initializes the weighted random generator for future draws.【F:RLItems.py†L7-L92】
* **Events (`RLEvents`)** – Parses story events, their rarity, mutually exclusive/required prerequisites, attached challenges, and potential rewards before seeding a weighted random picker.【F:RLEvents.py†L7-L109】
* **Actions (`RLActions`)** – Defines the checks players can take during events, required success points, and branching outcomes, leveraging player adjustments during resolution.【F:RLActions.py†L1-L61】
* **Challenges (`RLChallenges`)** – Works in tandem with events (inspect this module next to see how difficulty checks are modeled).
* **Player saves (`RLPlayer` via `load_player_info`)** – Restores earned adjustments, items, and save metadata when a `player` data file is encountered.【F:RLPlayer.py†L107-L141】

Weighted random selection logic lives in `RLRandom.WeightedRandom`, which normalizes configured weights and provides fast random index sampling. The items and events loaders both rely on it.【F:RLRandom.py†L7-L62】【F:RLItems.py†L89-L92】【F:RLEvents.py†L106-L109】

## Global state and player model
Shared registries (items, events, actions, player data, hash caches, etc.) live in `global_var`. Each loader populates these dictionaries, and UI modules read from them during gameplay. The `Player` model exposes helpers for applying adjustments, acquiring items, and enforcing event/item prerequisites based on those registries.【F:global_var.py†L19-L116】【F:RLPlayer.py†L5-L101】

Because the state is mutable and globally accessible, it is important to respect initialization order and consider thread-safety (dice animations use background threads). When adding new global data, follow the existing pattern in `global_var.init()`.

## Working effectively in the project
* **Logging:** Use `RLDebug.debug(...)` when instrumenting new code to ensure messages appear in both the debug window and console, and to keep source tagging consistent.【F:RLDebug.py†L36-L109】
* **Data validation:** Match the required key patterns used in existing loaders to avoid runtime skips. When introducing new JSON fields, update the relevant loader to validate and apply them.
* **UI changes:** Modify the Qt Designer `.ui` files under `ui/`, regenerate the Python stubs, and then adjust the controller methods. Each window sets icons and connects signals in its constructor; mirror that style for new widgets.【F:RLMain.py†L20-L38】【F:RLGame.py†L21-L60】【F:RLUtility.py†L25-L45】

## Suggested next steps for newcomers
1. **Study the JSON schemas** by opening the files in `data/` and cross-referencing how each loader consumes them. This will clarify how to craft new items/events or tweak gameplay balance.【F:RLDataFiles.py†L18-L146】【F:RLItems.py†L41-L85】【F:RLEvents.py†L54-L103】
2. **Explore challenge resolution** by reading `RLChallenges.py` and `RLConditions.py` to see how dice results and modifiers flow into success/failure outcomes.
3. **Trace the gameplay loop** starting from `RLGame.forward()` through dice rolling, event resolution, and transitions to deepen your understanding before adding mechanics.【F:RLGame.py†L107-L200】
4. **Experiment with debug tools**: launch the debug console and utility menu, try syncing data files, and observe the logs to learn how the system surfaces errors and updates.【F:RLUtility.py†L134-L200】【F:RLDebug.py†L25-L137】

Armed with these insights, you can iteratively expand RogueLifePy by updating data definitions, enhancing the UI, or extending the gameplay controllers.
