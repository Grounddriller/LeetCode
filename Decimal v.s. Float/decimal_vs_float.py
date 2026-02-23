# Floats are built into Python
# Decimal must be imported from the decimal module
from decimal import Decimal

print("---- FLOAT EXAMPLES ----")

a = 0.1
b = 0.2

# Addition
print("0.1 + 0.2 =", a + b)   #This is NOT exactly 0.3

# Subtraction
print("0.3 - 0.1 =", 0.3 - 0.1)

# Multiplication
print("0.1 * 0.2 =", 0.1 * 0.2)

# Division
print("1 / 3 =", 1 / 3)


print("\n---- DECIMAL EXAMPLES ----")

# IMPORTANT:
# Always pass strings into Decimal
# If you pass floats, you bring float precision error with you

x = Decimal("0.1")
y = Decimal("0.2")

# Addition
print("0.1 + 0.2 =", x + y)   # Correctly 0.3

# Subtraction
print("0.3 - 0.1 =", Decimal("0.3") - Decimal("0.1"))

# Multiplication
print("0.1 * 0.2 =", Decimal("0.1") * Decimal("0.2"))

# Division
print("1 / 3 =", Decimal("1") / Decimal("3"))