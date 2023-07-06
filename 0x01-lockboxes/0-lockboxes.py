#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing the boxes and their corresponding keys.
                      Each box is numbered sequentially from 0 to n - 1.

    Returns:
        bool: True if all boxes can be opened, False otherwise.

    """

    n = len(boxes)  # Number of boxes
    visited = set()  # Set to store visited boxes
    queue = [0]  # Queue to store boxes for exploration

    while queue:
        box = queue.pop(0)
        visited.add(box)

        # Check keys in the current box
        for key in boxes[box]:
            if key < n and key not in visited:
                visited.add(key)
                queue.append(key)

    return len(visited) == n
