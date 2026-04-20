# Pre-order traversal
"""Module"""
def pre_order(node):
    """pre"""
    if not node:
        return []
    return [node.data] + pre_order(node.left) + pre_order(node.right)

# In-order traversal
def in_order(node):
    """in"""
    if not node:
        return []
    return in_order(node.left) + [node.data] + in_order(node.right)

# Post-order traversal
def post_order(node):
    """post"""
    if not node:
        return []
    return post_order(node.left) + post_order(node.right) + [node.data]
