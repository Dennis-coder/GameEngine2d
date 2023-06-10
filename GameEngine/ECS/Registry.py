from .Pool import Pool


class Registry:
    def __init__(self):
        self.pools: dict[any, Pool] = {}
        self.id = 0
        self.max_value = 1000000
        self.capacity = 10000


    def create(self) -> int:
        entity = self.id
        self.id += 1
        return entity

    def destroy(self, entity_id: int):
        for pool in self.pools.values():
            pool.remove(entity_id)
        
    def has(self, entity_id: int, components: list[any]):
        for component in components:
            if component in self.pools:
                if not self.pools[component].contains(entity_id):
                    print(component)
                    return False
        return True
    
    def get(self, entity_id: int, components: list[any]):
        if not self.has(entity_id, components):
            return None
        
        return tuple(self.pools[component].get_component(entity_id) for component in components)

    def emplace(self, entity_id: int, component: any, *args, **kwargs):
        if component not in self.pools:
            self.pools[component] = Pool(self.max_value, self.capacity)
        
        created_component = component(*args, **kwargs)
        self.pools[component].add(entity_id, created_component)

        return created_component

    def erase(self, entity_id: int, component: any):
        if component in self.pools:
            self.pools[component].remove(entity_id)

    def view(self, components: list[any]):
        smallest_pool = None

        for component in components:
            if component not in self.pools:
                return []
            pool = self.pools[component]
            if not smallest_pool or pool.size < smallest_pool.size:
                smallest_pool = pool
        for entity_id in smallest_pool:
            out_list = self.get(entity_id, components)
            if out_list:
                yield entity_id, *out_list