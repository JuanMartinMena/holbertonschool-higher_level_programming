def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer, boolean) for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary representation of obj.
    """
    return obj.__dict__
