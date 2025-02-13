import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Displays the object attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the current instance of the object and saves it to the given filename."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            print(f"Object successfully serialized to {filename}")
        except Exception as e:
            print(f"Error during serialization: {e}")

    @classmethod
    def deserialize(cls, filename):
        """Deserializes the object from the given filename."""
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            return obj
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"Error during deserialization: {e}")
            return None
