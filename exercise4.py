quad_zahl = []

for zahl in range(1, 11):
    if zahl % 2 == 0:
        quad_zahl.append(zahl)
    else:
        quad_zahl.append(zahl**2)
        
print(quad_zahl)
