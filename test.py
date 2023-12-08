import argparse
from collections import defaultdict


def hello_func():
    print('How can I help you?')


def add_func(args, num_dict):
    num_dict[args.name] = args.number
    return num_dict


def change_func(args, num_dict):
    if args.name in num_dict:
        num_dict[args.name] = args.number
    else:
        print('Такого имени нет в словаре!')


def phone_func(args, num_dict):
    result = num_dict.get(args.name, 'Такого имени нет в словаре.')
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


def handle_func(command):
    if command in COMAND_DICT:
        return COMAND_DICT[command]
    else:
        print('Неизвестная команда')
        return None


def main():
    num_dict = defaultdict(str)

    parser = argparse.ArgumentParser(description='Программа бот ассистент.')
    subparser = parser.add_subparsers(dest='subcommand')

    hello_parser = subparser.add_parser('hello', help='Парсер для функции приветствия')
    hello_parser.set_defaults(func=hello_func)

    add_parser = subparser.add_parser('add', help='Парсер для функции добавления')
    add_parser.add_argument('name', help='Имя контакта')
    add_parser.add_argument('number', help='Номер контакта')
    add_parser.set_defaults(func=add_func)

    change_parser = subparser.add_parser('change', help='Парсер для функции изменения')
    change_parser.add_argument('name', help='Имя контакта')
    change_parser.add_argument('number', help='Новый номер контакта')
    change_parser.set_defaults(func=change_func)

    phone_parser = subparser.add_parser('phone', help='Парсер для функции вывода номера')
    phone_parser.add_argument('name', help='Имя контакта')
    phone_parser.set_defaults(func=phone_func)

    show_parser = subparser.add_parser('show all', help='Парсер для функции вывода всех контактов')
    show_parser.set_defaults(func=show_func)

    args = parser.parse_args()  # Сохраняем результат в переменную за пределами цикла

    while True:
        handler = args.func
        if handler:
            handler(args, num_dict)


        args = parser.parse_args()


if __name__ == "__main__":
    main()
