def add_integer(a, b=98):
  """
  Adds two integers.
  Args:
    a: The first integer.
    b: The second integer.
  Returns:
    The sum of the two integers.
  Raises:
    TypeError: If either a or b is not an integer or float.
  """
  if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
    raise TypeError("a must be an integer or b must be an integer")
  return int(a) + int(b)