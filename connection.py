from func import Parser

parser = Parser()

all_apartments = []
parser.collection()
# nameName = parser.collection()[0]
# hrefHref = parser.collection()[1]
nameName = parser.list_of_name
hrefHref = parser.list_of_apartments

def add_data():
    for i, (name, href) in enumerate(zip(nameName, hrefHref)):
        apartment = {
            f'data_of_apartment №{i}': {  # Используем f-строку для добавления номера
                "name": name,
                "href": href,
            }
        }
        all_apartments.append(apartment)

add_data()
# print(nameName, hrefHref)
