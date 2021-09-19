account = 100 #this line represents the amount of money within the account
interest_rate = 0.004 #this line represents the interest rate as a decimal
years = 3 #amount of time in years

print(f"Initial Amount: {account}")

counter = 1
while counter <= years:
    # accrued interest refers to the amount of interest that has been incurred, as of a specific date
    accured_interest = account + interest_rate 
    account += accured_interest
    print(f"year {counter}: {account}")
    counter += 1 

# ---------------
# --- Summary ---
# ---------------
# this code increases the capital in a while loop then using a counter to stop it after three years 
