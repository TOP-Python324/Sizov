from collections.abc import Iterable


def tree_leaves(leaves: list) -> int:
    """Считает количество листьев на дереве."""
    result = 0
    for elem in leaves:
        if elem == 'leaf':
            result += 1
        else:
            result += tree_leaves(elem)
    return result
    
    
# >>> tree = [[[['leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf', 'leaf'], 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf']], [['leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf'], ['leaf', 'leaf', ['leaf', 'leaf', 'leaf']], 'leaf', 'leaf'], ['leaf', 'leaf', ['leaf', 'leaf'], 'leaf']]
# >>>
# >>> tree_leaves(tree)
# 38
# >>> 
# >>> tree_leaves(['leaf',[]])
# 1
# >>>
# >>> tree_leaves([])
# 0
# >>>


# ИТОГ: отлично — 3/3
