class EmptyInput(Exception):
    pass

class OutOfBounds(Exception):
    pass

def empty(userInput) -> None:
    if userInput == "":
        raise EmptyInput("\nField cannot be left empty.")
    
def bounds(userInput, lower: int, upper: int):
    if userInput < lower or userInput > upper:
        raise OutOfBounds(f"\n{userInput} is not a valid choice.\n")