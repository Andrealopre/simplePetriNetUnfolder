class Condition:

    _counter = 1  # condition counter, used as "id"

    def __init__(self, place, event=None):
        self.place = place
        self.event = event
        self.id = Condition._counter
        Condition._counter += 1

    def __eq__(self, other):
        if not isinstance(other, Condition):
            return False
        return self.place == other.place and self.event == other.event

    def __hash__(self):
        ev_id = self.event.id if self.event is not None else -1
        return hash((self.place, ev_id))
