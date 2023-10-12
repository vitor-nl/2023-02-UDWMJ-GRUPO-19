import Client
import Socialnetwork
class Client_socialnetwork(Client.Client, Socialnetwork.Socialnetwork):
    def __init__(self, first_name, last_name, address, cell_phone, email, gender, name, description):
        super(Client, self).__init__(first_name, last_name, address, cell_phone, email, gender)
        super(Socialnetwork, self).__init__(id, name, description)