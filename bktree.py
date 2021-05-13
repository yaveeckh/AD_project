class BKTreeNode():
    
    def __init__(self, key):
        self._key = key
        self._children = {}

class BKTree():
    
    def __init__(self, distance_function):
        self._root = None
        self._count = 0
        self._distance_function = distance_function
        
    def __len__(self):
        return self._count
        
    def insert(self, key):
        """complete this function"""
        node = BKTreeNode(key)
        
        if (self._root == None):
            self._root = node
        else:
            current_node = self._root
            k = self._distance_function(node._key, current_node._key)
            
            while k in current_node._children:
                current_node = current_node._children[k]
                k = self._distance_function(current_node._key, node._key)
            
            current_node._children[k] = node;
                
        pass   
                    
    def get(self, key, max_dist = 1):
        """complete this function"""
        candidates = [self._root]
        results = []
        
        while len(candidates) > 0:
            current_node = candidates.pop(0)
            distance = self._distance_function(current_node._key, key)
            
            if distance <= max_dist:
                results.append(current_node)
                
            candidates.extend(child_node for child_distance, child_node in current_node._children.items() if distance - max_dist <= child_distance <= distance + max_dist)
        
        return results             
        pass