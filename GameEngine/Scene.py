from __future__ import annotations
from .ECS import Entity, Component, System, Components
import inspect

class Scene:

    def __init__(self):
        self.entities: dict[Component: set[Entity]] = {
            cls_obj: set()
            for _, cls_obj in inspect.getmembers(Components)
            if inspect.isclass(cls_obj)
        }
        self.systems: list[System] = []
    
    def update(self, dt: int) -> None:
        for system in self.systems:
            if not system.is_active:
                continue
            if system.interval:
                system.buffered_time += dt
                while system.buffered_time >= system.interval:
                    system.update(dt)
                    system.buffered_time -= system.interval
            else:
                system.update(dt)
    
    def add_entity(self, components: list[Component]) -> Entity:
        entity: Entity = Entity(self, components)
        self.entities.add(entity)
        return entity

    def remove_entity(self, entity: Entity) -> None:
        self.entites.remove(entity)

    def query(self, filter: list[Component]):
        pass
    
    def add_system(self, system: System) -> None:
        self.systems.append(system(self))
    
    def remove_system(self, system):
        self.systems.remove(system)
        