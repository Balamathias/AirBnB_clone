# AirBnB Clone Project

Welcome to the AirBnB clone project! This project aims to build a simplified version of the AirBnB web application, focusing on various aspects such as object management, serialization/deserialization, and storage.

## Project Structure

- `models/`: Contains the classes for AirBnB objects (BaseModel, User, State, City, Place, Amenity, Review).
- `models/engine/`: Includes the storage engine for serialization/deserialization (FileStorage).
- `tests/`: Contains unittests for the project.
- `console.py`: The command-line interface for managing AirBnB objects.

## BaseModel Class

- `id`: A unique identifier for each instance.
- `created_at`: The datetime when an instance is created.
- `updated_at`: The datetime when an instance is updated.
- `save()`: Updates the `updated_at` attribute with the current datetime.
- `to_dict()`: Returns a dictionary containing all keys/values of the instance.

## FileStorage Class

- Manages serialization and deserialization of instances to/from a JSON file.
- `all()`: Returns the dictionary of all objects.
- `new(obj)`: Adds a new object to the dictionary.
- `save()`: Serializes the objects to a JSON file.
- `reload()`: Deserializes the JSON file to objects.

## HBNBCommand Class (console.py)

- Implements a command interpreter using the `cmd` module.
- Supports commands like `quit`, `help`, `create`, `show`, `destroy`, `all`, `update`, and more.
- Provides a custom prompt: `(hbnb)`

## Unit Tests

- `tests/`: Contains unittests for the project.
- Use `python3 -m unittest discover tests` to run all tests.

## Execution

- To run the console in interactive mode: `$ ./console.py`
- To run the console in non-interactive mode: `$ echo "help" | ./console.py`

## Requirements

- Python 3.8.5
- pycodestyle 2.8.*
- All modules, classes, and functions should have proper documentation.
- All files must be executable.

## Contributors

- [Adegboyega Ademola]
- [Mathias Bala]

