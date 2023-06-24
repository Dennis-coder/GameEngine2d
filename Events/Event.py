class Event:
    __events__: dict[str: list[callable]] = {}

    @classmethod
    def subscribe(cls, event: str, fn: callable):
        if event not in cls.__events__:
            cls.__events__[event] = []
        cls.__events__[event].append(fn)
    
    @classmethod
    def unsubscribe(cls, event: str, fn: callable):
        if event in cls.__events__:
            cls.__events__[event].remove(fn)
    
    @classmethod
    def post(cls, event: str, *data: list):
        for fn in cls.__events__[event]:
            fn(data)
