def steigung_funktion(meine_Liste):
    x1 = meine_Liste[0] # 0 ist ein Index 
    y1 = meine_Liste[1]
    x2 = meine_Liste[2]
    y2 = meine_Liste[3]
    delta_x = x2 - x1 
    delta_y = y2 - y1
    
    if delta_x == 0:
        print("Die Steigung ist nicht definiert")
    else:
        steigung = delta_y / delta_x
        return steigung

test_list = [4, 4, 8, 7]

print(steigung_funktion(test_list))    
    
