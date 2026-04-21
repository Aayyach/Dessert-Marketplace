# Dessert Marketplace

This application uses a CLI to mimic popular food delivery apps like GrubHub and DoorDash, but it is specifically for desserts. There are three pre-determined shop types and a menu of items to choose from that users can interact with through the terminal. 

## Description

This application was built to get more practice in Python using Object-Oriented design principles and to learn how recursion works in Python. It uses a simple CLI to display the main menu, and four sub-menus consisting of three restaurants and a checkout menu. 

The cart is built using a binary search tree that currently allows users to add to their cart and display all items in the cart. Once a user enters a number for a sub-menu and decides that they want to order, they are given a series of prompts to create their order, which is ultimately added to their cart as an object. 

## Getting Started

### Dependencies

* Python 3.9+
* Pytest

### Installing

```
git clone https://github.com/Aayyach/Dessert-Marketplace.git
cd Dessert-Marketplace
```

### Executing program

* Enter the Dessert-Marketplace directory
* Run the command below

```
python3 -u main.py
```

## Notes

* PyTest test suite is only provided for the core hierarchy in shops.py.
* Delete functionality for the cart will be added later. 

## Authors

[@Aayyach](https://github.com/Aayyach)

## Acknowledgements

* [Coding Nomads](https://codingnomads.com/data-structure-python-binary-search-tree)