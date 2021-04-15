class Budget:

    def __init__(self, category, balance):
        self.category = category
        self.balance = balance

    def deposit(self):
        deposit_amount = int(input('Enter the amount you want to deposit: \n'))
        self.balance += deposit_amount
        print(f'Your new balance is #{self.balance}')
        return exit()

    def withdrawal(self):
        withdrawal_amount = int(input('How much do you want to withdraw? \n'))
        if withdrawal_amount > self.balance:
            print('Insufficient Funds! Please fund your account!')
        else:
            self.balance -= withdrawal_amount
            print(f'Take your cash, your new balance is #{self.balance}')
            return exist()

    def transfer(self, transfer_money):
        print(f'Transfer from {self.category} budget')
        transfer_amount = int(input('Enter the amount you want to transfer: \n'))
        if transfer_amount >= self.balance:
            print('Insufficient Funds! Please fund your account!')
            exist()
        else:
            self.balance -= transfer_amount
            print(f'Transfer Successful: Your new {self.category} balance is #{self.balance}')
            exist()

    def get_balance(self):
        print(f"{self.category} balance: #{self.balance}")
        exist()


def food():
    print('FOOD-BUDGET')
    food1 = Budget('food', 2000)
    food_Option = input('''Please choose out of the following options
        1. Deposit
        2. Withdraw
        3. Transfer
        4. Check balance \n ''')
    if food_Option == '1':

        food1.deposit()
    elif food_Option == '2':
        food1.withdrawal()
    elif food_Option == '3':
        transfer = input('''which category would you like to transfer to?
            1.clothing
            2.Entertainment \n''')
        if transfer == '1':
            food1.transfer('clothing')
        elif transfer == '2':
            food1.transfer('Entertainment')
        else:
            print('You have selected an invalid option')
    elif food_Option == '4':
        food1.get_balance()
    else:
        print('You have selected an invalid option')
        welcome()


def clothing():
    print('CLOTHING BUDGET')
    clothing1 = Budget('clothing', 5000)
    clothing_Option = input('''You have the following options
        1. Deposit
        2. withdraw
        3. Transfer
        4. Check balance \n ''')
    if clothing_Option == '1':
        clothing1.Deposit()
    elif clothing_Option == '2':
        clothing1.Withdrawal()
    elif clothing_Option == '3':
        category_TO_transfer = input('''Which category would you like to transfer to?
            1.food
            2.Entertainment \n''')
        if category_TO_transfer == '1':
            clothing1.Transfer('food')
        elif category_TO_transfer == '2':
            clothing1.Transfer('Entertainment')
        else:
            print('You have selected an invalid option')
    elif clothing_Option == '4':
        clothing1.get_balance()
    else:
        print('You have selected an invalid option')
        welcome()


def entertainment():
    print('ENTERTAINMENT BUDGET')
    Entertainment = Budget('Entertainment', 7000)
    Entertainment_Option = input('''You have the following options
        1. Deposit
        2. Withdraw
        3. Transfer
        4. Check balance \n ''')
    if Entertainment_Option == '1':
        Entertainment.Deposit()
    elif Entertainment_Option == '2':
        Entertainment.Withdrawal()
    elif Entertainment_Option == '3':
        transfer_to = input('''which category would you like to transfer to?
            1.food
            2.clothing \n''')
        if transfer_to == '1':
            Entertainment.Transfer('food')
        elif transfer_to == '2':
            Entertainment.Transfer('clothing')
        else:
            print('You have selected an invalid option')
    elif Entertainment_Option == '4':
        Entertainment.get_balance()
    else:
        print('You have selected an invalid option')
        welcome()


def welcome():
    try:
        print(" WELCOME TO BUDGET APP ️")
        select_option = int(input('''What would you like to budget for?
    1. Food 
    2. Clothing 
    3. Entertainment 
    4. Exit 
    '''))
        if select_option == 1:
            food()
        elif select_option == 2:
            clothing()
        elif select_option == 3:
            entertainment()
        elif select_option == 4:
            print("Thank you for using the budget app,\n We would love to have you back again")
            exit()
    except ValueError:
        print("You have not selected any correct option")
        return welcome()


def exit():
    try:
        exit_now = int(input("""Do you want to perform another transaction? \n
    1. Yes
    2. No \n
    """))
        if exit_now == 1:
            welcome()
        elif exit_now == 2:
            print('Thank you for your patronage!!! See you next time')
        else:
            print('Invalid Option Selected, Please try again')
            welcome()
    except ValueError:
        print('<<<Enter Number>>>')
        return exit()


welcome()