
# ----- Importing Required Packages ----- #

import numpy as np
from numpy.random import randn

# ------ Start of Program ----- #

# Geting the sample size from user:

N = int(input("Please enter the sample size: "))

# Known Value

Ex = 0.682

# Declaring the counter seed

Counter = 0

for seed in range(N):
    RandomNum = randn()
    if (RandomNum >= -1 and RandomNum <= 1):
        Counter += 1
    else:
        pass

Mean = Counter / N

if Mean > Ex:
    print(f"The mean is {Mean} and it's greater than {Ex}")
else:
    print(f"The mean is {Mean} and it's less than {Ex}")
