import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.read_config import read_config, connect_to_database

class TestReadConfig(unittest.TestCase):

    def test_read_config(self):
        config_file_path = os.path.join(os.getcwd(),
                                        str.format('config\\{0}.yaml', 'source'))
        config = read_config(config_file_path)
        self.assertIsNotNone(config)
        self.assertIsInstance(config, dict)
    
    
    def test_connect_to_database(self):
        config_file_path = os.path.join(os.getcwd(), 'config', 'source.yaml')
        config = read_config(config_file_path)
        connection = connect_to_database(config)
        self.assertIsNotNone(connection)
        # Add more assertions based on the expected behavior of connect_to_database
        # For example, if it returns a connection object, you might check its type
        # self.assertIsInstance(connection, ExpectedConnectionType)

if __name__ == '__main__':
    unittest.main()