# Nawara Levonitis

# 3/1/2024

# P2LAB1

# mathematical calculations and displays information to users: Driving costs for the gas cost for 20 miles, 75 miles, and 500 miles.

#input miles, gas price, and calculate gas per miles
miles = float(input())
gas = float(input())
gas_per_miles = gas / miles

#calculate the prices for each miles 
price1 = gas_per_miles * 20
price2 = gas_per_miles * 75
price3 = gas_per_miles * 500

#out put the results
print(f'{price1:.2f} {price2:.2f} {price3:.2f}')