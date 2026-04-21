import exceptions
import shops
import cart

# Function to add an order into the tree
def addToCart(shop: shops.CoffeeShop | shops.BobaShop | shops.Bakery, tree: cart.Tree, order: shops.CoffeeShop | shops.BobaShop | shops.Bakery) -> bool:
    inserted = tree.insert(order)
    if inserted:
        print("\nAdded to cart: \n")
        shop.displayOrder()
        return True
    return False

class Customer:
    def __init__(self):
        self._name = ""
        self._address = ""
        self._postal = ""

    def display(self) -> None:
        print("\nDelivery Information")
        print(f"\nName: {self._name}\nStreet Address: {self._address}\nCity and State: {self._postal}\n")

    def getInfo(self) -> None:
        print("\n> Dessert Marketplace <\n\nBefore you start shopping, we need more information.")
        while True:
            try:
                if not self._name:
                    self._name = input("\nEnter your full name: ")
                    exceptions.empty(self._name)
                if not self._address:
                    self._address = input("Enter street address: ")
                    exceptions.empty(self._address)
                if not self._postal:
                    self._postal = input("Enter city and state: ")
                    exceptions.empty(self._postal)
                break
            except exceptions.EmptyInput as empty:
                print(empty)

class MainMenu:
    def __init__(self):
        self._customer = Customer()
        self._bakery = shops.Bakery()
        self._coffeeMenu = CoffeeMenu()
        self._bobaMenu = BobaMenu()
        self._bakeryMenu = BakeryMenu()
        self._cart = cart.Tree()
        self._option = 0
        # Number of menu choices
        self._lower = 1
        self._upper = 4

    def run(self):
        self._customer.getInfo()
        while True:
            self.mainScreen()
            if self._option == 1:
                self._coffeeMenu.run(self._cart)
                self._option = 0
                continue
            if self._option == 2:
                self._bobaMenu.run(self._cart)
                self._option = 0
                continue
            if self._option == 3:
                self._bakeryMenu.run(self._cart)
                self._option = 0
                continue
            if self._option == 4:
                if self.cartScreen():
                    break
                self._option = 0
                continue

    # Displays the main menu screen and gets the option for the sub-menu that the user wants to access 
    def mainScreen(self) -> None:
        print("\nCraving a pastry, cup of coffee, or boba? Choose from either a\n" 
               "coffee shop, boba shop, or a bakery and get it delivered straight\n"
               "to your address for no delivery fee. Limited time only.\n")
        print("\t1. Fresh Roasters\n\t2. Best Boba\n\t3. Artisan Bakery\n\t4. Checkout\n")
        while self._option == 0:
            try:
                self._option = int(input("Enter menu choice: "))
                exceptions.bounds(self._option, self._lower, self._upper)
                break
            except exceptions.OutOfBounds as out:
                self._option = 0
                print(out)
            except ValueError:
                print("\nEnter a valid menu choice.\n")  

    def cartScreen(self) -> bool:
        """
        Returns True if the user exits the program to signify termination. 
        Otherwise returns False.
        """
        option = 0
        while True:
            print("\nYour cart:\n")
            if not self._cart.displayAll():
                print("There is nothing in your cart. Add an item to your cart before checking out.")
                break
            try:
                confirm = input("Confirm order (y/n): ")
                exceptions.empty(confirm)
                confirm = confirm.lower()
                if confirm != "y" and confirm != "n":
                    raise ValueError
                elif confirm == "y":
                    self._customer.display()
                    print("Thank you for placing your order with Dessert Marketplace. Your order will arrive shortly.\n")
                    return True
                elif confirm == "n":
                        break
            except exceptions.EmptyInput as empty:
                print(empty)
            except exceptions.OutOfBounds as out:
                print(out)
            except ValueError:
                print("Valid options are \"y\" and \"n\".")
            return False

class CoffeeMenu:
    def __init__(self):
        self._option = 0

    def run(self, cart) -> None:
            print("\nFresh Roasters get their coffee beans from local companies that\n"
                    "put love into their craft. Their syrups are sourced from\n"
                    "high-quality makers, elevating the flavor profile of your drink.\n"
                    "Satisfaction guaranteed.\n")
            while self._option != 5:
                shop = shops.CoffeeShop(("Strawberry", "Vanilla", "Hazelnut", "Caramel"), ("12oz", "16oz", "20oz"), ("Hot", "Iced"))
                size = shop.getMenuSize()
                print("> Fresh Roasters:\n")
                shop.displayMenu()
                while True:
                    try:
                        self._option = int(input("Enter menu choice: "))
                        exceptions.bounds(self._option, 1, size + 1)
                        if self._option == 5:
                            break
                        # Menu options are not displayed with an offset, so have to manually update
                        self._option -= 1
                        order = shop.order(self._option)
                        if not addToCart(shop, cart, order):
                            print("Couldn't add that item to your cart...")
                        break
                    except exceptions.OutOfBounds as out:
                        print(out)
                    except ValueError:
                        print("\nEnter a valid menu choice.\n")
            self._option = 0
            return

class BobaMenu:
    def __init__(self):
        self._option = 0

    def run(self, cart) -> None:
        print("\nBest Boba is a long standing boba shop known for its creative\n"
                "flavors and aesthetic drinks. Their brown sugar boba is cooked\n"
                "fresh daily and they're ranked as one of the best boba shops in\n"
                "town. Grab a drink and try it out today!\n")
        while self._option != 5:
            shop = shops.BobaShop(("Brown Sugar", "Strawberry", "Coconut", "Taro"), ("Medium", "Large"), ("30%", "50%", "100%"), ("y", "n"))
            size = shop.getMenuSize()
            print("> Best Boba:\n")
            shop.displayMenu()
            while True:
                try:
                    self._option = int(input("Enter menu choice: "))
                    exceptions.bounds(self._option, 1, size + 1)
                    if self._option == 5:
                        break
                    # Menu options are not displayed with an offset, so have to manually update
                    self._option -= 1
                    order = shop.order(self._option)
                    if not addToCart(shop, cart, order):
                            print("Couldn't add that item to your cart...")
                    break
                except exceptions.OutOfBounds as out:
                    print(out)
                except ValueError:
                    print("\nEnter a valid menu choice.\n")
        self._option = 0
        return
    
class BakeryMenu:
    def __init__(self):
        self._option = 0

    def run(self, cart) -> None:
        print("\nArtisan Bakery is a newly opened store founded by a recently\n"
                "appointed pastry chef. Although they only offer classic pastries,\n"
                "their use of high-quality ingredients speaks for itself and has\n"
                "left the place thriving with customer.\n")
        while self._option != 6:
            shop = shops.Bakery()
            size = shop.getMenuSize()
            print("> Artisan Bakery:\n")
            shop.displayMenu()
            while True:
                try:
                    self._option = int(input("Enter menu choice: "))
                    exceptions.bounds(self._option, 1, size + 1)
                    if self._option == 6:
                        break
                    # Menu options are not displayed with an offset, so have to manually update
                    self._option -= 1
                    order = shop.order(self._option)
                    if not addToCart(shop, cart, order):
                            print("Couldn't add that item to your cart...")
                    break
                except exceptions.OutOfBounds as out:
                    print(out)
                except ValueError:
                    print("\nEnter a valid menu choice.\n")
        self._option = 0
        return


