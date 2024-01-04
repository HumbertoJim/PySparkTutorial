import importlib
import sys

messages = dict(
    commands='Available commands\n'+ ('-'*20) + '\n - startapp\n - runapp\n'
)

if len(sys.argv) > 1:
    try:
        arg = sys.argv[1].strip()
        if arg == 'startapp':
            if len(sys.argv) < 3:
                raise Exception('startapp command requires the spark application name as argument.')
            param = sys.argv[2].strip()
            path = f'scripts/{param}.py'
            file = open(path, 'a')
            file.close()
            print(f'{path} created.')
        elif arg == 'runapp':
            if len(sys.argv) < 3:
                raise Exception('runapp command requires the spark application name as argument.')
            param = sys.argv[2].strip()
            importlib.import_module(f'scripts.{param}')
        else:
            print(messages.get('commands'))
    except NameError as e:
        print(f'Import Error:\n{e}')
    except Exception as e:
        print(f'Error:\n{e}')
else:
    print(messages.get('commands'))