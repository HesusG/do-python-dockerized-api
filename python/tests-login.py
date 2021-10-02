import unittest

from database import Database
from methods import Token, Restricted


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.database = Database()
        self.token = Token()
        self.restricted = Restricted()

    def test_get_user(self):
        self.assertEqual({"role": "admin"}, self.database.get_user('admin', 'secret'))

    def test_get_user_failed(self):
        self.assertEqual(None, self.database.get_user('admin', 'secret-wrong-password'))


    def test_generate_token(self):
        self.assertEqual('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4ifQ.BmcZ8aB5j8wLSK8CqdDwkGxZfFwM1X1gfAIN7cXOx9w', self.token.generate_token({'role': 'admin'}))

    def test_generate_token_failed(self):
        self.assertEqual(None, self.token.generate_token(''))


    def test_access_data(self):
        self.assertEqual('admin', self.restricted.access_data('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4ifQ.BmcZ8aB5j8wLSK8CqdDwkGxZfFwM1X1gfAIN7cXOx9w'))

    def test_access_data_failed(self):
        self.assertEqual(None, self.restricted.access_data('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0ZXN0Ijp0cnVlfQ.9dI-h6BKiikQvSPVLwJSqfWGhAgQ0F_bkugq4N6MHKI'))

if __name__ == '__main__':
    unittest.main()
