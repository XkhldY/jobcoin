#!/usr/bin/env python
import uuid
import sys
import click
from jobcoin.User import User
from jobcoin.jobcoin import Mixer


@click.command()
def main(args=None):
    print('Welcome to the Jobcoin mixer!\n')
    """
    """

    mixer = Mixer()
    user = User()
    while True:

        addresses = click.prompt(
            'Please enter a comma-separated list of new, unused Jobcoin '
            'addresses where your mixed Jobcoins will be sent.',
            prompt_suffix='\n[b to go back] > ',
            default='',
            show_default=False)
        if addresses.strip() == 0:
            sys.exit(0)
        user.set_deposit_address(mixer.generate_deposit_address())
        user.user_addresses = list(set(addresses.split(',')))

        click.echo(
            '\nYou may now send Jobcoins to address {deposit_address}. They '
            'will be mixed and sent to your destination addresses.\n'
              .format(deposit_address=user.deposit_address))

        print(mixer.mix(user))


if __name__ == '__main__':
    sys.exit(main())
