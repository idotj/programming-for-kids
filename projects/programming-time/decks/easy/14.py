# return the dice roll
def pick():
  return ⚂

a = [pick(), pick(), pick()]

# Sorting a list is quite common,
# the list object has a method
# `sort`, that sorts inplace, so it
# will just modify the list itself,
# without returning anything.
# After that the list will be sorted
# in ascending order (smaller
# numbers first).
a.sort()

# reverse does what it says, inplace
# it will reverse the list, it takes
# first and last elements and swaps
# them, then the second and
# pre-last, and so on. Inplace, so
# the list itself is modified. This
# is called mutating, like the
# teenage mutant ninja turtles, they
# changed from turtles to ninja
# turtles, so they mutated.
a.reverse()

print(a[0])
