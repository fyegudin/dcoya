import json
from jsonschema import validate, ValidationError


def validate_json_data(json_file, schema):
    # Read the JSON data from the file
    with open(json_file, 'r') as file:
        json_data = json.load(file)

    # Validate the JSON data against the schema
    try:
        validate(instance=json_data, schema=schema)
        print("JSON data is valid.")
    except ValidationError as e:
        print("Validation error(s) found:")
        print(e)
        return False

    return True


def main():
    # Define the JSON schema
    schema = {
        "type": "object",
        "properties": {
            "user_name": {"type": "string"},
            "password": {"type": "string"},
            "length": {"type": "integer"}
        },
        "required": ["user_name", "password", "length"],
        "additionalProperties": False
    }

    # Path to the JSON file to be validated
    json_file = "data.json"

    # Perform data validation
    validate_json_data(json_file, schema)


if __name__ == "__main__":
    main()
