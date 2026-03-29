from unfolder.condition import Condition
from unfolder.event import Event


class Processor:

    conflict_relation = set()
    causal_relation_pre = set()
    causal_relation_post = set()
    events = set()
    conditions = set()

    def __init__(self, net):
        self.net = net
        self.min = set()

        self.cut_off = set()

        self.minimum = {}

    def unfoldingAlgorithm(self):
        unf = set(self.initialMarking)
        if not unf:
            raise ValueError("ERROR: the net doesn't have an initial marking")

    def initialMarking(self):

        for place_name, place_obj in self.net.places.items():
            if place_obj.tokens > 0:
                newCondition = Condition(place_obj)
                self.conditions.add(newCondition)
                self.min.add(newCondition)

        return self.min
