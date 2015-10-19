# www.github.com/GiacomoPinardi/project-euler

# If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p <= 1000, is the number of solutions maximised?

# Main

result = 0
maxSolution = 0

for i in range(4, 1001, 2):
    sol = 0    
    for j in range(1, i-2):        
        for k in range(j, i-j-1):
            data = sorted([j, k, i-(j+k)])
            if (data[0]**2 + data[1]**2 == data[2]**2):
                sol += 1

    if maxSolution < sol:
        result = i
        maxSolution = sol

print result

#