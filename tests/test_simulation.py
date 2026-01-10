import unittest
from data_simulation.sensor import generate_sensor_data
from data_simulation import config

class TestSensorSimulation(unittest.TestCase):
    
    def test_data_structure(self):
        """Test if the generated data has all required keys."""
        data = generate_sensor_data(1)
        self.assertIn('sensor_id', data)
        self.assertIn('temperature', data)
        self.assertIn('vibration', data)
        self.assertIn('timestamp', data)

    def test_value_ranges(self):
        """Test if values fall within the configured min/max."""
        data = generate_sensor_data(1)
        self.assertTrue(config.MIN_TEMP <= data['temperature'] <= config.MAX_TEMP)
        self.assertTrue(config.MIN_VIBRATION <= data['vibration'] <= config.MAX_VIBRATION)

if __name__ == '__main__':
    unittest.main()