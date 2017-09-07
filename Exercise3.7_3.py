import math

def calc_molecular_weight_carbohydrate(hydrogen_atom, carbon_atom, oxygen_atom):
    molecular_weight_carbohydrate = hydrogen_atom * 2 * 1.00794 + carbon_atom * 12.0107 + oxygen_atom * 15.9994
    print (molecular_weight_carbohydrate)
    return molecular_weight_carbohydrate
    
hydrogen_atom = eval(input("What is the number of hydrogen atoms?: "))
carbon_atom = eval(input("What is the number of carbon atoms?: "))
oxygen_atom = eval(input("What is the number of oxygen atoms?: "))

calc_molecular_weight_carbohydrate(hydrogen_atom, carbon_atom, oxygen_atom)