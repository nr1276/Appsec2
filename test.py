import unittest
import requests

server_address="http://127.0.0.1:5000"
SERVICE_ADDR=server_address


class FeatureTest(unittest.TestCase):

    def test_server_is_alive(self):
        req = requests.get(server_address)
        self.assetEqual(req.status_code, 200)


    def test_login(self):
        req = requests.get(serer_address + "/login")
        self.assertEqual(req.status_code, 200)

    def test_page_exits(self):
        PAGES = ["/register", "/login", "/spell_check"]
        for page in PAGES:
                req = requests.get(server_address + page)
                self.assertEqual(req.status_code, 200)

    def test_no_login(self):
        req = requests.get(server_address + "spell_check")
        self.assetEqual(req.status_code, 400)

    def test_spell_check(self):
        req = requests.get(server_address + "register")
        self.assertEqual(req.status_code, 200)
        uname = 'tjramlogan'
        pword = "blahblah"
        mfa = "1234567891"
        # Add register code
        # check successful

        req = requests.get(server_address + "login")
        self.assetEqual(req.status_code, 200)
        # login
        # check successful

        req = requests.get(server_address + "spell_check")
        self.assetEqual(req.status_code, 200)




