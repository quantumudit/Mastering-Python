# ---- Importing required packages --- #

import numpy as np

# ---- Monthly Financial Data --- #

revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44,
           11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57,
            840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]

# ---- Financial Analysis --- #
# =========================== #

# Converting the given lists into Numpy arrays

Rev = np.array(revenue)
Exp = np.array(expenses)

# 1. Profit by Month

Profit = np.around(np.subtract(Rev, Exp), 2)

Profit_in_Thousands = np.around(Profit / 1000, 2)

print(f" Profit by Month (in '000s):\n {Profit_in_Thousands}\n")


# 2. Profit by Month after tax

TaxRate = 0.30

Profit_After_Tax = Profit * (1-TaxRate)
Profit_After_Tax = np.around(Profit_After_Tax, 2)

Profit_After_Tax_in_Thousands = np.around(Profit_After_Tax / 1000, 2)

print(
    f"Profit by Month after 30% Tax (in '000s):\n {Profit_After_Tax_in_Thousands}\n")

# 3. Profit Margin by Month

Profit_Margin = np.divide(Profit_After_Tax, Rev) * 100
Profit_Margin = np.around(Profit_Margin, 2)

print(f"Profit Margin by Month (in %):\n {Profit_Margin}\n")

# 4. Good & Bad Months

# Finding the mean profit after tax for the year:

Mean_Profit_After_Tax = np.around(np.mean(Profit_After_Tax), 2)

Mean_Profit_After_Tax_in_Thousands = round(Mean_Profit_After_Tax/1000, 2)

print(
    f"The Mean Profit after Tax for the year is : {Mean_Profit_After_Tax_in_Thousands}\n")

# Tagging the months as good/bad

Month_Status = list([])

for i in range(0, len(Profit_After_Tax)):
    if Profit_After_Tax[i] > Mean_Profit_After_Tax:
        Month_Status.append("Good")
    else:
        Month_Status.append("Bad")

print(f"Profitability status of months: \n {Month_Status}\n")

# 5. The best & worst months

Max_Profit = max(Profit_After_Tax)
Min_Profit = min(Profit_After_Tax)

for i in range(0, len(Profit_After_Tax)):
    if Profit_After_Tax[i] == Max_Profit:
        print(f"The best month is: {i+1}")
    elif Profit_After_Tax[i] == Min_Profit:
        print(f"The worst month is: {i+1}")
    else:
        pass
