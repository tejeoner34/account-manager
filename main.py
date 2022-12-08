## Program to manage bank accounts (deposit, withdraw, create accounts...)


class Client:
    def __init__(self, name, surname, account_number, balance):
        self.name = name
        self.surname = surname
        self.account_number = account_number
        self.balance = balance

    def withdraw(self):
        quantity = int(input('Insert quantity: '))
        if quantity > self.balance:
            print('There is not enough balance')
            return False
        else:
            self.balance -= quantity
            return quantity

    def deposit(self):
        quantity = int(input('Insert quantity: '))
        self.balance += quantity


def init():
    print('Create new client data')
    name = input('Insert name: ')
    surname = input('Insert surname: ')
    account_number = input('Insert account number: ')
    balance = int(input('Insert balance: '))
    user = create_user(name, surname, account_number, balance)
    app_loop(user)


def create_user(name, surname, account, balance):
    new_user = Client(name, surname, account, balance)
    print(new_user)
    return new_user


def app_loop(user):
    actions = [
        {
            'id': 1,
            'name': 'Withdraw',
            'function': user.withdraw
        },
        {
            'id': 2,
            'name': 'Deposit',
            'function': user.deposit
        },
        {
            'id': 3,
            'name': 'Finish',
            'function': ''
        }
    ]
    ##Option with if statements
    # while True:
    #     print_options(actions)
    #     option_selected = int(input('Choose one: '))
    #     if option_selected == 1:
    #         user.withdraw(int(input('Insert quantity: ')))
    #     elif option_selected == 2:
    #         user.deposit(int(input('Insert quantity: ')))
    #     else:
    #         break
    #     print(f'Current balance is {user.balance}')

    ## Without depending on if statements
    while True:
        print_options(actions)
        option_selected = int(input('Choose one: '))
        if option_selected == len(actions):
            break
        actions[option_selected - 1]['function']()
        print(f'Current balance is {user.balance}')


def print_options(options):
    for option in options:
        print(f"{option['id']}: {option['name']}\n")



## We initiate the app
init()
