from db_func import get_product_by_id, get_category_by_id

db_config = {
    'host': 'localhost',
    'database': 'Nortwind_traders',
    'user': 'postgres',
    'password': '0000'
}

if __name__ == "__main__":
    while True:
        command = input("Выберите продукты(0) или катекгории(1) или введите exit для выхода из программы: ")

        if command =='0':
            id = input('Введите ID товара (максимум 77): ')
            if int(id) > 77 or int(id) < 1:
                print('Нет такого ID, попробуйте заново!')
                continue
            res = get_product_by_id(config=db_config, id=id)
            print('*' * 600)
            print(res)
            print('*' * 600)
        elif command == '1':
            id = input('Введите ID категории (максимум 8): ')
            if int(id) > 8 or int(id) < 1:
                print('Нет такого ID, попробуйте заново!')
                continue
            res = get_category_by_id(config=db_config, id=id)
            print('*' * 600)
            print(res)
            print('*' * 600)
        elif command == 'exit':
            break
        else:
            print('команды не существует, попробуйте заново!')
            continue