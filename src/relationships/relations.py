from unfolder.processor import Processor
from unfolder.condition import Condition
import configurations.config


def causalUpdaterPre(condition, event):
    Processor.causal_relation_pre.add((condition, event))


def causalUpdaterPost(condition, event):
    Processor.causal_relation_post.add((event, condition))


def addConflict(event1, event2):
    Processor.conflict_relation.add((event1, event2))
    Processor.conflict_relation.add((event2, event1))


def updateConflictRelation(event):
    for e in Processor.events:
        if e is event:
            continue

        if (event, e) in Processor.conflict_relation or (
            e,
            event,
        ) in Processor.conflict_relation:
            continue

        if not event.postset_conditions.isdisjoint(e.preset_conditions):
            addConflict(event, e)

        for c in event.preset_conditions:
            if c.event and (
                (c.event, e) in Processor.conflict_relation
                or (e, c.event) in Processor.conflict_relation
            ):
                addConflict(event, e)
                break


def isCausal(x, y):
    x_event = x.event if isinstance(x, Condition) else x
    y_event = y.event if isinstance(y, Condition) else y

    if x_event is None or y_event is None:
        return False

    if x_event is y_event:
        return False

    visited = set()
    stack = [x_event]

    while stack:
        node = stack.pop()

        if node == y_event:
            return True

        if node in visited:
            continue

        visited.add(node)

        producedConditions = {
            cond for (e, cond) in Processor.causal_relation_post if e is node
        }

        successorEvents = {
            ev2
            for (cond2, ev2) in Processor.causal_relation_pre
            if cond2 in producedConditions
        }

        stack.extend(successorEvents)

    return False


def isConcurrent(x, y):
    if x is y:
        return False

    x_event = x.event if isinstance(x, Condition) else x
    y_event = y.event if isinstance(y, Condition) else y

    if x_event is None and y_event is None:
        return True

    if x_event is None or y_event is None:
        if x_event is None:
            if x in y_event.preset_conditions:
                return False
            config_y = configurations.config.localConfiguration(y_event)
            for ancestorEvent in config_y:
                if x in ancestorEvent.preset_conditions:
                    return False
            return True
        else:
            if y in x_event.preset_conditions:
                return False
            config_x = configurations.config.localConfiguration(x_event)
            for ancestorEvent in config_x:
                if y in ancestorEvent.present_conditions:
                    return False
            return True

    if isCausal(x_event, y_event) or isCausal(y_event, x_event):
        return False

    if (x_event, y_event) in Processor.conflict_relation or (
        y_event,
        x_event,
    ) in Processor.conflict_relation:
        return False

    return True
