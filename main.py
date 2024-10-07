# Step 1: Prompt the user to input their package
package = input("Enter your package (Green, Blue, Purple): ")

# Step 2: Continue to prompt until a valid package is entered
while package != "Green" and package != "Blue" and package != "Purple":
    print("Invalid package. Please try again!")
    package = input("Enter your package (Green, Blue, Purple): ")

# Step 4: Prompt the user to input the amount of data and store it in the variable GB
GB = float(input("Enter the amount of data used in GB: "))

# Step 5: Calculate the total bill based on the package selected
if package == "Green":
    fixed_cost = 49.99
    if GB > 2:
        excess_GB = GB - 2
        additional_charges = excess_GB * 15
        total_bill = fixed_cost + additional_charges
    else:
        total_bill = fixed_cost
    coupon = input("Do you have a coupon? (yes/no): ")
    if coupon == "yes" and total_bill >= 75:
        total_bill -= 20

elif package == "Blue":
    base_cost = 70
    if GB > 4:
        excess_GB = GB - 4
        additional_charges = excess_GB * 10
        total_bill = base_cost + additional_charges
    else:
        total_bill = base_cost

else:
    total_bill = 99.95  # Purple package: unlimited data

# Step 18: Display the total bill
print(f"Your total bill is: ${total_bill:.2f}")
