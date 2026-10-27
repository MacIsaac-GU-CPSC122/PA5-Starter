class Empty(Exception):
    """Error attempting to access an element from an empty container.
    """
    pass

class ArrayStack:
    def __init__(self) -> None:
        self._data = []

    def __len__(self) -> int:
        return 0 # TODO: fix this
    
    def is_empty(self) -> bool:
        return True # TODO: fix this
    
    def push(self, e: object) -> None:
        pass # TODO: finish this

    def peek(self) -> object:
        return None # TODO: fix this
    
    def pop(self) -> object:
        return None # TODO: fix this
