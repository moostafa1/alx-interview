#!/usr/bin/python3

def pascal_triangle(n):
    triangle = []

    if n <= 0:
        return []

    for r in range(n):
        coef = 1
        row = []
        for c in range(r + 1):
            row.append(coef)
            coef = coef * (r - c) // (c + 1)
        triangle.append(row)
    return triangle