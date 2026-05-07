# Ren'Py console + Taboo Mode helper
# Place this file in the game/ folder, next to the game's .rpa files.
# Restart the game fully after adding or changing this file.

# Auto-loaded at startup:
# Creates/enables the persistent special-content flag if it does not already exist.
default persistent.is_special = True

# Auto-loaded at startup:
# Enables the developer console.
init -999 python:
    config.developer = True
    config.console = True

# Auto-loaded at startup:
# Enables the game/patch flag that exposes Settings > Gameplay > Taboo Mode.
# The late init priority helps if the base game defines the flag earlier.
init 999 python:
    is_taboo_edition = True

# Optional safety placeholder.
# Keep this only if the game expects a dev_controls screen.
screen dev_controls():
    null
