import json
import os

from src.sub_main import Category, Product


def load_data() -> list:
    """Функция получения данных с json-файла"""
    current_dir = os.path.dirname(__file__)  # Получаем директорию текущего файла
    path = os.path.join(
        current_dir, "..", "products.json"
    )  # Поднимаемся на уровень выше и добавляем
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def create_class_obj():
    """Создание объектов класса из json файла"""
    categories = []
    data_list = load_data()
    for data in data_list:
        products = []
        for el in data["products"]:
            product = Product(
                name=el["name"],
                description=el["description"],
                price=el["price"],
                quantity=el["quantity"],
            )
            products.append(product)

        category = Category(
            name=el["name"], description=el["description"], products=products
        )
        categories.append(category)
    return categories
