import logging




# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a,%d %b %Y %H:%M:%S',
#                     # )
#                     filename='test.log',
#                     filemode='w')
#
# # 五个日志的级别
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')


#step1:创建logger对象
logger = logging.getLogger()   #拿一个logger对象
#step2:创建日志Handler
fh = logging.FileHandler('test.log') #创建一个handler，用于写入日志文件
ch = logging.StreamHandler()   #创建一个handler，用于将日志打到屏幕上
#step3:定义日志格式并应用到handler中
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') #定义日志格式
fh.setFormatter(formatter)
ch.setFormatter(formatter)

#step4:添加Handler到logger对象中
logger.addHandler(fh) #logger对象可以添加多个fh和ch对象
logger.addHandler(ch)


# step5：设置日志信息
logger.setLevel(logging.DEBUG)   #设置日志level效果等同于logging.basicConfig(level=logging.DEBUG)
logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')