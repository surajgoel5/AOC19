f=open("input_1.txt")

lines=[line for line in f]
mass=0

for l in lines:
    n=int(l.strip())
    mass+=int(n/3)-2
print(mass)
