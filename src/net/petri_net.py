class Place:

    def __init__(self, name, tokens):
        self.name = name
        self.tokens = tokens


class Transition:

    def __init__(self, name):
        self.name = name


class Arc:

    def __init__(self, src, dst, weight=1):

        self.src = src
        self.dst = dst
        self.weight = weight


class PetriNet:

    def __init__(self):
        self.places = {}
        self.transitions = {}
        self.arcs = []

    def addPlace(self, p_name, token):
        if token > 1:
            raise ValueError("ERROR: the software only works for 1-safe nets")
        self.places[p_name] = Place(p_name, token)

    def addTransition(self, t_name):
        self.transitions[t_name] = Transition(t_name)

    def addArc(self, src, dst, weight=1):

        if src in self.places and dst in self.transitions:
            self.arcs.append(Arc(self.places[src], self.transitions[dst], weight))
        elif src in self.transitions and dst in self.places:
            self.arcs.append(Arc(self.transitions[src], self.places[dst], weight))
        else:
            raise ValueError("ERROR: invalid arc")

    def pasteNet(self):
        for p in self.places:
            print(f"Place: {p}")

        for t in self.transitions:
            print(f"Transition: {t}")

        for a in self.arcs:
            print(f"Arcs: {a.src.name} -> {a.dst.name}")

        for p_name, p_obj in self.places.items():
            print(f"{p_name} has {p_obj.tokens} tokens")
