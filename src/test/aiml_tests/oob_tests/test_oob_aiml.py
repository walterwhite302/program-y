import unittest
import os

from test.aiml_tests.client import TestClient
from programy.config.sections.brain.oob import BrainOOBConfiguration

class OOBTestClient(TestClient):

    def __init__(self):
        TestClient.__init__(self)

    def load_configuration(self, arguments):
        super(OOBTestClient, self).load_configuration(arguments)
        self.configuration.brain_configuration.files.aiml_files._files = os.path.dirname(__file__)
        default = BrainOOBConfiguration("default")
        default._classname = "programy.utils.oob.default.DefaultOutOfBoundsProcessor"
        self.configuration.brain_configuration.oob._default = default

class OOBAIMLTests(unittest.TestCase):

    def setUp(self):
        OOBAIMLTests.test_client = OOBTestClient()

    def test_oob_one_word(self):
        response = OOBAIMLTests.test_client.bot.ask_question("test",  "HELLO")
        self.assertEqual(response, "<oob>HELLO, WORLD</oob>")

    def test_oob_complex(self):
        response = OOBAIMLTests.test_client.bot.ask_question("test",  "FILE BUG REPORT")
        self.assertEqual(response, "To help the developers blah blah blah <oob><dialog><title>Would you like to send a bug report?</title> <list><item>Yes</item> <item>No</item></list></dialog></oob>")
