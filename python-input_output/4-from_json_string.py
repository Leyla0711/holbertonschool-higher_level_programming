#!/usr/bin/python3
import json

def from_json_string(my_str):
    """Returns a Python object represented by a JSON string.

    Args:
        my_str: A string containing a JSON object.

    Returns:
        A Python object represented by the JSON string.

    Example:
        >>> from_json_string('[1, 2, 3]')
        [1, 2, 3]
    """
    return json.loads(my_str)
