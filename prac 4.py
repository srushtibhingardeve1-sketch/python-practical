print("***************************** Traffic signal simulation system****************************")
signal =input("Enter a signal color :").lower()

if signal=="red":
    print("signal is red")
    print("action : STOP ")

elif signal=="yellow":
    print("signal is yellow")
    print("action : GET READY ")

elif signal=="green":
    print("signal is green")
    print("action : GO ")

else:
    print("Invalid color enter red,yellow,green :")
