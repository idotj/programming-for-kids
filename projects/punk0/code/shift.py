# shifts the list to the left
# adding 0 to the end
#   [2,3,4,5]
# returns:
#   [3,4,5,0]
def shift(x):
    r = []
    for i in range(1, len(x)):
        v = x[i]
        r.append(v)

    r.append(0)
    return r


print(shift([1, 1, 2, 3, 3, 4, 1, 2, 7, 9]))
