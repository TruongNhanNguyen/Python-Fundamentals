import unittest


class TreeNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


def tree_sort(arr: list[int]) -> list[int]:
    # Construct the binary search tree
    root: TreeNode | None = None
    for val in arr:
        root = insert(root, val)

    # Perform an in-order traversal of the binary search tree
    sorted_arr: list[int] = []
    inorder_traversal(root, sorted_arr)

    return sorted_arr


def insert(root: TreeNode | None, val: int) -> TreeNode:
    # If the tree is empty, create a new node as the root
    if root is None:
        return TreeNode(val)

    # Otherwise, insert the node recursively in the appropriate subtree
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    return root


def inorder_traversal(root: TreeNode | None, sorted_arr: list[int]) -> None:
    # Perform an in-order traversal of the binary search tree
    if root is None:
        return

    inorder_traversal(root.left, sorted_arr)
    sorted_arr.append(root.val)
    inorder_traversal(root.right, sorted_arr)


class TestTreeSort(unittest.TestCase):
    def test_empty_list(self):
        arr: list[int] = []
        expected_result: list[int] = []
        self.assertEqual(tree_sort(arr), expected_result)

    def test_single_element_list(self):
        arr: list[int] = [1]
        expected_result: list[int] = [1]
        self.assertEqual(tree_sort(arr), expected_result)

    def test_two_element_unsorted_list(self):
        arr: list[int] = [2, 1]
        expected_result: list[int] = [1, 2]
        self.assertEqual(tree_sort(arr), expected_result)

    def test_two_element_sorted_list(self):
        arr: list[int] = [1, 2]
        expected_result: list[int] = [1, 2]
        self.assertEqual(tree_sort(arr), expected_result)

    def test_multiple_element_unsorted_list(self):
        arr: list[int] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        expected_result: list[int] = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        self.assertEqual(tree_sort(arr), expected_result)

    def test_repeated_element_list(self):
        arr: list[int] = [1, 1, 1, 1, 1, 1]
        expected_result: list[int] = [1, 1, 1, 1, 1, 1]
        self.assertEqual(tree_sort(arr), expected_result)

    def test_already_sorted_list_ascending_order(self):
        arr: list[int] = [1, 2, 3, 4, 5]
        expected_result: list[int] = [1, 2, 3, 4, 5]
        self.assertEqual(tree_sort(arr), expected_result)

    def test_already_sorted_list_descending_order(self):
        arr: list[int] = [5, 4, 3, 2, 1]
        expected_result: list[int] = [1, 2, 3, 4, 5]
        self.assertEqual(tree_sort(arr), expected_result)


if __name__ == "__main__":
    unittest.main()
