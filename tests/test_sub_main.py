import pytest

from src.sub_main import Category, LawnGrass, Product, Smartphone


@pytest.fixture
def product_data():
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
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
    product_iphone = Product.new_product(
        {
            "name": "iPhone 14 Pro",
            "description": "128GB, Золотой цвет",
            "price": 150000.0,
            "quantity": 3,
        }
    )

    total_price = product_samsung + product_iphone
    expected_total = (product_samsung.price * product_samsung.quantity) + (
        product_iphone.price * product_iphone.quantity
    )
    assert total_price == expected_total


def test_category_initialization():
    category = Category("Телефоны", "Все телефоны")
    assert category.name == "Телефоны"
    assert category.description == "Все телефоны"
    assert category.products == ""


def test_smartphone_initialization():
    smartphone = Smartphone(
        "iPhone 14 Pro",
        "128GB, Золотой цвет",
        150000.0,
        3,
        efficiency="A16 Bionic",
        model="14 Pro",
        memory="128GB",
        color="Gold",
    )

    assert smartphone.name == "iPhone 14 Pro"
    assert smartphone.efficiency == "A16 Bionic"


def test_lawn_grass_initialization():
    lawn_grass = LawnGrass(
        "Зеленая трава",
        "Для газонов",
        500.0,
        10,
        country="Россия",
        germination_period="7-14 дней",
        color="Зеленый",
    )

    assert lawn_grass.name == "Зеленая трава"
    assert lawn_grass.country == "Россия"


def test_add_product_wrong_type(category_electronics):
    with pytest.raises(TypeError):
        category_electronics.add_product("hello")


def test_repr():
    product = Product(
        name="iPhone 14 Pro",
        description="128GB, Золотой цвет",
        price=150000.0,
        quantity=3,
    )
    assert (
        repr(product) == "Product('iPhone 14 Pro', '128GB, Золотой цвет', 150000.0, 3)"
    )
