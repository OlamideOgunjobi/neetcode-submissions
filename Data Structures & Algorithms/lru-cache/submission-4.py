class Node:
    def __init__(self, key=0, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

class LRUCache:

    # create a dictionary to store the key and value pairs
    def __init__(self, capacity: int):
        self.stored_vals = dict()
        self.cap = capacity

        self.head = None
    
    def find_node(self, head, key):

        prev = None

        while head:
            if head.key == key:
                return prev, head
            prev = head
            head = head.right

        return None, None

    def move_node_to_front(self, node, front, prev):

        # the most recently used node could already be at the front
        if node != front:
            prev.right = node.right
            node.right = front
            front.left = node
            node.left = None
            front = node

        return front

    def remove_last_from_LRU(self, node):

        # if the LRU has a length of 1
        if not node.right:
            return None, None

        head = node

        prev = None

        while node.right:
            prev = node
            node = node.right

        prev.right = None
        node.left = None

        return node, head

    # dict: get the value of the key
    # LL: update the LRU Cache
    def get(self, key: int) -> int:

        # if the key is not in the 
        if key not in self.stored_vals:
            return -1


        prev, node = self.find_node(self.head, key)
        
        self.head = self.move_node_to_front(node, self.head, prev)

        return self.stored_vals[key]


    # dict: insert value into the dictionary
    # LL: insert into the front of the LRU Cache
    #   : Check if the capacity has been passed
    #   : If it has, remove the last value from the LRU Cache and dict
    def put(self, key: int, value: int) -> None:

        # most recent and new so slap at the front
        if key not in self.stored_vals:
            self.stored_vals[key] = value

            if not self.head:
                self.head = Node(key)
            else:
                tmp = Node(key)
                self.head.left = tmp
                tmp.right = self.head
                self.head = tmp

            # dealing with above capacity
            if len(self.stored_vals) > self.cap:
                removed, self.head = self.remove_last_from_LRU(self.head)

                if not self.head:
                    self.stored_vals = dict()
                else:
                    self.stored_vals.pop(removed.key)
        else: # most recent so find and move to the front
            self.stored_vals[key] = value
            prev, node = self.find_node(self.head, key)
            self.head = self.move_node_to_front(node, self.head, prev)

        