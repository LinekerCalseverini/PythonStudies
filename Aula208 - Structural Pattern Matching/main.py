# def execute_command(command):
#     if command == "ls":
#         print('$ listing files')
#     elif command == "cd":
#         print('$ changing directory')
#     else:
#         print('$ command not implemented')

#     print('...rest of the code')

# def execute_command(command):
#     match(command):
#         case 'ls':
#             print('$ listing files')
#         case 'cd':
#             print('$ changing directory')
#         case _:  # Não obrigatório
#             print('$ command not implemented')

#     print('...rest of the code')

# def execute_command(command):
#     match command.split():
#         case ['ls', *directories, '--force']:
#             for directory in directories:
#                 print('$ FORCE listing files from', directory)
#         case ['ls', *directories]:
#             for directory in directories:
#                 print('$ listing files from', directory)
#         case ['cd', path, *_]:
#             print('$ changing directory to', path)
#         case _:  # Não obrigatório
#             print('$ command not implemented')


# execute_command('ls /path /home /root --force')
# execute_command('ls /path /home /root')

# def execute_command(command):
#     match command.split():
#         case ['ls' | 'list', *directories]:
#             for directory in directories:
#                 print('$ listing files from', directory)
#         case ['cd' | 'change', path, *_]:
#             print('$ changing directory to', path)
#         case _:  # Não obrigatório
#             print('$ command not implemented')

# def execute_command(command):
#     match command.split():
#         case ['ls' | 'list', *directories] if len(directories) > 1:
#             for directory in directories:
#                 print('$ listing ALL files from', directory)
#         case ['ls' | 'list', *directories] if len(directories) <= 1:
#             for directory in directories:
#                 print('$ listing ONE file from', directory)
#         case ['cd' | 'change', path, *_]:
#             print('$ changing directory to', path)
#         case _:  # Não obrigatório
#             print('$ command not implemented')

# def execute_command(command):
#     match command.split():
#         case ['ls' | 'list' as the_command, *directories] as the_list \
#                 if len(directories) > 1:
#             for directory in directories:
#                 print('$ listing ALL files from', directory)
#             print(f'{the_command=}, {the_list=}')
#         case ['ls' | 'list', *directories] if len(directories) <= 1:
#             for directory in directories:
#                 print('$ listing ONE file from', directory)
#         case ['cd' | 'change', path, *_]:
#             print('$ changing directory to', path)
#         case _:  # Não obrigatório
#             print('$ command not implemented')


# def execute_command(command):
#     match command:
#         case {'command': 'ls', 'directories': [_, *_]}:
#             for directory in command['directories']:
#                 print('$ listing ALL files from', directory)
#         case _:  # Não obrigatório
#             print('$ command not implemented')
from dataclasses import dataclass


@dataclass
class Command:
    command: str
    directories: list[str]


def execute_command(command: Command):
    match command:
        case Command(command='ls', directories=[_, *_]):
            for directory in command.directories:
                print('$ listing ALL files from', directory)
        case Command(command='ls', directories=[_]):
            for directory in command.directories:
                print('$ changing directory to ', directory)
        case _:  # Não obrigatório
            print('$ command not implemented')


execute_command(Command('ls', ['path', 'home', 'root']))
