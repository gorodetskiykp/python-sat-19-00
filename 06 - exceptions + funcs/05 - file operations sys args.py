import sys

args = sys.argv

if len(args) == 1:
    print("Hello!")
else:
    if args[1] == 'ru':
        print("Привет!")
    elif args[1] == 'esp':
        print("Hola!")
    else:
        print("Hello!")

