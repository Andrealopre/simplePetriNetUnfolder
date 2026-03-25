class Event:

    _counter = 1 # event counter, used as id
    
    def _init__(self, transition, preset_conditions):
        self.transition = transition
        self.preset_conditions = preset_conditions
        self.postset_conditions = set()
        self.id = Event._counter
        Event._counter += 1

    def _eq_(self, other):
        return isinstance(other, Event) and self.id == other.id

    def __hash__(self):
        return hash(self.id)
