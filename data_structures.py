grades = {
    "Calculus" : 87,
    "Comm Skills" : 90,
    "Intro IT" : 90
}
#Manual Printing
print(grades["Calculus"])

print(grades["Comm Skills"])

print(grades["Intro IT"])
#OR
for i in grades:
    print(f"{i}: {grades[i]}")

Cars = {
    "Lamborghni" : 2000000,
    "Escalade" : 300000,
    "Audi" : 250000,
    "Mercedes" : 300000
    }
for a in Cars:
    print(f"{a}:{Cars[a]}")

Shopping = ["Books", "Clothes", "Bags", "Cars"]
print(Shopping[2])

Grabbies = ('20', 'bottles', 'cars')
print(Grabbies)
Grabbies = (30)

Fig = 1
Multipler = 1
while Fig <= 12:
    print(f"{Fig} times table")
    print("\n")
    while Multipler <= 12:
        print(f"{Fig}*{Multipler} = {Fig*Multipler}")
        Multipler += 1

    Fig += 1
    Multipler = 1
    print("\n")        
       

















# Notes
#list ; datatype: all, mutability: true, access:bracket, representation:[], for ordered output
#tuple; datatype: all, mutability: false, access:bracket, representation:()
#dict: datatype: all, mutuability: true, access:key, representation:{}, 
