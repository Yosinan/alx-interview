#!/usr/bin/python3
"""Pascal's Triangle"""

def pascal_triangle(n):
    triangle = []

    for i in range(n):
        row = []
        
        if n <= 0:
            return triangle
        for j in range(i + 1):
            if j == 0 or j == i:
                # the first and last elements in each row are always 1
                row.append(1)
            else:
                # calculate the value based on the sum of the two numbers above
                value = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(value)
        
        triangle.append(row)
    
    return triangle