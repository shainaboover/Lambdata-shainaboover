
from pandas import DataFrame

print('Hello')

# import enlarge function
from my_lambdata.my_mod import enlarge

# invoke function
print(enlarge(8))


df = DataFrame({'state': ['CT', 'CO', 'CA', 'TX']})
print(df.head(2))