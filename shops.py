import exceptions

# ***** Base class *****
class Restaurant:
    def __init__(self, name: str, menu: tuple[str]):
        self._name = name
        self._menu = menu

    def display(self, items) -> None:
        index = 1
        for item in items:
            if index == 1:
                print(f"\n\t{index}. {item}")
            else:
                print(f"\t{index}. {item}")
            index += 1

    def displayMenu(self) -> None:
        size = self.getMenuSize()
        self.display(self._menu)
        print(f"\t{size + 1}. Return to main menu\n")

    def getMenuSize(self) -> int:
        return len(self._menu)

    def getChoice(self, options: tuple[str], prompt: str) -> int:
        raw = ""
        choice = -1
        while True:
            try:
                if choice == -1:
                    self.display(options)
                    raw = input(f"\n\t{prompt} ")
                    exceptions.empty(raw)

                    choice = int(raw)
                    exceptions.bounds(int(choice), 1, len(options))
                break
            except exceptions.EmptyInput as emp:
                choice = -1
                print(emp)
            except exceptions.OutOfBounds as out:
                choice = -1
                print(out)
            except ValueError:
                choice = -1
                print(f"\n{choice} is not a valid choice.\n")
        return choice - 1

# ***** Derived classes *****
class CoffeeShop(Restaurant):
    def __init__(self, flavors: tuple[str], sizes: tuple[str], temps: tuple[str]):
        super().__init__("Fresh Roasters", ("Latte", "Cappucino", "Americano", "Matcha"))
        self._flavors = flavors
        self._sizes = sizes
        self._temps = temps
        self._item = None
        self._flavor = None
        self._size = None
        self._temp = None

    def __lt__(self, other):
        try:
            return self._flavor < other._flavor
        except TypeError:
            return self._flavor < str(other._flavor)
    
    def __le__(self, other):
        try:
            return self._flavor <= other._flavor
        except TypeError:
            return self._flavor <= str(other._flavor)

    def __gt__(self, other):
        try:
            return self._flavor > other._flavor
        except TypeError:
            return self._flavor > str(other._flavor)
        
    def __eq__(self, other):
        """
        Created for the retrieval/deletion function in the BST. 
        Uses the flavor and menu item to search for a match.
        """
        if self._flavor == other._flavor and self._item == other._item:
            return True
        return False

    def displayFlavors(self) -> None:
        self.display(self._flavors)

    def displaySizes(self) -> None:
        self.display(self._sizes)

    def displayTemps(self) -> None:
        self.display(self._temps)

    def displayOrder(self) -> None:
        print(f"{self._temp} {self._flavor} {self._size} {self._item}\n")

    def order(self, option) -> CoffeeShop:
        flavor = self.getChoice(self._flavors, "Choose flavor: ")
        size = self.getChoice(self._sizes, "Choose size: ")
        temp = self.getChoice(self._temps, "Choose temperature: ")
        self._item = self._menu[option]
        self._flavor = self._flavors[flavor]
        self._size = self._sizes[size]
        self._temp = self._temps[temp]
        return self
        
class BobaShop(Restaurant):
    def __init__(self, flavors: tuple[str], sizes: tuple[str], sweetness: tuple[str], boba: tuple[str]):
        super().__init__("Best Boba", ("Milk Tea", "Fruit Tea", "Mojito", "Smoothie"))
        self._flavors = flavors
        self._sizes = sizes
        self._sweetness = sweetness
        self._addBoba = boba
        self._item = None
        self._flavor = None
        self._size = None
        self._lvl = None
        self._add = None

    def __lt__(self, other):
        try:
            return self._flavor < other._flavor
        except TypeError:
            return self._flavor < str(other._flavor)
    
    def __le__(self, other):
        try:
            return self._flavor <= other._flavor
        except TypeError:
            return self._flavor <= str(other._flavor)

    def __gt__(self, other):
        try:
            return self._flavor > other._flavor
        except TypeError:
            return self._flavor > str(other._flavor)
        
    def __eq__(self, other):
        """
        Created for the retrieval/deletion function in the BST. 
        Uses the flavor and menu item to search for a match.
        """
        if self._flavor == other._flavor and self._item == other._item:
            return True
        return False

    def displayFlavors(self) -> None:
        self.display(self._flavor)

    def displaySizes(self) -> None:
        self.display(self._sizes)

    def displaySweetness(self) -> None:
        self.display(self._sweetness)

    def displayOrder(self) -> None:
        if self._add == "n":
            print(f"{self._size} {self._flavor} {self._item}, {self._lvl} sweet with no boba\n")
        else:
            print(f"{self._size} {self._flavor} {self._item}, {self._lvl} sweet with boba\n")

    def order(self, option) -> BobaShop:
        flavor = self.getChoice(self._flavors, "Choose flavor: ")
        size = self.getChoice(self._sizes, "Choose a size: ")
        sweetness = self.getChoice(self._sweetness, "Choose sweetness level: ")
        addBoba = self.getChoice(self._addBoba, "Do you want to add brown sugar boba (y/n): ")
        self._item = self._menu[option]
        self._flavor = self._flavors[flavor]
        self._size = self._sizes[size]
        self._lvl = self._sweetness[sweetness]
        self._add = self._addBoba[addBoba]
        return self

class Bakery(Restaurant):
    def __init__(self):
        super().__init__("Artisan Bakery", ("Crossiant", "Danish", "Madeline", "Coconut Macaroon", "Chocolate Chip Cookie"))
        self._order = ""
        self._amount = 0
        self._warmed = False

    def wantWarmed(self) -> bool:
        warmed = ""
        while not warmed:
            try:
                warmed = input("Would you like your desserts warmed? (y/n): ")
                exceptions.empty(warmed)
                if warmed.lower() != 'y' and warmed.lower() != 'n':
                    warmed = ""
                    print("Valid choices are \'y\' and \'n\'.")
                    continue
            except exceptions.EmptyInput as empty:
                print(empty)
            if warmed == 'y':
                return True
            return False 
  
    def __lt__(self, other):
        try:
            return self._order < other._order
        except TypeError:
            return self._order < str(other._order)
    
    def __le__(self, other):
        try:
            return self._order <= other._order
        except TypeError:
            return self._order <= str(other._order)
        except AttributeError:
            return self._order <= other._flavor

    def __gt__(self, other):
        try:
            return self._order > other._order
        except TypeError:
            return self._order > str(other._order)  
        except AttributeError:
            return self._order > other._flavor 

    def __eq__(self, other):        
        """
        Created for the retrieval/deletion function in the BST. 
        Uses the amount and menu item to search for a match.
        """
        if self._order == other._order and self._amount == other._amount:
            return True
        return False
   
    def displayOrder(self) -> None:
        if self._warmed == "y":
            print(f"{self._amount} {self._order}, Warmed\n")
        print(f"{self._amount} {self._order}\n")
    
    def order(self, order) -> Bakery:
        #order = self.getChoice(self._menu, "\nEnter menu choice: ")
        self._order = self._menu[order]
        while self._amount == 0:
            try:
                self._amount = int(input("Enter amount: "))
                if self._amount <= 0:
                    raise ValueError
            except ValueError:
                self._amount = 0
                print("Please enter a valid number.")
        self._warmed = self.wantWarmed()
        return self




    