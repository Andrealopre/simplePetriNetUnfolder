from unfolder.condition import Condition
from unfolder.event import Event
from unfolder.processor import Processor

def initialExtensions(self, unf):
    initialExtensions = set()

    initialMarkings = {c for c in unf if isinstance(c, Condition)}

    for t in Processor.net.transitions.values():
        presetPlaces 
