class Event:
    events: dict[str: list[function]] = {}

    @classmethod
    def subscribe(cls, event: str, fn: function):
        if event not in cls.events:
            cls.events[event] = []
        cls.events[event].append(fn)
    
    @classmethod
    def unsubscribe(cls, event: str, fn: function):
        if event in cls.events:
            cls.events[event].remove(fn)
    
    @classmethod
    def post(cls, event: str, *data: list):
        for fn in cls.events[event]:
            fn(data)