# Follow the assignment instructions to code an app that
# will tell a user their birthstone.
print("*" * 30)
user_input = input("Enter the number of the moth you were born (1-12)")
month = int(user_input)
if month == 1:
    birth_stone = 'garnet'
elif month == 2:
    birth_stone = 'amethyst'
elif month == 3:
    birth_stone = 'bloodstone'
elif month == 4:
    birth_stone = 'diamond'
elif month == 5:
    birth_stone = 'emerald'
elif month == 6:
    birth_stone = 'pearl'
elif month == 7:
    birth_stone = 'ruby'
elif month == 8:
    birth_stone = 'peridot'
elif month == 9:
    birth_stone = 'sapphire'
elif month == 10:
    birth_stone = 'opal'
elif month == 11:
    birth_stone = 'topaz'
elif month == 12:
    birth_stone = 'tanzanite'
else:
    birth_stone = "NA"
if birth_stone == "NA":
    print("Numeric Month Entered is not within the (1-12) range, please try again")
else:
    print(f"Your birthstone is: {birth_stone}")
# BRYAN FUDALA - CIDM 6303
