from src.create_file import create_file, create_folder


def main():
    filename = 'lita-rk1-theory.pdf'
    create_folder(filename)
    for opacity in range(20, 60, 10):
        create_file(opacity, filename)
        print(f'A file "{filename}" with {opacity}% transparency has been created')


if __name__ == '__main__':
    main()
