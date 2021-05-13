class BinaryTreeNode():
    
    def __init__(self, key, value, left = None, right = None):
        self._key = key
        self._values = [value]
        self._left = None
        self._right = None
 

class BinaryTree():
    
    def __init__(self):
        self._root = None
        self._count = 0
        
    def __len__(self):
        return self._count
        
    def insert(self, key, value):
        """complete this function"""
        pass
                      
    def get(self, key):
        """complete this function"""
        pass
