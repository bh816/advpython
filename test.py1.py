# Simple interst Calculation 

def simple_interst(p,n,r):
    i=(p*n*r)/100
    amt = p + i
    return{ "interst":i ,"amount":amt}

# Take input from users in console
p = float(input("Please enter Principle in INR :"))
n = int(input("Please enter number of Years : "))
r = float(input("Please enter rate of Interst in %p.a : "))

#calculate interst and amount 
results = simple_interst(p, n, r)

#Print the Results
print(results)