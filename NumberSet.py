my_set = {1,3,2,44,4,4,4,4,5}
print("Set: ", my_set)

my_set.add(5)
print("Updated set: ", my_set)

set1 = my_set
set2 = {2,3,4,5,4,4,6}

print("\nSet 1", set1)
print("Set 2", set2)
print("Difference")
print(set1.difference(set2))
print("Symmetric difference")
print(set1.symmetric_difference(set2))