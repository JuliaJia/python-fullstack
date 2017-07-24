import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {'KEY1':'VALUE1',
                     'KEY2':'VALUE2',
                     'KEY3':'VALUE3'}

config['GROUP1'] = {}
config['GROUP1']['KEY1'] = 'VALUE1'

with open('example.ini','w') as configfile:
    config.write(configfile)


