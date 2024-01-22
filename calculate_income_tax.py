# Calculate income tax for the given income by adhering to the rules below
# First $10,000 is taxed at 0%, next $10,000 is taxed at 10%, remainder is taxed at 20%

# pseudocode

# get the taxable income from the user
taxable_income = int(input("Enter your income: "))

# calculate the tax based on the taxable income
# if the taxable income is less than 10000
#     tax = 0
# else if the taxable income is less than 20000
#     tax = 10000 * 0 + (taxable_income - 10000) * 0.1
# else
#     tax = 10000 * 0 + 10000 * 0.1 + (taxable_income - 20000) * 0.2

# print the tax
