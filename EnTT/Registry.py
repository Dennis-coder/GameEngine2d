from .Pool import Pool
from collections.abc import Sequence


class Registry:
    def __init__(self):
        self.__entities__ = []
        self.__pools__: dict[any, Pool] = {}
        self.__max_value__ = 1000000
        self.__capacity__ = 10000
        self.__destroyed__ = None


    # def create(self) -> tuple[int, int]:
    #     if self.destroyed != None:
    #         entity_id = self.destroyed
    #         self.destroyed, version = self.entities[self.destroyed]
    #         self.entities[entity_id] = (entity_id, version)
    #     else:
    #         entity_id = len(self.entities)
    #         self.entities.append((entity_id, 0))
    #     return self.entities[entity_id]
    
    # def destroy(self, entity: tuple[int, int]):
    #     entity_id, version = entity
    #     for pool in self.pools.values():
    #         pool.remove(entity_id)

    #     self.entities[entity_id] = (self.destroyed, version+1) if self.destroyed != None else (None, version+1)
    #     self.destroyed = entity_id

    def create(self) -> int:
        if self.__destroyed__ != None:
            entity_id = self.__destroyed__
            self.__destroyed__ = self.__entities__[self.__destroyed__]
            self.__entities__[entity_id] = entity_id
        else:
            entity_id = len(self.__entities__)
            self.__entities__.append(entity_id)
        return entity_id

    def destroy(self, entity_id: int):
        for pool in self.__pools__.values():
            pool.remove(entity_id)

        self.__entities__[entity_id] = self.__destroyed__ if self.__destroyed__ != None else None
        self.__destroyed__ = entity_id
        
    def has(self, entity_id: int, components):
        if isinstance(components, Sequence):
            for component in components:
                if component not in self.__pools__ or not self.__pools__[component].contains(entity_id):
                    return False
            return True
        return components in self.__pools__ and self.__pools__[components].contains(entity_id)
    
    def get(self, entity_id: int, components):
        if not self.has(entity_id, components):
            return None
        
        if isinstance(components, Sequence):
            return tuple(self.__pools__[component].get_component(entity_id) for component in components)
        else:
            return self.__pools__[components].get_component(entity_id)

    def emplace(self, entity_id: int, component: any, *args, **kwargs):
        if component not in self.__pools__:
            self.__pools__[component] = Pool(self.__max_value__, self.__capacity__)
        created_component = component(*args, **kwargs)
        self.__pools__[component].add(entity_id, created_component)
        return created_component

    def erase(self, entity_id: int, component: any):
        if component in self.__pools__:
            self.__pools__[component].remove(entity_id)

    def view(self, components: any):
        if isinstance(components, Sequence):
            smallest_pool = None
            for component in components:
                if component not in self.__pools__:
                    return []
                pool = self.__pools__[component]
                if not smallest_pool or pool.size < smallest_pool.size:
                    smallest_pool = pool
            for entity_id in smallest_pool:
                if self.has(entity_id, components):
                    yield entity_id
        else:
            if components not in self.__pools__:
                return []
            for entity_id in self.__pools__[components]:
                if self.has(entity_id, components):
                    yield entity_id

if __name__ == "__main__":
    reg = Registry()
    e0 = reg.create()
    print(reg.__entities__, reg.__destroyed__) # [(0, 0)] None
    e1 = reg.create()
    print(reg.__entities__, reg.__destroyed__) # [(0, 0), (1, 0)] None
    e2 = reg.create()
    print(reg.__entities__, reg.__destroyed__) # [(0, 0), (1, 0), (2, 0)] None
    reg.destroy(e1)
    print(reg.__entities__, reg.__destroyed__) # [(0, 0), (None, 1), (2, 0)] 1
    e1 = reg.create()
    print(reg.__entities__, reg.__destroyed__) # [(0, 0), (1, 1), (2, 0)] None
    reg.destroy(e1)
    print(reg.__entities__, reg.__destroyed__) # [(0, 0), (None, 2), (2, 0)] 1
    reg.destroy(e0)
    print(reg.__entities__, reg.__destroyed__) # [(1, 1), (None, 2), (2, 0)] 0
    reg.destroy(e2)
    print(reg.__entities__, reg.__destroyed__) # [(1, 1), (None, 2), (0, 1)] 2
    e2 = reg.create()
    print(reg.__entities__, reg.__destroyed__) # [(1, 1), (None, 2), (2, 1)] 0
    e0 = reg.create()
    print(reg.__entities__, reg.__destroyed__) # [(0, 1), (None, 2), (2, 1)] 1
    e1 = reg.create()
    print(reg.__entities__, reg.__destroyed__) # [(0, 1), (1, 2), (2, 1)] None
    e3 = reg.create()
    print(reg.__entities__, reg.__destroyed__) # [(0, 1), (1, 2), (2, 1), (3, 0)] None
    print(e0,e1,e2,e3)                 # (0, 1) (1, 2) (2, 1) (3, 0)
