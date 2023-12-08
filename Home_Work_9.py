import argparse
from collections import defaultdict


def hello_func():
    print('How can I help you?')


def add_func(argv, num_dict):
    num_dict[argv.name] = argv.number
    return num_dict


def change_func(args, num_dict):
    try:
        if args.name in num_dict:
            num_dict[args.name] = args.num
    except KeyError:
        print('Такого имени нет в словаре!')


def phone_func(args, num_dict):
    result = None
    try:
        if args.name in num_dict:
            result = num_dict[args.name]
    except KeyError:
        print('Такого имени нет в словаре.')
    print(f'Для контакта {args.name} закреплен номер {result}')


def show_func(num_dict):
    print(num_dict)


COMAND_DICT = {
    'hello': hello_func,
    'add': add_func,
    'change': change_func,
    'phone': phone_func,
    'show all': show_func
}


def handle_func(*args):
    if args in COMAND_DICT:
        return COMAND_DICT[args]
    else:
        print('Неизвестная команда')
        return None

def main():
    num_dict = defaultdict(str)
    while True:
        parser = argparse.ArgumentParser(description='Программа бот ассистент.')

        subparser = parser.add_subparsers(dest='subcommand', )

        hello_parcer = subparser.add_parser('hello', help='Парсер для функции приветсвия')
        hello_parcer.set_defaults(func=hello_func())