def id_caching():
    val_1 = 10
    val_2 = 10

    # for small numbers and all Strings Python re-use objects
    print(f'id of val_1 = {id(val_1)}')
    print(f'id of val_2 = {id(val_2)}')

    str_1 = 'string_token'
    str_2 = 'string_token'

    print(f'id of str_1 = {id(str_1)}')
    print(f'id of str_2 = {id(str_2)}')


def main():
    id_caching()


if __name__ == '__main__':
    main()
