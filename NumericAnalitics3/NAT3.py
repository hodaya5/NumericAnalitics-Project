import numpy as np

def linear_interpolation(table_points, point):
    result = 0
    flag = True

    for i in range(len(table_points) - 1):
        x1, y1 = table_points[i]
        x2, y2 = table_points[i + 1]
        if x1 <= point <= x2:
            # נוסחת האינטרפולציה הלינארית
            result = y1 + ((y2 - y1) / (x2 - x1)) * (point - x1)
            print(f"The approximation (interpolation) of the point {point} is: {round(result, 4)}")
            flag = False
            break

    if flag:
        print("The point is outside the interpolation range.")
    return result


def polynomial_method(table_points, x):
    n = len(table_points)
    x_vals, y_vals = zip(*table_points)

    matrix = np.vander(x_vals, increasing=True)
    b = np.array(y_vals).reshape(-1, 1)

    coefficients = np.linalg.solve(matrix, b)

    print("The matrix is:")
    print(matrix)
    print("\nb vector is:")
    print(b)

    result = sum(coefficients[i][0] * (x ** i) for i in range(n))

    polynomial = " + ".join([f"({coefficients[i][0]:.4f}) * x^{i}" for i in range(n)])
    print(f"\nThe polynomial is:\n{polynomial}")
    print(f"\nThe approximation of the point {x} is: {round(result, 4)}")
    return result


def main_func():
    table_points = [(0, 0), (1, 0.8415), (2, 0.9093), (3, 0.1411), (4, -0.7568), (5, -0.9589), (6, -0.2794)]
    x = 1.28

    print(f"Table Points: {table_points}\nFinding an approximation to the point {x}\n\nLinear:")
    linear_interpolation(table_points, x)
    print("\nPolynomial:")
    polynomial_method(table_points, x)


main_func()
