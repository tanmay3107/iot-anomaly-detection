import json
import os
from jsonschema import validate, ValidationError

# Get the absolute path to the schema file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMA_PATH = os.path.join(BASE_DIR, 'schemas', 'sensor_schema.json')

def load_schema():
    """Loads the JSON schema from file."""
    with open(SCHEMA_PATH, 'r') as f:
        return json.load(f)

# Load it once when the module starts
SENSOR_SCHEMA = load_schema()

def validate_data(data):
    """
    Validates a dictionary against the sensor schema.
    Returns True if valid, raises ValidationError if invalid.
    """
    try:
        validate(instance=data, schema=SENSOR_SCHEMA)
        return True
    except ValidationError as e:
        print(f"❌ Validation Error: {e.message}")
        return False