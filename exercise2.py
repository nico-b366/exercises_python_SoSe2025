def teilbar(x, y):
    if y == 0:
        print("Division durch 0 nicht möglich.")
    elif y == x:
        print("x und y sind gleich")
    else: 
        if x%y == 0 :
            print(x, "ist teilbar durch", y)
        else:
            print(x, "ist nicht teilbar durch", y)
            
print(teilbar(10, 5))

