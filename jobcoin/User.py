
class User:
    """
    user is a collection of features to save in one place the user addresses, deposit address,
    later we can add balance and other information related to particular User
    """
    def __init__(self):
        self.addresses = None
        self.deposit_address = None

    @property
    def user_addresses(self):
        return self.addresses

    @user_addresses.setter
    def user_addresses(self, addresses):
        self.addresses = addresses

    def get_deposit_address(self):
        if not self.deposit_address:
            raise ValueError('no deposit address assigned yet please add new addresses first')
        return self.deposit_address

    def set_deposit_address(self, deposit_address):
        self.deposit_address = deposit_address
