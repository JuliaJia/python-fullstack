import os
import time
import logging

USER_DIR_FOLDER = r"E:\python\anaconda\ATM"
def get_logger(card_num, struct_time):

    # if struct_time.tm_mday < 23:
    #     file_name = "%s_%s_%d" %(struct_time.tm_year, struct_time.tm_mon, 22)
    # else:
    #     file_name = "%s_%s_%d" %(struct_time.tm_year, struct_time.tm_mon+1, 22)

    file_name = struct_time
    file_path = os.path.join(USER_DIR_FOLDER, card_num, 'record')
    os.system("mkdir -p %s" % file_path)
    file_handler = logging.FileHandler(
        os.path.join(file_path, file_name),
        encoding='utf-8'
    )
    fmt = logging.Formatter(fmt="%(asctime)s :  %(message)s")
    file_handler.setFormatter(fmt)

    logger1 = logging.Logger('user_logger', level=logging.INFO)
    logger1.addHandler(file_handler)
    return logger1

struct_time = time.strftime('%Y-%m-%d %H-%M-%S',time.localtime())

while True:
    card_num = input("Enter your CardNum:")
    logger = get_logger(card_num,struct_time)
    logger.info('Your Card %s login!' % card_num)
    break

