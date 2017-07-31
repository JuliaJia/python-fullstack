from configparser import ConfigParser
import random
import logging

DOC_PATH = "E:\\python\\anaconda\\python_fullstack\\day18\\ATM\\doc"

def readfile(filename):
    line_list = []
    file = open(filename,'a+')
    for line in file.readlines():
        line = line.strip('\n')
        line_list.append(line)
    file.close()
    return line_list

def createfile(filename):
    file = open(filename,'w')
    file.close()

def atm_log(account,level,message):
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a,%d %b %Y %H:%M:%S',
                        filename=DOC_PATH + '\\log\\' + account + '.log',
                        filemode='w')
    if level == 'info':
        logging.info(message)
    elif level == 'warning':
        logging.warning(message)
    elif level == 'error':
        logging.error(message)

def checkadminaccount(account):
    account_list = readfile("%s\\admin_account_list.txt" % DOC_PATH)
    if account in account_list:
        return False
    else:
        return True

def addadminaccount():
    account = input("Enter admin account:")
    check = checkadminaccount(account)
    while check == False:
        account = input("This account is exist,try again:")
        check = checkadminaccount(account)
    password1 = input("Enter password:")
    password2 = input("Enter password again:")
    while password2 != password1:
        print("The two passwords do not match!")
        password1 = input("Enter password:")
        password2 = input("Enter password again:")
    password = password1
    config = ConfigParser()
    config['DEFAULT'] = {'ACCOUNT': account}
    config[account] = {}
    config[account]['ACCOUNT'] = account
    config[account]['PASSWORD'] = password
    account_file = DOC_PATH + "\\admin_account_info\\" + account + '_info'
    with open(account_file,'w') as configfile:
        config.write(configfile)
    message = 'Create this admin account(%s)!' % account
    atm_log(account,'warning',message)
    print(message)

def checkuseraccount(account):
    account_list = readfile("%s\\account_list.txt" % DOC_PATH)
    if account in account_list:
        return False
    else:
        return True

def createuseraccount():
    account = '6225'
    count = 12
    for i in range(count):
        account += str(random.randrange(0,10))
    check = checkuseraccount(account)
    if check == True:
        return account
    else:
        return False

def adduseraccount():
    INIT_MONEY = "15000.0"
    account = createuseraccount()
    check = checkuseraccount(account)
    while check == False:
        account = createuseraccount()
        check = checkuseraccount(account)
    config = ConfigParser()
    config['DEFAULT'] = {'INIT_MONEY':INIT_MONEY,
                         'ACCOUNT':account,
                         'REPAY_DATE':10,
                         'BILL_DATE':22,
                         'INTEREST':0.0005}

    config[account] = {}
    config[account]['NOW_MONEY'] = INIT_MONEY
    config[account]['USE_MONEY'] = "0"
    config[account]['OVER_MONEY'] = INIT_MONEY
    config[account]['FREEZE_STATUS'] = "False"
    config[account]['PASSWORD'] = "88888888"
    account_file = DOC_PATH + "\\account_info\\" + account + '_info'
    with open(account_file,'w') as configfile:
        config.write(configfile)
    message = 'Create this account(%s)!' % account
    atm_log(account,'warning',message)
    print(message)

def changeusermoney(account,newmoney):
    account_file = DOC_PATH + "\\account_info\\" + account + '_info'
    config = ConfigParser()
    config.read(account_file)
    config_group = config.sections()[0]
    over_money = str(float(newmoney) - float(config[account]['USE_MONEY']))
    if config.has_section(config_group) == True:
        config.set(config_group,'NOW_MONEY',str(float(newmoney)))
        config.set(config_group,'OVER_MONEY',over_money)
        config.write(open(account_file, 'w'))
        message = "Change the account(%s)'s limit to %s" % account,newmoney
        atm_log(account,'warning',message)
        print(message)
    else:
        message = "The account %s is deleted!" % account
        atm_log(account, 'error', message)
        print(message)

    # return config_group

def freezeuseraccount(account):
    account_file = DOC_PATH + "\\account_info\\" + account + '_info'
    config = ConfigParser()
    config.read(account_file)
    config_group = config.sections()[0]
    now_status = config[account]['FREEZE_STATUS']
    if now_status == 'False':
        config.set(config_group,'FREEZE_STATUS','True')
        config.write(open(account_file,'w'))
        message = "This account(%s) Freeze Now!!!" % account
        atm_log(account,"warning",message)
        print(message)
    else:
        message = "This account(%s)'s Freeze status is True!!! " % account
        atm_log(account,'error',message)
        print(message)

addadminaccount()

# changemoney("6225034329348771","20000")

# freeze_account("6225189517912256")
# changemoney('6225189517912256','20000')