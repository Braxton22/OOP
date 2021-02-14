# Create Class
class RetailItem:
    # Set parameters
    def __init__(self, description, inventory, p):
        # Create attributes
        self.__itemdescription = description
        self.__unitsininventory = inventory
        self.__price = p

    # Retrieve description
    def get_description(self):
        return self.__itemdescription

    # Retrieve inventory level
    def get_inventory(self):
        return self.__unitsininventory

    # Retrieve price
    def get_price(self):
        return self.__price
