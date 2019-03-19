from math import sqrt


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None
    root1 = (-b - sqrt(discriminant)) / (2 * a)
    if discriminant == 0:
        return root1, None
    root2 = (-b + sqrt(discriminant)) / (2 * a)
    return root1, root2


if __name__ == '__main__':
    coefficient_a = 1
    coefficient_b = -2
    coefficient_c = 3
    print(get_roots(coefficient_a, coefficient_b, coefficient_c))
