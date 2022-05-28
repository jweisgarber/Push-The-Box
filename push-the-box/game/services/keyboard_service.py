import pyray

class KeyboardService:
    """Detects player input. 
    
    The responsibility of a KeyboardService is to indicate whether or not a key is pressed.

    Attributes:
        _keys (Dict[string, int]): The letter to key mapping.
    """

    def __init__(self):
        """Constructs a new KeyboardService."""
        self._keys = {}
        
        self._keys['w'] = pyray.KEY_W
        self._keys['a'] = pyray.KEY_A
        self._keys['s'] = pyray.KEY_S
        self._keys['d'] = pyray.KEY_D

    def is_key_pressed(self, key):
        """Checks if the given key is currently up.
        
        Args:
            key (string): The given key (w, a, s, d)
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_pressed(pyray_key)
