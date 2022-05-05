X = [2, 3, 4, 6, 8]
Y = [4, 9, 16, 36, 64]
l = 0
x = 5
for i in range(len(X)):
    p = 1
    for j in range(len(X)):
        if i != j:
            p = p * (x - X[j]) / (X[i] - X[j])
    l = l + p * Y[i]

print(l)