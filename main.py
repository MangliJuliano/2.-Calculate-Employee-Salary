salary = int(input("Enter the salary amount: "))

# Calculate the number of 50 euro notes needed
fifty_count = salary // 50 
salary %= 50

# Calculate the number of 20 euro notes needed
twenty_count = salary // 20
salary %= 20

# Calculate the remaining amount to be paid with 1s and 2s
one_count = salary // 1
two_count = (salary % 1) // 2

print("You need:")
print(f"{fifty_count} x 50 euro notes")
print(f"{twenty_count} x 20 euro notes")
print(f"{one_count} x 1 euro coins")
print(f"{two_count} x 2 euro coins")
