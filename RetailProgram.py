# Import class file
import RetailItemClass as ri

# Create variables to format the price
PriceFormat = "${:,.2f}"
JacketPrice = 59.95
JeanPrice = 34.95
ShirtPrice = 24.95
# Create instances of the class for a jacket, a pair of jeans and a shirt with their respective inventory level and price. Use formatted price variables.
Item1 = ri.RetailItem("Jacket", 12, PriceFormat.format(JacketPrice))
Item2 = ri.RetailItem("Designer Jeans", 40, PriceFormat.format(JeanPrice))
Item3 = ri.RetailItem("Shirt", 20, PriceFormat.format(ShirtPrice))

# Print the jacket name, inventory level and price with correct spacing
print(
    "Item:",
    " ",
    Item1.get_description(),
    "\n",
    "Inventory Level:",
    " ",
    Item1.get_inventory(),
    " ",
    "units",
    "\n",
    "Price:",
    " ",
    Item1.get_price(),
    sep="",
)
# Line break
print()
# Print the jeans name, inventory level and price with correct spacing
print(
    "Item:",
    " ",
    Item2.get_description(),
    "\n",
    "Inventory Level:",
    " ",
    Item2.get_inventory(),
    " ",
    "units",
    "\n",
    "Price:",
    " ",
    Item2.get_price(),
    sep="",
)
# Line break
print()
# Print the shirt name, inventory level and price with correct spacing
print(
    "Item:",
    " ",
    Item3.get_description(),
    "\n",
    "Inventory Level:",
    " ",
    Item3.get_inventory(),
    " ",
    "units",
    "\n",
    "Price:",
    " ",
    Item3.get_price(),
    sep="",
)