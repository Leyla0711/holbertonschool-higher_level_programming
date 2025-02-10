#!/usr/bin/python3
import json

def to_json_string(my_obj):
    """Returns the JSON representation of a Python object as a string.

    Args:
        my_obj: The Python object to be converted to a JSON string.

    Returns:
        A JSON string representation of the input object.

    Example:
        >>> to_json_string([1, 2, 3])
        '[1, 2, 3]'
    """
    return json.dumps(my_obj)
