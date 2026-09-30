# MW, functions 

#round()
#len()
#print()

income = float(input("what is your monthly income: "))
rent = float(input("what is your monthley rent: "))
utilities = float(input("what is your mothley utilities: "))
groceries = float(input("what is your monthley grocieries: "))
transportation = float(input("what is your monthly transportation: "))

# functions  go seccond 
def calc_percent(bill, income):
    return round (bill/income * 100)

print(f"your rent is ${rent} which is {calc_percent(rent, income)}% of yopur income")
print(f"your rent is ${rent} which is {calc_percent(rent, income)}% of yopur income")
print(f"your rent is ${rent} which is {calc_percent(rent, income)}% of yopur income")
print(f"your rent is ${rent} which is {calc_percent(rent, income)}% of yopur income")
print(f"your rent is ${rent} which is {calc_percent(rent, income)}% of yopur income")
print(f"your rent is ${rent} which is {calc_percent(rent, income)}% of yopur income")
