from io import StringIO
from unittest import TestCase

from virtual_ta import render_template_from_csv_file, SlackBot


# noinspection SpellCheckingInspection
class TestRenderers(TestCase):
    def test_render_template_from_csv_file_with_key(self):
        test_template = StringIO('{{First_Name}} {{Last_Name}}')
        test_expectations = {
            "auser1": "a user1",
            "buser2": "b user2",
        }
        test_gradebook_entries = [
            "User_Name,First_Name,Last_Name",
            "auser1,a,user1",
            "buser2,b,user2"
        ]
        test_gradebook = StringIO("\n".join(test_gradebook_entries))
        test_results = render_template_from_csv_file(
            test_template,
            test_gradebook,
            key="User_Name",
        )
        self.assertEqual(test_expectations, test_results)

    def test_render_template_from_csv_file_without_key(self):
        test_template = StringIO('{{First_Name}} {{Last_Name}}')
        test_expectations = {
            "auser1": "a user1",
            "buser2": "b user2",
        }
        test_gradebook_entries = [
            "User_Name,First_Name,Last_Name",
            "auser1,a,user1",
            "buser2,b,user2"
        ]
        test_gradebook = StringIO("\n".join(test_gradebook_entries))
        test_results = render_template_from_csv_file(
            test_template,
            test_gradebook,
        )
        self.assertEqual(test_expectations, test_results)


class TestSlackBots(TestCase):
    def test_set_api_token_from_file(self):
        test_token = "Test Token Value"
        test_fp = StringIO(test_token)

        test_bot = SlackBot()
        test_bot.set_api_token_from_file(test_fp)
        self.assertEqual(test_token, test_bot.api_token)
