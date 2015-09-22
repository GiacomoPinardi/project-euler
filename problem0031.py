# www.github.com/GiacomoPinardi/project-euler

# In England the currency is made up of pound, P, and pence, p,
# and there are eight coins in general circulation:

#     1p, 2p, 5p, 10p, 20p, 50p, P1 (100p) and P2 (200p).

# It is possible to make P2 in the following way: 1xP1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p

# How many different ways can P2 be made using any number of coins?

def compose (array):
    array = sorted(array)
    n = 0
    for m in money:
        for i in range(0, len(array)):            
            if len(array) > 1:
                if m == sum(array[:i+2]):
                    tmp = array
                    del tmp[:i+1]
                    tmp[0] = m
                    tmp = sorted(tmp)
                    if tmp not in combinations:
                        combinations.append(tmp)        
                        n += 1 + compose(tmp)

    return n


# Main

money = [2, 5, 10, 20, 50, 100, 200]

array = [1] * 200

combinations = []

print compose(array) + 1

#