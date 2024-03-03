print("enter the weight")
weight = int(input());

print("In which way you want kilos or pounds")

unit = input();

if(unit.upper() == 'L'):
    kilos = weight*0.45;
    print("Weigth in kilos ->" , kilos);
else :
    pu = weight/0.45
    print("weight in pf" , pu)
