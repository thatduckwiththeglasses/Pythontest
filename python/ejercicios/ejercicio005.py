#5.Desarrollar una función que permita convertir un número romano en un número decimal

def romadecimal(numr):
    if len(numr) <= 0:
        return 0
    elif numr[len(numr)-1] == "M":
        num = (numr.count("M") * 1000)
        numr = numr.replace("M"," ")
        print(numr)
        return num + romadecimal(numr)
    elif numr[len(numr)-1] == "V":
        numr = numr.split(numr.replace(numr[len(numr)-1]," "))
        return 5 + romadecimal(numr)
    elif numr[len(numr)-1] == "X":
        numr = numr.split(numr.replace(numr[len(numr)-1]," "))
        return 10 + romadecimal(numr)
    elif numr[len(numr)-1] == "L":
        numr = numr.split(numr.replace(numr[len(numr)-1]," "))
        return 50 + romadecimal(numr)
    elif numr[len(numr)-1] == "C":
        numr = numr.split(numr.replace(numr[len(numr)-1]," "))
        return 100 + romadecimal(numr)
    elif numr[len(numr)-1] == "D":
        numr = numr.split(numr.replace(numr[len(numr)-1]," "))
        return 500 + romadecimal(numr)
    elif numr[len(numr)-1] == "I":
        numr = numr.split(numr.replace(numr[len(numr)-1]," "))
        return 1000 + romadecimal(numr)

print(romadecimal("CM"))