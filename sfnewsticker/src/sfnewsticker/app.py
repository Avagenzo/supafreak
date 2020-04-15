"""
Custom Newsticker App with Beeware Tools
This file contains the logic and application window
"""

import toga
from toga import Group
from toga.style.pack import Pack, COLUMN


def build(app):
    main_box = toga.Box(style=Pack(direction=COLUMN, padding_top=50))
    settings_icon = "icons/baseline_settings_black_48dp.png"
    search_icon = "icons/baseline_search_black_48dp.png"

    toolbar_grp: Group = toga.Group('Toolbar')

    settings_cmd = toga.Command(
        settings_action,
        label='Settings',
        tooltip='Change Settings',
        # shortcut=toga.Key.MOD_1 + 'k',
        icon=settings_icon,
        group=toolbar_grp
    )

    search_cmd = toga.Command(
        search_action,
        label='Search',
        tooltip='Search',
        icon=search_icon,
        group=toolbar_grp
    )

    button = toga.Button(
        'Say Hello!',
        on_press=say_hello,
        style=Pack(padding=50)
    )

    main_box.add(button)

    # app.main_window = toga.MainWindow()
    # app.main_window.content = main_box
    app.main_window.toolbar.add(search_cmd, settings_cmd)
    # app.main_window.show()

    # app.commands.add(settings_cmd, search_cmd)

    return main_box


def settings_action(widget):
    print("Settings")


def search_action(widget):
    print("Search")


def say_hello(widget):
    print("Hello")


def main():
    """
    Function to call main function with title and startup method
    :return:
    """
    return toga.App('Supafreak Newsticker', startup=build)


if __name__ == '__main__':
    main().main_loop()
