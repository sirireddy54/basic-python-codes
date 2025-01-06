weight= float(input("Weight: "))
unit = input("Kg or Lbs: ")
if unit.upper()=='K':
    converted_weight= weight/0.45
    print("Weight in Lbs: ", converted_weight)
else:
    converted_weight= weight*0.45
    print("Weight in Kg: ",converted_weight)