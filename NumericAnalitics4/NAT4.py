"""
Hodaya Bruchim 325249639
Or Farkash 314920984
Shaked Asayag 322490293
"""

def lagrange_interpolation(table_points, x):
    """
    Lagrange Interpolation Method
    :param table_points: List of (x, y) tuples
    :param x: Point to evaluate
    :return: Interpolated value at x
    """
    xList = [point[0] for point in table_points]
    yList = [point[1] for point in table_points]

    if x in xList:
        index = xList.index(x)
        return yList[index]

    if not (min(xList) <= x <= max(xList)):
        print("The given x value is outside the range of xList.")
        return None

    n = len(xList)
    p_x = 0
    for i in range(n):
        # Calculate L_i(x)
        L_i = 1
        for j in range(n):
            if i != j:
                L_i *= (x - xList[j]) / (xList[i] - xList[j])
        p_x += yList[i] * L_i

    print(f"The interpolated value at x = {x} is: {p_x}")
    return p_x

def neville_interpolation(table_points, x):
    """
    Neville's Method for Interpolation
    :param table_points: List of (x, y) tuples
    :param x: Point to evaluate
    :return: Interpolated value at x
    """

    xList = [point[0] for point in table_points]
    yList = [point[1] for point in table_points]

    if x in xList:
        index = xList.index(x)
        return yList[index]

    if not (min(xList) <= x <= max(xList)):
        print("The given x value is outside the range of xList.")
        return None

    n = len(xList)
    temp_table = [[xList[i], yList[i]] for i in range(n)]

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            temp_table[i][1] = ((x - temp_table[i - j][0]) * temp_table[i][1] - (x - temp_table[i][0]) * temp_table[i - 1][1]) / (temp_table[i][0] - temp_table[i - j][0])


    result = temp_table[n - 1][1]
    print(f"The interpolated value at x = {x} is: {result}")
    return result

def main_func():
    # Define table points and x
    table_points = [(0, 0), (1, 0.8415), (2, 0.9093), (3, 0.1411), (4, -0.7568), (5, -0.9589), (6, -0.2794)]
    x = 1.28

    print(f"Table Points: {table_points}\nFinding an approximation to the point {x}\n\nLagrange:")
    lagrange_interpolation(table_points, x)
    print("\nNeville:")
    neville_interpolation(table_points, x)

main_func()
