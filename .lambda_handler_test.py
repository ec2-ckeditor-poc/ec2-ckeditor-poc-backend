import sys
print(sys.path)

import unittest
from unittest.mock import patch

from lambda_handler import lambda_handler

class TestLambdaFunction(unittest.TestCase):

    @patch('lambda_function.boto3')
    def test_lambda_handler(self, mock_boto3):
        # Set up mock DynamoDB client and response
        mock_table = mock_boto3.resource.return_value.Table.return_value
        mock_table.update_item.return_value = {
            'Attributes': {'visitor_count': 5}  # Sample response
        }

        # Mock the environment variable
        with patch.dict('os.environ', {'TABLE_NAME': 'YourTableName'}):
            # Prepare a sample event and context (these can be customized)
            event = {}
            context = {}

            # Call the lambda_handler function
            response = lambda_handler(event, context)

            # Assertions
            self.assertEqual(response['statusCode'], 200)
            self.assertEqual(
                response['body'],
                '{"visitor_count": 5}'  # Ensure the expected visitor count is returned
            )
            # Additional assertions based on your function's logic

            # Verify function calls (optional)
            mock_table.update_item.assert_called_once()

if __name__ == '__main__':
    unittest.main()
