def canUnlockAll(boxes):
    n = len(boxes)  # Number of boxes
    visited = set()  # Set to store visited boxes
    visited.add(0)  # Mark the first box as visited

    keys = boxes[0]  # Keys obtained from the first box

    while keys:
        key = keys.pop(0)  # Take a key from the list

        if key < n and key not in visited:
            visited.add(key)
            keys.extend(boxes[key])  # Add keys from the new box

    return len(visited) == n
