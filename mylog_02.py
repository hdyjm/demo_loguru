from loguru import logger
def add(a,b,*args):
    sum = 0
    if not isinstance(a,int):
        logger.error('输入的数据类型不正确')
        return
    if not isinstance(b,int):
        logger.error('输入的参数b类型不正确')

    for x in args:
        if not isinstance(x,int):
            logger.warning('输入的数据有错误类型，请检查')
            continue

        sum += x

    sum = sum + a + b
    return sum

add(3,4)
print('='* 20)
add(3,'h')
print('='* 20)
add(3,5,8)
print('='* 20)
add(3,5,'t')
print('='* 20)
print(add(3,5,'k',2))
