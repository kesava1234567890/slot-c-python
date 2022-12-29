b=int(input("enter the value of b"))
if b<150 :
    charge=b*150
    print("Rs 2 per unit")
elif b>150 and b<300 :
    charge=b*300
    print("Rs 100+Rs 3 per unit")
elif b>300 and b<450 :
    charge=b*450
    print("Rs 250+Rs 4 per unit")
elif b>450 :
    charge=b*600
    print("Rs 300+Rs 5 per unit")
else :
    print("charge")
    
