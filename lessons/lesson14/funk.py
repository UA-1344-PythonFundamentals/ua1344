import math


def solve_quadratic_equation(a, b, c):
    """
    Solves a quadratic equation of the form ax^2 + bx + c = 0.

    Args:
      a: The coefficient of x^2.
      b: The coefficient of x.
      c: The constant term.

    Returns:
      A tuple containing the roots of the equation (x1, x2).
      Returns None if there are no real roots.
    """
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        return None  # No real roots
    elif discriminant == 0:
        x = -b / (2 * a)
        return (x, x)  # One real root (or two equal roots)
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (x1, x2)  # Two distinct real roots


