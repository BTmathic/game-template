import tcod as libtcod


def handle_keys(key):
    # Movement keys
    if key.vk == libtcod.KEY_UP:
        return {'move': (0, -1)}
    elif key.vk == libtcod.KEY_DOWN:
        return {'move': (0, 1)}
    elif key.vk == libtcod.KEY_LEFT:
        return {'move': (-1, 0)}
    elif key.vk == libtcod.KEY_RIGHT:
        return {'move': (1, 0)}

    if key.vk == libtcod.KEY_ENTER and key.alt:
        # Alt + Enter toggles fullscreen view
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Escape exits the window
        return {'exit': True}

    # No key was pressed
    return {}