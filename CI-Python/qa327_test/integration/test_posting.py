import pytest
from seleniumbase import BaseCase

from unittest.mock import patch

from qa327_test.conftest import base_url
from qa327.models import User
from werkzeug.security import generate_password_hash
from datetime import date, timedelta

test_user = User(
    email='user@domain.com',
    name='test user',
    password=generate_password_hash('Password!1'),
    balance=5000
)

dateTime = date.today()
dateTime = dateTime + timedelta(days=10)
future_date = dateTime.strftime("%Y\t%m%d")
format_date = dateTime.strftime("%Y-%m-%d")


@pytest.mark.usefixtures('server')
#@patch('qa327.backend.get_user', return_value=test_user)
class IntegrationPostingTest(BaseCase):

    def register(self):
        """register new user"""
        self.open(base_url + '/register')
        self.type("#email", "test0@test.com")
        self.type("#name", "test0")
        self.type("#password", "Test0000#")
        self.type("#password2", "Test0000#")
        self.click('input[type="submit"]')

    def login(self):
        """ Login to Swag Labs and verify that login was successful. """
        self.open(base_url + '/login')
        self.type("#email", "test0@test.com")
        self.type("#password", "Test0000#")
        self.click('input[type="submit"]')


    def test_posting(self, *_):
        """
        Test that user can post a ticket for sale, using full system from login through logout
        """
        self.register()
        self.login()
        self.open(base_url)
        self.assert_element("#welcome-header")
        self.assert_text("Welcome test0", "#welcome-header")
        # log in patched user
        # post a ticket for sale
        self.type("#sell_ticket_name", "PostingTestTicket")
        self.type("#sell_num_tickets", "15")
        self.type("#sell_ticket_price", "15")
        self.type("#sell_ticket_date", future_date)  # use date that is ahead of today's date
        self.click('input[id="sell_btn-submit"]')
        x='PostingTestTicket%15%15%' + format_date + '%user@domain.com'
        # Check for posted ticket in table
        self.driver.find_element_by_id('PostingTestTicket%15%15%' + format_date + '%user@domain.com')

        # check that url is /sell
        self.assertEqual(self.get_current_url(), base_url + "/sell")

        # logout
        self.open(base_url + '/logout')
