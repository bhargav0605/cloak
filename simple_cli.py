import sys

def print_help():
    help_text = """
    Simple Cli Application

    Usage:
        python simple_cli.py [options]

    Options:
        -h, --help      Show this help message and exit.
        -g, --greet     Greet the user with a message.
        -n, --name      Specify the name of the user.
    """
    print(help_text)

def greet(name):
    if name:
        print(f"Hello, {name}!!")
    else:
        print("Hello!");

def main():
    print(f"Argument: {sys.argv}");
    if len(sys.argv) < 2:
        print("No arguments provided. Use -h or --help for usage.")
        return

    args = sys.argv[1:];
    if '-h' in args or '--help' in args:
        print_help()
    elif '-g' in args or '--greet' in args:
        name_index = args.index('-n') + 1 if '-n' in args else args.index('--name') + 1 if '--name' in args else None
        name = args[name_index] if name_index and name_index < len(args) else None
        greet(name)
    else:
        print("Unknown option. Use -h or --help for usage.")

if __name__ == "main":
    main();
