import logging
from configparser import ConfigParser


DOC_PATH = "E:\\python\\anaconda\\python_fullstack\\day18\\ATM\\doc"



def login_defunc(func):
    def inner():
        account = input("Enter your account:")
        password = input("Enter your password:")
        func(account,password)
        # return func(account,password)
    return inner


@login_defunc

def user_login(account,password):
    account_file = DOC_PATH + "\\account_info\\" + account + '_info'
    config = ConfigParser()
    config.read(account_file)
    # config_group = config.sections()[0]
    # print(str(config[account]['PASSWORD']))
    if password == config[account]['PASSWORD']:
        print("Welcome %s !" % account)
        return True
    else:
        print("Wrong password!")
        return False
    # return test


@login_defunc
def admin_login(account,password):
    account_file = DOC_PATH + "\\admin_account_info\\" + account + '_info'
    config = ConfigParser()
    config.read(account_file)
    # config_group = config.sections()[0]
    # print(str(config[account]['PASSWORD']))
    if password == config[account]['PASSWORD']:
        print("Welcome %s !" % account)
        return True
    else:
        print("Wrong password!")
        return False


    # print(account)


def Choice():
    print("Welcome to use ATM!")
    print("Who are you?")
    print("1.Users")
    print("2.Admin")
    print("3.exit")
    choice = input(">")
    return choice

def login_index():
    count = 1

    while True:
        choice = Choice()
        if choice == '1':
            user_login()
            break
        # break
        elif choice == '2':
            admin_login()
            break
        elif choice == '3':
            break
        else:
            if count > 2:
                print("Wrong counts is 3 !!!")
                break
            else:
                print("Wrong choice,Please try again!")
                count += 1


login_index()