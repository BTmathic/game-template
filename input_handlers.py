import tcod as libtcod


def handle_keys(key):
    # Movement keys
    key_char = chr(key.c)
    if key.vk == libtcod.KEY_UP or key_char == 'k' or key_char == 'w':
        return {'move': (0, -1)}
    elif key.vk == libtcod.KEY_DOWN or key_char == 'j' or key_char == 's':
        return {'move': (0, 1)}
    elif key.vk == libtcod.KEY_LEFT or key_char == 'h' or key_char == 'a':
        return {'move': (-1, 0)}
    elif key.vk == libtcod.KEY_RIGHT or key_char == 'l' or key_char == 'd':
        return {'move': (1, 0)}
    elif key_char == 'y' or key_char == 'q':
        return {'move': (-1, -1)}
    elif key_char == 'u' or key_char == 'e':
        return {'move': (1, -1)}
    elif key_char == 'b' or key_char == 'z':
        return {'move': (-1, 1)}
    elif key_char == 'n' or key_char == 'c':
        return {'move': (1, 1)}

    if key.vk == libtcod.KEY_ENTER and key.alt:
        # Alt + Enter toggles fullscreen view
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Escape exits the window
        return {'exit': True}

    # No key was pressed
    return {}