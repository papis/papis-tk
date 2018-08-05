"""
Tk gui
*******
.. papis-config:: open
    :section: tk-gui

.. papis-config:: edit
    :section: tk-gui

.. papis-config:: exit
    :section: tk-gui

.. papis-config:: clear
    :section: tk-gui

.. papis-config:: help
    :section: tk-gui

.. papis-config:: focus_prompt
    :section: tk-gui

.. papis-config:: move_down
    :section: tk-gui

.. papis-config:: move_up
    :section: tk-gui

.. papis-config:: move_top
    :section: tk-gui

.. papis-config:: move_bottom
    :section: tk-gui

.. papis-config:: print_info
    :section: tk-gui

.. papis-config:: half_down
    :section: tk-gui

.. papis-config:: half_up
    :section: tk-gui

.. papis-config:: scroll_down
    :section: tk-gui

.. papis-config:: scroll_up
    :section: tk-gui

.. papis-config:: prompt-fg
    :section: tk-gui

.. papis-config:: prompt-bg
    :section: tk-gui

    Color of the foreground of an entry

.. papis-config:: entry-fg
    :section: tk-gui

    Color of the foreground of an active entry

.. papis-config:: activeforeground
    :section: tk-gui

    Color of the background of an active entry

.. papis-config:: activebackground
    :section: tk-gui

.. papis-config:: insertbackground
    :section: tk-gui

.. papis-config:: prompt-font-size
    :section: tk-gui

.. papis-config:: entry-bg-size
    :section: tk-gui

.. papis-config:: entry-font-size
    :section: tk-gui

.. papis-config:: entry-font-name
    :section: tk-gui

.. papis-config:: entry-font-style
    :section: tk-gui

.. papis-config:: entry-lines
    :section: tk-gui

.. papis-config:: entry-bg-odd
    :section: tk-gui

.. papis-config:: entry-bg-pair
    :section: tk-gui

.. papis-config:: cursor
    :section: tk-gui

.. papis-config:: height
    :section: tk-gui

.. papis-config:: labels-per-page
    :section: tk-gui

.. papis-config:: borderwidth
    :section: tk-gui

.. papis-config:: window-width
    :section: tk-gui

.. papis-config:: window-bg
    :section: tk-gui

.. papis-config:: window-height
    :section: tk-gui

.. papis-config:: match-format
    :section: tk-gui

.. papis-config:: header-format
    :section: tk-gui

"""

import papis.config


configuration_settings = {
    "tk-gui": {
        "open": "o",
        "edit": "e",
        "exit": "<Control-q>",
        "clear": "q",
        "help": "h",
        "focus_prompt": ":",
        "move_down": "j",
        "move_up": "k",
        "move_top": "g",
        "move_bottom": "<Shift-G>",
        "print_info": "i",
        "half_down": "<Control-d>",
        "half_up": "<Control-u>",
        "scroll_down": "<Control-e>",
        "scroll_up": "<Control-y>",
        "prompt-fg": "lightgreen",
        "prompt-bg": "black",
        # Color of the foreground of an entry
        "entry-fg": "grey77",
        # Color of the foreground of an active entry
        "activeforeground": "gray99",
        # Color of the background of an active entry
        "activebackground": "#394249",
        "insertbackground": "red",
        "prompt-font-size": "14",
        "entry-bg-size": "14",
        "entry-font-size": "14",
        "entry-font-name": "Times",
        "entry-font-style": "normal",
        "entry-lines": "3",
        "entry-bg-odd": "#273238",
        "entry-bg-pair": "#273238",
        "cursor": "xterm",
        "height": 1,
        "labels-per-page": 6,
        "borderwidth": -1,
        "window-width": "1200",
        "window-bg": "#273238",
        "window-height": "700",
        "match-format": \
            "{doc[tags]}{doc.subfolder}{doc[title]}"
            "{doc[author]}{doc[year]}",
        "header-format": \
            "{doc[title]}\n"\
            "{doc[empty]}   {doc[author]}\n"\
            "({doc[year]:->4})",
    }
}


def register_default_settings():
    papis.config.register_default_settings(configuration_settings)
