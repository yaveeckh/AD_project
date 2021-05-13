class RedBlackTreeNode():
    
    def __init__(self, key, value, parent = None, left = None, right = None):
        self._key = key
        self._values = [value]
        self._parent = parent
        self._black = False
        self._left = None
        self._right = None


class RedBlackTree():
    
    def __init__(self):
        self._root = None
        self._count = 0
        
    def __len__(self):
        return self._count
        
    def insert(self, key, value):
        """complete this function"""
        pass
                            
    def _right_rotate(self, node):
        """complete this function"""
        pass
        
    def _left_rotate(self, node):
        """complete this function"""
        pass
                    
    def get(self, key):
        """complete this function"""
        pass