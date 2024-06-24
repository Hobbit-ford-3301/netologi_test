import os
from datetime import datetime

def logger(old_function):
    def new_function(*args, **kwargs):
        timestamp = datetime.now().strftime('%y-%m-%d %H:%M:%S')
        args_str = ', '.join(map(repr, args))
        kwargs_str = ', '.join(f'{k}={v!r}' for k, v in kwargs.items())
        arguments = args_str + ', ' + kwargs_str if args_str and kwargs_str else args_str or kwargs_str

        result = old_function(*args, **kwargs)

        with open('main.log', 'a') as log_file:
            log_file.write(f'{timestamp}: {old_function.__name__}({arguments}) -> {result}\n')

        return result

    return new_function

def test_1():

    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'hello world'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'hello world' == hello_world(), "функция возвращает 'hello world'"
    result = summator(2, 2)
    assert isinstance(result, int), 'должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()