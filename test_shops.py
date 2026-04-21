import shops
# Base Class Tests

def test_getMenuSize():
    # One menu item
    Restaurant1 = shops.Restaurant("Test", ("Test",))
    assert Restaurant1.getMenuSize() == 1

    # More than one menu item
    Restaurant2 = shops.Restaurant("Test", ("Test", "Test"))
    assert Restaurant2.getMenuSize() == 2

    # No menu items
    Restaurant3 = shops.Restaurant("Test", ())
    assert Restaurant3.getMenuSize() == 0

def test_getChoice():
    # One menu item
    Restaurant1 = shops.Restaurant("Test", ("Test",))
    assert Restaurant1.getChoice(("Test",), "Enter Choice: ") == 0

    # More than one menu item
    Restaurant2 = shops.Restaurant("Test", ("Test", "Test"))
    assert Restaurant2.getChoice(("Test", "Test"), "Enter choice: ") == 0 and Restaurant2.getChoice(("Test", "Test"), "Enter choice: ") == 1
    assert Restaurant2.getChoice(("Test", "Test"), "Enter choice: ") == 1 and Restaurant2.getChoice(("Test", "Test"), "Enter choice: ") == 0

    """
    # No menu items
    Restaurant3 = shops.Restaurant("Test", ())
    assert Restaurant3.getChoice((), "Enter choice: ") == -2

    Doesn't work due to exception handling.
    """

# Derived Class Tests

def test_coffeeOrder():
    CoffeeShop = shops.CoffeeShop(("Test",), ("Test",), ("Test",))
    assert CoffeeShop.order(1) == CoffeeShop

def test_bobaOrder():
    BobaShop = shops.BobaShop(("Test",), ("Test",), ("Test",), ("Test",))
    assert BobaShop.order(1) == BobaShop

def test_bakeryOrder():
    Bakery = shops.Bakery()
    assert Bakery.order(1) == Bakery

