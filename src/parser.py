from net import PetriNet


class Parser:

    def __init__(self, filepath):
        self.filepath = filepath

    def parse(self):
        net = PetriNet()

        with open(self.filepath, encoding="UTF-8") as file:
            for line in file:
                v = line.split()

                if not v:
                    continue

                if v[0] == "p":
                    if len(v) != 6:
                        raise ValueError("ERROR: place format not valid")

                    _, _, _, name, token, _ = v
                    net.addPlace(name, int(token))

                elif v[0] == "t":
                    if len(v) != 7:
                        raise ValueError("ERROR: transition format not valid")

                    _, _, _, name, _, _, _ = v
                    net.addTransition(name)

                elif v[0] == "e":
                    if len(v) != 5:
                        raise ValueError("ERROR: arc format not valid")

                    _, source, destination, weight, _ = v
                    net.addArc(source, destination, weight)

                elif v[0] == "h":
                    continue
                else:
                    raise ValueError("ERROR: unknown line")

        return net
