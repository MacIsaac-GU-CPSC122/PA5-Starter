class Empty(Exception):
    """Error attempting to access an element from an empty container.
    """
    pass

class ArrayQueue:
    DEFAULT_CAPACITY = 10 # moderate capacity for all new queues

    def __init__(self) -> None:
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self) -> int:
        return 0 # TODO: fix this
    
    def is_empty(self) -> bool:
        return True # TODO: fix this
    
    def enqueue(self, e: object) -> None:
        pass # TODO: finish this

    def peek(self) -> object:
        return None # TODO: fix this
    
    def dequeue(self) -> object:
        return None # TODO: fix this
    
    def clear(self) -> None:
        pass # TODO: finish this
    
    def remove_divisible_by(self, p: int) -> None:
        pass # TODO: finish this