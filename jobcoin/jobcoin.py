import requests
from requests.exceptions import RequestException
from random import uniform
from . import config
import uuid
from .User import User
import time


class Mixer:
    """
    main logic where we create the deposit account
    listen to the user transactions to the deposit account
    transfer user funds from deposit to the house account
    dole out the funds over the user requested addresses
    """
    def __init__(self):
        self.DELAY_TIME = 2
        self.HOUSE_ACCOUNT = 'house_account'

    @staticmethod
    def generate_deposit_address() -> str:
        """
        :return: the auto generated deposit address
        """
        return uuid.uuid4().hex

    @staticmethod
    def transfer_funds(source_address: str, target_address: str, amount: float):
        """
        :param amount: user coins to be added
        :param source_address: address where the funds located
        :param target_address:  address where the funds moving to
        :return: transaction succeed or failed
        """

        payload = {
            "amount": amount,
            "fromAddress": source_address,
            "toAddress": target_address
        }
        response = requests.post(config.API_TRANSACTIONS_URL, data=payload)

        if 'error' in response.json():
            return response.json()['error']

        elif response.status_code == 200:
            return 'funds has been added to address: ' + target_address

    @staticmethod
    def detect_transaction(address: str):
        """
        :param address: user allocated deposit address
        :return: funds once the user do the transaction
        """

        url = config.API_ADDRESS_URL + address
        while True:
            response = requests.get(url)

            if response.json()['balance'] != '0':
                return float(response.json()['balance'])

    def mix(self, user: User):
        """
        :param : User object contains the addresses and deposit address
        :return: information about the addresses after dole out the funds
        """
        coins = self.detect_transaction(user.get_deposit_address())
        try:
            self.transfer_funds(source_address=user.get_deposit_address(),
                                target_address=self.HOUSE_ACCOUNT, amount=coins)
        except RequestException as e:
            return e
        n = len(user.user_addresses)

        if coins <= 0:
            return "user doesn't have enough balance to transfer"
        elif n <= 0:
            return "user doesn't have addresses to mix"

        chucks = []
        for _ in range(n - 1):
            chucks.append(round(uniform(0, coins - sum(chucks)), 4))

        chucks.append(round(coins - sum(chucks), 4))

        assert len(chucks) == len(user.user_addresses)

        for address, chuck in zip(user.user_addresses, chucks):
            try:
                self.transfer_funds(source_address=self.HOUSE_ACCOUNT,
                                    target_address=address, amount=chuck)
                time.sleep(self.DELAY_TIME)
            except RequestException as e:
                return e

        return "the balance is distributed successfully on the user Addresses: " + \
               ' '.join(user.user_addresses)
