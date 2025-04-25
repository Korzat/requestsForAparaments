from connection import all_apartments
if __name__ == '__main__':
    try:
        print(all_apartments)
    except Exception as e:
        print(f'Ошибка: {e}')
