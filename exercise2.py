def teilbar(x, y):
    if y == 0:
        print("Es ist nicht möglich durch 0 zu teilen")
    elif y == x:
        print("x und y sind gleich")
    else:
        if x%y == 0:
            print(x, "ist teilbar durch", y)
        else:
            print(x, "ist nicht teilbar durch", y)
        
teilbar(10, 10)
