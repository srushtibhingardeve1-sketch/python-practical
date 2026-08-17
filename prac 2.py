print("--------Grocery Shop Detail ------------")
total=0

n=int(input("Enter your items : "))


name =input("Enter your item name :")
price = float(input("Enter price :"))
quanity1= float(input("Enter Quanity :"))
amount1=price*quanity1
total+=amount1

n=int(input("Enter your items : "))


name =input("Enter your item name :")
price = float(input("Enter price :"))
quanity2= float(input("Enter Quanity :"))
amount2=price*quanity2
total+=amount2

n=int(input("Enter your items : "))


name =input("Enter your item name :")
price = float(input("Enter price :"))
quanity3= float(input("Enter Quanity :"))
amount3=price*quanity3
total+=amount3

price=amount1+amount2+amount3
quanity=quanity1+quanity2+quanity3
total=amount1+amount2+amount3

print("--------------- Bill -------------------")

print("Enter price :",price )
print("Enter quanity :",quanity)

print("---------------TOTAL AMOUNT---------------")
print("Total Amount :",total)
print("============THANK YOU =============")