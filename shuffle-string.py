import itertools
from random import shuffle
from math import factorial

my_lst = [1, 2, 3, 4]
all_combinations = []
for r in range(len(my_lst) + 1):
    combinations_object = itertools.combinations(my_lst, r)
    combinations_list = list(combinations_object)
    all_combinations += combinations_list
    
print(all_combinations)

print(all_combinations[1])