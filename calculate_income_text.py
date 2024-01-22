# Calculate income tax for the given income by adhering to the rules
# First 10000 is 0 tax, the next 10000 is 10% tax, the remaining is 20% tax

# pseudocode

# ask user for taxable income
taxable_income = int(input("Enter your taxable income: "))

# if income is less than 10000
if taxable_income < 10000:
    tax = 0

# else if income is less than 20000
elif taxable_income < 20000:
    tax = (taxable_income - 10000) * 0.1

# else
else:
    tax = 10000 * 0 + 10000 * 0.1 + (taxable_income - 20000) * 0.2

# print the tax
