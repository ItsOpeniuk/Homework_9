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


def handle_func(args):
    if args.command in COMAND_DICT:
        return COMAND_DICT[args.command]
    else:
        print('Неизвестная команда')
        return None


def main():
    num_dict = defaultdict(str)
    while True:
        parser = argparse.ArgumentParser(description='Программа бот ассистент.')
        subparser = parser.add_subparsers(help='Доступные комманды' )

        subparser.add_parser('hello', help='Парсер для функции приветсвия')

        add_func_parser = subparser.add_parser('add', help='Парсер функции "add"')
        add_func_parser.add_argument('name', help='Имя контакта')
        add_func_parser.add_argument('number', help='Номер контакта')
        add_func_parser.set_defaults(func=lambda args: add_func(args, num_dict))

        change_parser = subparser.add_parser('change', help='Замена номера телефона определенного контакта')
        change_parser.add_argument('name', help='Имя контакта которому нужно сменить телефон')
        change_parser.set_defaults(func=lambda args: change_func(args, num_dict))

        phone_parser = subparser.add_parser('phone', help='Определяет номер телефона заданного контакта')
        phone_parser.add_argument('name', help='Имя контакта чей номер нужно показать')
        phone_parser.set_defaults(func=lambda args: phone_func(args, num_dict))

        show_parser = subparser.add_parser('show_all', help='Вывод полного словаря контактов')
        show_parser.set_defaults(func=lambda args: show_func(num_dict))

        args = parser.parse_args()
        args.func(args)


if __name__ == '__main__':
    main()

