import time
import sys
from net.petri_net import PetriNet
from parse_net.net_parser import Parser
from unfolder.processor import Processor


def main(filepath):
    net = PetriNet()
    parser = Parser(filepath)

    net = parser.parse()
    processor = Processor(net)


if __name__ == "__main__":
    if sys.argv is None:
        raise ValueError("ERROR: net missing")
    startTime = time.time()
    filePath = sys.argv[1]
    main(filePath)
    print(f"--- Execution time: {time.time() - startTime}")
