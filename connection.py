from func import Parser

parser = Parser()

all_apartments = []
nameName = parser.name().values()
hrefHref = parser.href().values()

def add_data():
    for i, (name, href) in enumerate(zip(nameName, hrefHref), start=1):
        apartment = {
            f'data_of_apartment №{i}': {  # Используем f-строку для добавления номера
                "name": name,
                "href": href,
            }
        }
        all_apartments.append(apartment)

add_data()
# print(all_apartments)