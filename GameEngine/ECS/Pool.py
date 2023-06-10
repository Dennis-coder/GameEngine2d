class Pool:
    def __init__(self, max_value, capacity):
        self.indices = [None] * (max_value+1)
        self.entities = [None] * capacity
        self.components = [None] * capacity
        self.capacity = capacity               # capacity of set or size of dense
        self.max_value = max_value           # Maximum value in set or size of sparse
        self.n = 0                     # Current no of elements, No elements initially
 
    def index(self, entity_id):
        # Searched element must be in range
        if entity_id > self.max_value:
            return -1
 
        # The first condition verifies that 'x' is
        # within 'n' in this set and the second
        # condition tells us that it is present in
        # the data structure.
        if self.indices[entity_id] != None:
            return self.indices[entity_id]
 
        # Not found
        return -1
    
    def contains(self, entity_id):
        return False if self.index(entity_id) == -1 else True
 
    def add(self, entity_id, component):
        # Corner cases, x must not be out of
        # range, dense[] should not be full and
        # x should not already be present
        if entity_id > self.max_value:
            return
        if self.n >= self.capacity:
            return
        if self.index(entity_id) != -1:
            return
 
        # Inserting into array-dense[] at index 'n'.
        self.entities[self.n] = entity_id
        self.components[self.n] = component
 
        # Mapping it to sparse[] array.
        self.indices[entity_id] = self.n
 
        # Increment count of elements in set
        self.n += 1
 
    def remove(self, entity_id):
        # If x is not present
        if not self.index(entity_id):
            return
 
        temp_entity_id = self.entities[self.n - 1]  # Take an element from end
        temp_component = self.components[self.n - 1]  # Take an element from end

        self.entities[self.indices[entity_id]] = temp_entity_id  # Overwrite.
        self.components[self.indices[entity_id]] = temp_component  # Overwrite.

        self.indices[temp_entity_id] = self.indices[entity_id]  # Overwrite.
        self.indices[entity_id] = None
 
        # Since one element has been deleted, we
        # decrement 'n' by 1.
        self.n -= 1
 
    def get_component(self, entity_id):
        index = self.index(entity_id)
        if index == -1:
            return None
        
        return self.components[index]
    
    def intersection(self, other):
        # Capacity and max value of result set
        iCap = min(self.n, other.n)
        iMaxVal = max(other.maxValue, self.max_value)
 
        # Create result set
        result = Pool(iMaxVal, iCap)
 
        # Find the smaller of two sets
        # If this set is smaller
        if self.n < other.n:
            # Search every element of this set in 's'.
            # If found, add it to result
            for i in range(self.n):
                if other.search(self.entites[i]) != -1:
                    result.add(self.entites[i], self.components[i])
        else:
            # Search every element of 's' in this set.
            # If found, add it to result
            for i in range(other.n):
                if self.index(other.entites[i]) != -1:
                    result.add(other.dense[i], other.components[i])
 
        return result

    def __iter__(self):
        for i in range(self.n):
            yield self.entities[i]
    
    @property
    def size(self):
        return self.n