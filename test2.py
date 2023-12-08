import argparse

def add_func(args, num_dict):
    num_dict[args.name] = args.number
    print(num_dict)
    return num_dict

def main():
    num_dict = {}  # Создаем словарь для номеров телефонов
    parser = argparse.ArgumentParser(description='Программа бот ассистент.')
    subparsers = parser.add_subparsers(help='Доступные команды')

    add_parser = subparsers.add_parser('add', help='Парсер функции "add"')
    add_parser.add_argument('name', help='Имя контакта')
    add_parser.add_argument('number', help='Номер контакта')
    add_parser.set_defaults(func=lambda args: add_func(args, num_dict))

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
