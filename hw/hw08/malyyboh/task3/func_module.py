def calculate_area_rectangle(L, w):
    """
    Calculates the area of a rectangle

    Args:
        L (int, float): length
        w (int, float): width

    Returns:
        int, float: area of a rectangle
    """
    return f"Area of rectangle: {L * w}"


def calculate_area_triangle(b, h):
    """
    Calculates the area of a triangle

    Args:
        b (int, float): base
        h (int, float): height

    Returns:
        float: area of a triangle
    """
    return f"Area of triangle: {0.5 * b * h}"


def calculate_area_circle(r, pi, pow_r):
    """
    Calculates the area of a circle

    Args:
        r (int, float): radius
        pi (int, float): pi
        pow_r (int, float): radius raised to power 2.

    Returns:
        float: area of a circle
    """

    return f"Area of circle: {pi * pow_r}"
