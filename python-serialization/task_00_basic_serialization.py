import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes the provided Python dictionary `data` to a JSON file
    and saves it to the given `filename`. If the file already exists,
    it is overwritten.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)
    print(f"Data serialized and saved to '{filename}'.")

def load_and_deserialize(filename):
    """
    Loads and deserializes the data from a given JSON file `filename`
    and returns the Python dictionary.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
