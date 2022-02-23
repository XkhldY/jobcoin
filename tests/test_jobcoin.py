#!/usr/bin/env python
import pytest
from jobcoin.User import User
from jobcoin.jobcoin import Mixer
from requests.exceptions import RequestException
import re
from click.testing import CliRunner

import cli
from jobcoin import config


@pytest.fixture
def response():
    import requests
    return requests.get('https://jobcoin.gemini.com/')


def test_content(response):
    assert b'Hello!' in response.content


def test_user_deposit_address():
    user = User()
    with pytest.raises(ValueError):
        user.get_deposit_address()


def test_transfer_fund_exception():
    mixer = Mixer()
    config.API_TRANSACTIONS_URL = 'failed_test'
    with pytest.raises(RequestException):
        mixer.transfer_funds('source_test', 'target_test', 0.0)
