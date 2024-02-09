import sys

def cat():
    print('meow')

def default():
    print('Hello')

def main():
    # Check if there are command-line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "cat":
            cat()
        else:
            default()
    else:
        default()

# This block ensures that the main() function is called only when the script is run directly
if __name__ == '__main__':
    main()

