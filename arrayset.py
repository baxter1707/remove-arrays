
names = ["Alex","Mary","Steve","John","Seinfeld","Alan","Jane"]


namesToRemove = ["Steve","Alan"]

names_set = set(names)
namesToRemove_set = set(namesToRemove)

print(names_set)
print(namesToRemove_set)

delta_set = names_set - namesToRemove_set
print(delta_set)

names_delta_set = list(delta_set)
print(names_delta_set)
