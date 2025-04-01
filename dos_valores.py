

n = [252, 14, 58] 

for i in range(2):
    if n[i] > n[i+1]:
        n[i] = n[i+1] = n[i+1], n[i]
    

print(n)
         





