from loguru import logger
logger.add('b.txt',format='{time} {level} {message}',level='WARNING')
logger.info('这是一条info级别的信息：')
logger.debug('这是一条debug的日志')
logger.warning('这是一条warning的日志')
logger.success('这是一条success的日志')
logger.error('这是一条error的日志')
logger.info('这是一条{}的日志','info')
