import unittest
import requests
from app import app

server_address="http://127.0.0.1:5000"
SERVICE_ADDR=server_address


class FeatureTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        app.testing = True

    def test_register(self):
        req = requests.get(server_address + "/register")
        self.assertEqual(req.status_code, 200)
        print("OK")

    def test_login(self):
        req = requests.get(server_address + "/login")
        self.assertEqual(req.status_code, 200)
        print("OK")

    def test_no_login(self):
        req = requests.get(server_address + "/spell_check")
        self.assertEqual(req.status_code, 401)
        print("OK")

    def test_spell_check(self):
        req = requests.get(server_address + "/register")
        self.assertEqual(req.status_code, 200)
        uname = 'tjramlogan'
        pword = "blahblah"
        mfa = "1234567891"
        # Add register code
        # check successful
        req = requests.get(server_address + "/login")
        self.assertEqual(req.status_code, 200)
        # login
        # check successful
        print("OK")

        req = requests.get(server_address + "/spell_check")
        self.assertEqual(req.status_code, 200)


    def tearDown(self):
        pass

if __name__ == '__main__':
    
    unittest.main()


