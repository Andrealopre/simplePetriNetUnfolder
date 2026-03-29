from unfolder.processor import Processor

configurations_cache = {}
configLengthCache = {}


def localConfiguration(event):
    if event in configurations_cache:
        return configurations_cache[event]

    visited = set()
    stack = [event]

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)

        for c in node.preset_conditions:
            if c.event is not None:
                stack.append(c.event)

    configurations_cache[event] = visited
    return visited


def getConfigurationLength(event):
    if event in configLengthCache:
        return configLengthCache[event]

    length = len(localConfiguration(event))
    configLengthCache[event] = length
    return length
