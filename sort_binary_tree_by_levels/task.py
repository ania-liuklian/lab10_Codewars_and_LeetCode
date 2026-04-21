"""Module"""
from collections import deque
def tree_by_levels(node):
    """tree"""
    if not node:
        return []

    queue = deque()
    result = []
    queue.append(node)
    while queue:
        node = queue.popleft()
        result.append(node.value)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return result
