from time import sleep
import os

class Client:
    """Class representing a user client.

    Attributes:
        min_len_password (int): Minimum length required for a password.
        forbidden_name_len (int): Length of a name that is considered forbidden.

    Methods:
        __init__(self, name, password): Constructor method to initialize a Client object.

    """
    min_len_password = 8
    forbidden_name_len = 0

    def __init__(self, name, password):
        """Initializes a Client object.

        Args:
            name (str): The name of the client.
            password (str): The password for the client.

        Raises:
            ValueError: If the length of the name is equal to the forbidden_name_len.

        """
        self._name = name
        self._password = password

    @property
    def name(self):
        """Getter method for the client's name.

        Returns:
            str: The name of the client.

        """
        return self._name

    @name.setter
    def name(self, new_name):
        """Setter method for the client's name.

        Args:
            new_name (str): The new name for the client.

        Raises:
            ValueError: If the length of the new_name is equal to forbidden_name_len.

        """
        if len(new_name) == Client.forbidden_name_len:
            raise ValueError('The user name is required!')
        self._name = new_name.title()

    @property
    def password(self):
        """Getter method for the client's password.

        Returns:
            str: The password of the client.

        """
        return self._password

    @password.setter
    def password(self, new_password):
        """Setter method for the client's password.

        Args:
            new_password (str): The new password for the client.

        Raises:
            ValueError: If the length of new_password is less than min_len_password.

        """
        if len(new_password) < Client.min_len_password:
            raise ValueError(f'Password needs to be more than or equal to {Client.min_len_password}')
        self._password = int(new_password)

    def __repr__(self):
        return f'Client name: {self._name}\nClient password: {self._password}'

def clear_terminal():
    operational_system = os.name

    if operational_system == 'posix':
        os.system('clear')

    elif operational_system == 'nt':
        os.system('cls')
    else:
        print("It was not possible determine the operational system. It was not possible clear the terminal.")

def show_help_message():
    print('*' * 90)
    print('COMMANDS')
    print('1"help" ---> it shows the available commands.')
    print('2"create user" ---> Creates an user, it takes user name and password.')
    print('3"see data ---> Allows you to see the last data stored."')
    print('4"change data ---> it allows you to change the data. it takes: "name" or "password."')
    print('5"quit ---> it stops the program."')
    print('6"clear ---> it clear the terminal."')
    print('*' * 90)

while True:
    user_command_terminal = str(input('command: '))

    if user_command_terminal == 'create user':
        user_name = str(input('Type the user name: '))

        if user_name.isnumeric():
            print('Error. Only letters.')
            continue

        user_password = str(input('Type user password: '))
        new_client = Client(user_name.title(), user_password)

    elif user_command_terminal == 'see data':
        try:
            print(new_client)
        except (NameError):
            print('There is no data stored')
            continue

    elif user_command_terminal == 'change data':
        choose_user_data = str(input('Which data you wanna change: '))

        if choose_user_data == 'name':
            new_name = str(input('Type new name: '))
            try:
                new_client.name = new_name
                sleep(0.5)
                print('Name changed.')
            except NameError:
                print('Please, first create an user.')
                continue

        elif choose_user_data == 'password':
            new_password = str(input('Type new password: '))
            try:
                new_client.password = new_password
                sleep(0.5)
                print('password changed.')
            except NameError:
                print('Please, first create an user.')

    elif user_command_terminal == 'clear':
        clear_terminal()

    elif user_command_terminal == 'help':
        show_help_message()

    elif user_command_terminal == 'quit':
        print('Bye...')
        break