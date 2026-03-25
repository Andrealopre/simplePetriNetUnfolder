import time
import sys
from net.petri_net import PetriNet
from parser.net_parser import Parser

def main(filepath):
    net = PetriNet()
    parser = Parser(filepath)

    net = parser.parse()


if __name__ == "__main__":
    if sys.argv is None:
        raise ValueError("ERROR: net missing")
    startTime = time.time()
    filepath = sys.argv[1]
    main(filepath)
    print(f"--- Execution time: {time.time() - startTime}")
