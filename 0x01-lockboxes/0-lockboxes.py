def canUnlockAll(boxes):
    n = len(boxes)  # no of boxes
    visited = set()  # set to store visited boxes
    queue = [0]  # Queue to store boxes for checking

    while queue:
        box = queue.pop(0)
        visited.add(box)

        # Check keys in the current box
        for key in boxes[box]:
            if key < n and key not in visited:
                visited.add(key)
                queue.append(key)

    return len(visited) == n
