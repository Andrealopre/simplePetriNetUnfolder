def findPreset(net, transition):
    preset = set()

    for arc in net.arcs:
        if arc.dst == transition:
            preset.add(arc.src)

    return preset


def findPostset(net, transition):
    postPlaces = set()

    for arc in net.arcs:
        if arc.src == transition:
            postPlaces.add(arc.dst)

    return postPlaces


def findSuccTransitions(net, post_places):
    succ_transitions = set()

    for arc in net.arcs:
        for p in post_places:
            if arc.src == p:
                succ_transitions.add(arc.dst)

    return succ_transitions


def findDifference(net, difference):
    postDifference = set()

    for arc in net.arcs:
        for p in difference:
            if arc.src == p:
                postDifference.add(arc.dst)

    return postDifference
