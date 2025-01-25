"""
Hodaya Bruchim 325249639
Or Farkash 314920984
Shaked Asayag 322490293
"""
import numpy as np

def spline_cubic(table_points, point):
    """
    Cubic Spline Interpolation Method
    :param table_points: List of (x, y) tuples
    :param point: Point to evaluate
    :return: Tuple with natural spline and full spline cubic results
    """
    xList = [p[0] for p in table_points]
    yList = [p[1] for p in table_points]

    n = len(xList) - 1

    # Step 1: Create h_list
    h_list = [xList[i + 1] - xList[i] for i in range(n)]

    # Step 2: Create lambda_list, mu_list, and d_list
    lambda_list = [h_list[i + 1] / (h_list[i] + h_list[i + 1]) for i in range(n - 1)]
    mu_list = [1 - lambda_list[i] for i in range(n - 1)]
    d_list = [
        (6 / (h_list[i] + h_list[i + 1])) * \
        ((yList[i + 2] - yList[i + 1]) / h_list[i + 1] - (yList[i + 1] - yList[i]) / h_list[i])
        for i in range(n - 1)
    ]

    # Step 3: Create the natural spline matrix and solution vector
    A = np.zeros((n + 1, n + 1))
    b = np.zeros(n + 1)

    A[0, 0], A[n, n] = 1, 1
    b[0], b[n] = 0, 0

    for i in range(1, n):
        A[i, i - 1] = mu_list[i - 1]
        A[i, i] = 2
        A[i, i + 1] = lambda_list[i - 1]
        b[i] = d_list[i - 1]
    M_natural = np.linalg.solve(A, b)

    # Step 4: Full spline cubic conditions
    fTag0 = 0.5  # Default value for the derivative at the first point
    fTagN = -0.5  # Default value for the derivative at the last point
    b[0] = (6 / h_list[0]) * ((yList[1] - yList[0]) / h_list[0] - fTag0)
    b[n] = (6 / h_list[-1]) * (fTagN - (yList[n] - yList[n - 1]) / h_list[-1])

    M_full = np.linalg.solve(A, b)

    # Step 5: Find the appropriate interval for point
    for i in range(n):
        if xList[i] <= point <= xList[i + 1]:
            # Natural spline cubic result
            h = h_list[i]
            a = (M_natural[i + 1] - M_natural[i]) / (6 * h)
            b = M_natural[i] / 2
            c = (yList[i + 1] - yList[i]) / h - (M_natural[i + 1] + 2 * M_natural[i]) * h / 6
            d = yList[i]
            natural_result = a * (point - xList[i])**3 + b * (point - xList[i])**2 + c * (point - xList[i]) + d

            # Full spline cubic result
            a = (M_full[i + 1] - M_full[i]) / (6 * h)
            b = M_full[i] / 2
            c = (yList[i + 1] - yList[i]) / h - (M_full[i + 1] + 2 * M_full[i]) * h / 6
            d = yList[i]
            full_result = a * (point - xList[i])**3 + b * (point - xList[i])**2 + c * (point - xList[i]) + d

            return natural_result, full_result

    print("The given point is outside the range of xList.")
    return None, None

def main_func():
    # Define table points and point
    table_points = [(0, 0), (1, 0.8415), (2, 0.9093), (3, 0.1411), (4, -0.7568), (5, -0.9589), (6, -0.2794)]
    point = 1.28

    natural_result, full_result = spline_cubic(table_points, point)
    print(f"Table Points: {table_points}\nFinding an approximation to the point {point}\n")
    print(f"Natural Cubic Spline:\nThe interpolated value at x = {point} is {natural_result:.4f}\n")
    print(f"Full Cubic Spline:\nThe interpolated value at x = {point} is {full_result:.4f}")


main_func()
