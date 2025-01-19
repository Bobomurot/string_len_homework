def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    n = len(s)
    if n % 2 == 1:
        return s[n // 2]
    else:
        return s[n // 2 - 1:n // 2 + 1]