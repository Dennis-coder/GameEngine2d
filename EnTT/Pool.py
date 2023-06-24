class Pool:
    def __init__(self, max_value, capacity):
        self.__indices__ = [None] * (max_value+1)
        self.__entities__ = [None] * capacity
        self.__components__ = [None] * capacity
        self.__capacity__ = capacity               # capacity of set or size of dense
        self.__max_value__ = max_value           # Maximum value in set or size of sparse
        self.__n__ = 0                     # Current no of elements, No elements initially

    def __index__(self, entity_id):
        # Searched element must be in range
        if entity_id > self.__max_value__:
            return -1
 
        # The first condition verifies that 'x' is
        # within 'n' in this set and the second
        # condition tells us that it is present in
        # the data structure.
        if self.__indices__[entity_id] != None:
            return self.__indices__[entity_id]
 
        # Not found
        return -1
    
    def contains(self, entity_id):
        return False if self.__index__(entity_id) == -1 else True
 
    def add(self, entity_id, component):
        # Corner cases, x must not be out of
        # range, dense[] should not be full and
        # x should not already be present
        if entity_id > self.__max_value__:
            return
        if self.__n__ >= self.__capacity__:
            return
        if self.__index__(entity_id) != -1:
            return
 
        # Inserting into array-dense[] at index 'n'.
        self.__entities__[self.__n__] = entity_id
        self.__components__[self.__n__] = component
 
        # Mapping it to sparse[] array.
        self.__indices__[entity_id] = self.__n__
 
        # Increment count of elements in set
        self.__n__ += 1
 
    def remove(self, entity_id):
        # If x is not present
        if not self.__index__(entity_id):
            return
 
        temp_entity_id = self.__entities__[self.__n__ - 1]  # Take an element from end
        temp_component = self.__components__[self.__n__ - 1]  # Take an element from end

        self.__entities__[self.__indices__[entity_id]] = temp_entity_id  # Overwrite.
        self.__components__[self.__indices__[entity_id]] = temp_component  # Overwrite.

        self.__indices__[temp_entity_id] = self.__indices__[entity_id]  # Overwrite.
        self.__indices__[entity_id] = None
 
        # Since one element has been deleted, we
        # decrement 'n' by 1.
        self.__n__ -= 1
 
    def get_component(self, entity_id):
        index = self.__index__(entity_id)
        if index == -1:
            return None
        
        return self.__components__[index]
    
    def __iter__(self):
        for i in range(self.__n__):
            yield self.__entities__[i]
    
    @property
    def size(self):
        return self.__n__