from unfolder.condition import Condition
from unfolder.event import Event
import relationships.relations
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
            postsetPlaces = util.findPostset(net, t)

            for p in postsetPlaces:
                newCondition = Condition(p, newEvent)
                newEvent.postset_conditions.add(newCondition)

            initialExtensions.add(newEvent)

    return initialExtensions


def updatePotExt(net, unf, event):
    extensions = set()

    u = event.transition

    postPlaces = util.findPostset(net, u)
    successiveTransitions = util.findSuccTransitions(net, postPlaces)
    presetPlaces = util.findPreset(net, u)

    difference = presetPlaces - postPlaces
    postDifference = util.findDifference(net, difference)

    transitions = successiveTransitions - postDifference

    for t in transitions:
        preset = util.findPreset(net, t)
        C = {
            c
            for c in unf
            if isinstance(c, Condition)
            and c.place in preset
            and relationships.relations.isConcurrent(c, event)
        }

        extensions |= cover(C, t, dict(), net)

    return extensions


def cover(C, t, preset, net):
    preset_t = util.findPreset(net, t)
    extensions = set()

    if len(preset_t) == len(preset):
        inputConditions = {preset[p] for p in preset_t}

        conditionsList = list(inputConditions)
