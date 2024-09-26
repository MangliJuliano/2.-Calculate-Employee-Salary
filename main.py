salary = int(input("Enter the salary amount: "))

# Calculate the number of 50 euro notes needed
fifty_count = salary // 50 
salary %= 50

# Calculate the number of 20 euro notes needed
twenty_count = salary // 20
salary %= 20

# Calculate the number of 2 euro coins needed
two_count = salary // 2
salary %= 2

# Calculate the number of 1 euro coins needed
one_count = salary

print("You need:")
print(f"{fifty_count} x 50 euro notes")
print(f"{twenty_count} x 20 euro notes")
print(f"{two_count} x 2 euro coins")
print(f"{one_count} x 1 euro coins")
