import argparse
from collections import defaultdict


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            print(f'Error: {e}')
    return wrapper


def hello_func(*args, **kwargs):
    print('How can I help you?')

@input_error
def add_func(args, num_dict):
    num_dict[args.name] = args.number
    return num_dict

@input_error
def change_func(args, num_dict):
    if args.name in num_dict:
        num_dict[args.name] = args.number
    else:
        raise KeyError(f'No such name in the dictionary!')

@input_error
def phone_func(args, num_dict):
    result = num_dict.get(args.name, None)
    if result is None:
        raise KeyError('No such name in the dictionary.')
    print(f'For the contact {args.name}, the number is {result}')

@input_error
def show_func(*args, **kwargs):
    print(kwargs['num_dict'])


COMAND_DICT = {
    'hello': hello_func,
    'add': add_func,
    'change': change_func,
    'phone': phone_func,
    'show_all': show_func
}


@input_error
def handle_func(args, num_dict):
    if args.command in COMAND_DICT:
        return COMAND_DICT[args.command](args, num_dict=num_dict)
    else:
        raise KeyError('Unknown command')


def main():
    num_dict = defaultdict(str)
    while True:
        command = input('Enter command: ')
        if command.lower() in ['good bye', 'close', 'exit']:
            print('Good bye!')
            break

        command_parts = command.lower().split()
        command_name = command_parts[0]

        if command_name in COMAND_DICT:
            parser = argparse.ArgumentParser(description='Assistant bot program.')
            parser.add_argument('command', choices=COMAND_DICT.keys(), help='Available commands')
            parser.add_argument('name', nargs='?', default='', help='Contact name')
            parser.add_argument('number', nargs='?', default='', help='Contact number')
            args = parser.parse_args(command_parts)
            result = handle_func(args, num_dict)
            if result is not None:
                print(result)
        else:
            print('Invalid command. Please try again.')


if __name__ == '__main__':
    main()
