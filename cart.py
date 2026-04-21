import shops

class Node:
    def __init__(self, value: shops.Bakery | shops.BobaShop | shops.CoffeeShop):
        self._value = value
        self._left = None
        self._right = None

    def getValue(self) -> shops.Bakery | shops.BobaShop | shops.CoffeeShop:
        return self._value

    def getLeft(self) -> Node:
        return self._left
    
    def getRight(self) -> Node:
        return self._right
    
    def compare(self, value2) -> str:
        if value2 is None:
            return None
        # le stands for less than or equal to
        if value2 <= self._value:
            return "le"
        # g stands for greater than
        elif value2 > self._value:
            return "g"
        # e stands for equal to
        elif value2 == self._value:
            return "e"
        
    def swap(self, other) -> None:
        temp = self._value
        self._value = other._value
        other._value = temp
        
    def display(self, option):
        self._value.displayOrder(option)
    
class Tree:
    def __init__(self):
        self._root = None

    def count(self) -> int:
        if self._root is None:
            return 0
        return self._count(self._root)
        
    def _count(self, subtree) -> int:
        count = 0
        if subtree is None:
            return 0
        count += self._count(subtree.getLeft())
        count += 1
        count += self._count(subtree.getRight())
        return count

    def insert(self, value) -> bool: 
        """
        Objects in the tree are sorted by their main attribute (e.g. flavor for the Coffee
        and Boba shops, and the name of the menu item for the Bakery).
        """
        if self._root is None:
            self._root = Node(value)
            return True
        else:
            self._root = self._insert(self._root, value)
            return True
        
    def _insert(self, subtree, value):
        if subtree is None:
            subtree = Node(value)
            return subtree
        comp = subtree.compare(value)
        # less than or equal to
        if comp == "le":
            subtree._left = self._insert(subtree._left, value)
        # greater than
        if comp == "g":
            subtree._right = self._insert(subtree._right, value)
        return subtree

    def displayAll(self) -> bool:
        if self._root is None:
            return False
        self._displayAll(self._root, [0])
        return True

    def _displayAll(self, subtree, counter) -> None:
        if subtree is None:
            return 
        self._displayAll(subtree._left, counter)
        # Displays a number next to each object in the tree to make deletion easier
        counter[0] += 1
        print(f"{counter[0]}.", end=" ")
        subtree._value.displayOrder()
        self._displayAll(subtree._right, counter)