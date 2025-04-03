

n = [252, 14, 58] 

def swap(j):
  a = n[j] 
  n[j]= n[j + 1]
  n[j+1] = a



for i  in range(len(n)-2):    
    for j in range(len(n)-1):
        if n[j] > n[j + 1]:
            swap(j)

print(n)