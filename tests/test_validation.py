import unittest
from utils.validation import validate_data

class TestSchemaValidation(unittest.TestCase):
    
    def setUp(self):
        # A valid sample
        self.valid_data = {
            "sensor_id": 1,
            "timestamp": 167888.0,
            "temperature": 25.5,
            "vibration": 100.2
        }

    def test_valid_data(self):
        """Should return True for correct data"""
        self.assertTrue(validate_data(self.valid_data))

    def test_missing_field(self):
        """Should fail if a required field is missing"""
        bad_data = self.valid_data.copy()
        del bad_data['temperature']
        self.assertFalse(validate_data(bad_data))

    def test_wrong_type(self):
        """Should fail if types are wrong (e.g., string instead of number)"""
        bad_data = self.valid_data.copy()
        bad_data['temperature'] = "Twenty Degrees"  # This is a string, schema expects number
        self.assertFalse(validate_data(bad_data))

if __name__ == '__main__':
    unittest.main()