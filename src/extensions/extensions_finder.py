from unfolder.condition import Condition
from unfolder.event import Event
import utils.utilities as util


def initialExtensions(net, unf):
    initialExtensions = set()

    initialMarkings = {c for c in unf if isinstance(c, Condition)}

    for t in net.transitions.values():
        presetPlaces = util.findPreset(net, t)

        presetConditions = {
                c for c in initialMarkings if c.place in presetPlaces}

        if len(presetConditions) == len(presetPlaces):
            newEvent = Event(t, presetConditions)

