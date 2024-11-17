import pytest

from src.sub_main import Product, Category


@pytest.fixture
def product_data():
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    }


@pytest.fixture
def product_samsung(product_data):
    return Product.new_product(product_data)


@pytest.fixture
def category_electronics():
    return Category("Телефоны", "Все телефоны")


def test_product_initialization(product_samsung):
    assert product_samsung.name == "Samsung Galaxy S23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert product_samsung.price == 180000.0
    assert product_samsung.quantity == 5


def test_product_str(product_samsung):
    expected_str = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(product_samsung) == expected_str



def test_product_addition(product_samsung):
    product_iphone = Product.new_product({
        "name": "iPhone 14 Pro",
        "description": "128GB, Золотой цвет",
        "price": 150000.0,
        "quantity": 3
    })

    total_price = product_samsung + product_iphone
    expected_total = (product_samsung.price * product_samsung.quantity) + (
                product_iphone.price * product_iphone.quantity)
    assert total_price == expected_total


def test_category_initialization(category_electronics):
    assert category_electronics.name == "Телефоны"
    assert category_electronics.description == "Все телефоны"
    assert len(category_electronics.products) == 0
    assert Category.category_count == 1


def test_add_product_to_category(category_electronics, product_samsung):
    category_electronics.add_product(product_samsung)
    assert Category.product_count == 1


def test_category_products_str(category_electronics, product_samsung):
    category_electronics.add_product(product_samsung)
    expected_str = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
    assert category_electronics.products == expected_str


def test_category_product_count(category_electronics):
    product_iphone = Product.new_product({
        "name": "iPhone 14 Pro",
        "description": "128GB, Золотой цвет",
        "price": 150000.0,
        "quantity": 3
    })

    category_electronics.add_product(product_iphone)
    assert Category.product_count == 3