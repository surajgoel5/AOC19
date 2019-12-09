f=open("input_1.txt")

lines=[line for line in f]
code=[1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,9,23,1,23,13,27,1,10,27,31,2,31,13,35,1,10,35,39,2,9,39,43,2,43,9,47,1,6,47,51,1,10,51,55,2,55,13,59,1,59,10,63,2,63,13,67,2,67,9,71,1,6,71,75,2,75,9,79,1,79,5,83,2,83,13,87,1,9,87,91,1,13,91,95,1,2,95,99,1,99,6,0,99,2,14,0,0]
i=0
while True:
    
    if code[i]==1:
       code[code[i+3]]=code[code[i+1]]+code[code[i+2]]
    elif code[i]==2:
       code[code[i+3]]=code[code[i+1]]*code[code[i+2]]
    elif code[i]==99:
       break
    else:
        print("error")
        break
    i+=4
print(code)
