# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def is_balanced(root):
    if root is None:
        return True, None, None

    balanced_left, min_left, max_left = is_balanced(root.left)
    balanced_right, min_right, max_right = is_balanced(root.right)

    is_balanced_node = (balanced_left and balanced_right and
                        (max_left is None or root.value > max_left) and
                        (min_right is None or root.value < min_right))

    min_value = min([x for x in [min_left, root.value, min_right] if x is not None])
    max_value = max([y for y in [max_left, root.value, max_right] if y is not None])

    return is_balanced_node, min_value, max_value


def solution(root) -> bool:
    return is_balanced(root)[0]


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


if __name__ == '__main__':
    test()
