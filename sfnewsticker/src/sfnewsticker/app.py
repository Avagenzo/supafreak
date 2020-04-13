"""
Custom Newsticker App with Beeware Tools
This file contains the logic and application window
"""

import toga
from toga import Group
from toga.style.pack import Pack, COLUMN


def build(app):
    main_box = toga.Box(style=Pack(direction=COLUMN, padding_top=50))
    settings_icon = "icons/baseline_settings_black_18dp.png"

    toolbar_grp: Group = toga.Group('Toolbar')

    settings_cmd = toga.Command(
        settings_action,
        label='Settings',
        tooltip='Change Settings',
        # shortcut=toga.Key.MOD_1 + 'k',
        icon=settings_icon,
        group=toolbar_grp
    )

    app.commands.add(settings_cmd)
    app.main_window.toolbar.add(settings_cmd)

    return main_box


def settings_action(widget):
    print("Settings")


def main():
    return toga.App('Supafreak Newsticker', startup=build)


if __name__ == '__main__':
    main().main_loop()
