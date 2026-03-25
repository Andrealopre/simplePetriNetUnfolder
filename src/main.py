import time
import sys
from net import PetriNet


def main(filepath):
    net = PetriNet


if __name__ == "__main__":
    if sys.argv is None:
        raise ValueError("ERROR: net missing")
    startTime = time.time()
    filepath = sys.argv[1]
    main(filepath)
    print(f"--- Execution time: {time.time() - startTime}")
