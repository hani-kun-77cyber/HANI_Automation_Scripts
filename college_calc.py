# 1. Define a Welcome Message using the print() function
print("===================================")
print("💰 Simple College Budget Calculator 💰")
print("===================================")

# 2. Get User Input (Asking the user for a value)
# The input() function asks a question and stores the answer in a VARIABLE.
# The float() function converts the input string into a number (decimal).

income = float(input("Enter your Monthly Income (e.g., from part-time work): "))
fees = float(input("Enter your Monthly Hostel/Fixed Fees: "))

# 3. Process the Data (Calculation)
# Calculate the remaining budget and store it in a new variable.

budget_left = income - fees

# 4. Display the Results (Outputting the variables)
print("\n--- Summary ---")
print(f"Total Income: ₹{income:.2f}")
print(f"Total Fixed Fees: ₹{fees:.2f}")
print("-----------------")
print(f"Your Remaining Budget is: ₹{budget_left:.2f}")
print("-----------------")

# Simple Conditional Logic (Your first Python if/else)
if budget_left < 5000:
    print("Warning: Budget is low! Focus on expense tracking.")
else:
    print("Budget is healthy. Keep track of discretionary spending!")
