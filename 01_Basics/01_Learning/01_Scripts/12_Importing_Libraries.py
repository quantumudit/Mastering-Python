# Importing Libraries #
# =================== #

# Importing pre-installed regEx library

import re

str = "'I'M NOT SCREAMING... She said; But, we all know that the place was HAUNTED !!!."

rmvUpperCases = re.sub("[A-Z]", "", str)
rmvOdds = re.sub("[.,!a-zA-Z]", "", str)

print(rmvUpperCases)
print(rmvOdds)
