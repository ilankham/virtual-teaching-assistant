"""Create functional tests for project using unittest module

This module assumes the file examples/token.ini exists and has a single line of
contents comprising a valid Slack Web API Token.

"""

from pprint import pprint
from unittest import TestCase

from virtual_ta import mail_merge_from_csv_file, SlackAccount


class TAWorkflowTests(TestCase):
    def test_send_slack_messages_with_csv_import(self):
        # For the intended Slack Workspace and the user account from which they
        # wish to have messages originate, Prof. X creates an API Token by
        # (1) visiting https://api.slack.com/custom-integrations/legacy-tokens
        #     and generating a Legacy Token, or
        # (2) visiting https://api.slack.com/apps and creating a new app with
        #     permission scopes for chat:write:user, im:read, and users:read

        # Prof. X saves the API Token in a text file

        # Prof. X saves a gradebook csv file named with column headings and one
        # row per student grade record

        # Prof. X saves a template text file as a Jinja2 template, with each
        # variable name a column heading in the gradebook csv file

        # Prof. X uses the mail_merge_from_csv_file method to mail merge their
        # template file against their gradebook file, returning a dictionary of
        # messages keyed by Slack user name
        with open('examples/example_template.txt') as template_fp:
            with open('examples/example_gradebook.csv') as gradebook_fp:
                mail_merge_results = mail_merge_from_csv_file(
                    template_fp, gradebook_fp, key='Slack_User_Name'
                )

        # Prof. X prints the dictionary to ensure messages are as intended
        pprint(mail_merge_results)

        # Prof. X initiates a SlackAccount object and then uses the
        # set_api_token_from_file method to load their API Token
        test_bot = SlackAccount()
        with open('examples/token.ini') as fp:
            test_bot.set_api_token_from_file(fp)

        # Prof. X then checks the SlackAccount's API Token was loaded correctly
        with open('examples/token.ini') as fp:
            self.assertEqual(fp.readline(), test_bot.api_token)

        # Prof. X uses the SlackAccount direct_message_users method to send the
        # messages in the dictionary to the indicated students
        test_bot.direct_message_by_username(mail_merge_results)

        # Prof. X then verifies in the Slack Workspace corresponding to their
        # API Token direct messages have been send with themselves as the
        # apparent sender
