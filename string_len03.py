def main(a,b):
    """
    String type variables a and b are given. Return True if the length is equal. If not equal, return False.
    Args:
        a: string
        b: string
    Returns:
        True or False
    """
    a1 = len(a)
    b1 = len(b)
    if a1 == b1:
        return True
    else:
        return False