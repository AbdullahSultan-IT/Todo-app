feet_inch = input("enter feet and inches")

def parse (feet_inch):
    
    part = feet_inch.split(" ")
    m = float(part[0])
    i = float(part[1])
    return m , i
    


def convert(m , i):
    
    matars = m * 0.30 + i * 0.02
    return matars



m , i = parse(feet_inch)
 
resulst = convert(m , i)

print(resulst)