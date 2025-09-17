from typing import List, Tuple

def take_next(queue: List[str]) -> Tuple[str | None, List[str]]:
    if not queue:
        return (None, [])
    return (queue[0], queue[1:])


def move_to_back(queue: List[str], name: str) -> List[str]:
    if name not in queue:
        return queue.copy()  # return a new list
    new_queue = queue.copy()
    new_queue.remove(name)
    new_queue.append(name)
    return new_queue


def interleave(q1: List[str], q2: List[str]) -> List[str]:
    result = []
    len1, len2 = len(q1), len(q2)
    for i in range(max(len1, len2)):
        if i < len1:
            result.append(q1[i])
        if i < len2:
            result.append(q2[i])
    return result
