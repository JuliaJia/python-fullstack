# from configparser import ConfigParser

# config = ConfigParser()
# config['DEFAULT'] = {'KEY1':'VALUE1',
#                      'KEY2':'VALUE2',
#                      'KEY3':'VALUE3'}
#
# config['GROUP1'] = {}
# config['GROUP1']['KEY1'] = 'VALUE1'
#
# with open('example.ini','w') as configfile:
#     config.write(configfile)





# from configparser import ConfigParser
#
# def test(key,config_name):
#     d = 'DEFAULT'
#     config = ConfigParser()
#     config.read(config_name)
#     config_groups = config.sections()
#     for i in config_groups:
#         if key in config[i]:
#             KEY = config[i][key]
#         else:
#             KEY = config[d][key]
#     return KEY
#
# config_name = 'example.ini'
# KEY1 = test('KEY1',config_name)
# KEY2 = test('KEY2',config_name)
# KEY3 = test('KEY3',config_name)
# print("KEY1 is %s,KEY2 is %s,KEY3 is %s" % (KEY1,KEY2,KEY3))

from configparser import ConfigParser

def test(groupname,key,value,config_name,functionname):
    config = ConfigParser()
    config.read(config_name)
    groups = config.sections()
    if functionname == 'remove_section' and groupname in groups:
        config.remove_section(groupname)
        config.write(open(config_name,"w"))
    elif functionname == 'remove_section' and groupname not in groups:
        print("No this section!!!!")
    if functionname == "add_section" and config.has_section(groupname) != True:
        config.add_section(groupname)
        config.write(open(config_name,"w"))
    elif functionname == "add_section" and config.has_section(groupname) == True:
        print("This section is already exists!!!")
    if functionname == "set_option":
        config.set(groupname,key,value)
        config.write(open(config_name,"w"))
    if functionname == "remove_option" and config.has_option(groupname,key) == True:
        config.remove_option(groupname,key)
        config.write(open(config_name,"w"))
    elif functionname == "remove_option" and config.has_option(groupname,key) != True:
        print("No this option!!!!")



# test('test',None,None,'example.ini','add_section')
# test('test',None,None,'example.ini','remove_section')
# test('test','Name','Julia','example.ini','set_option')
test('test','Name',None,'example.ini','remove_option')