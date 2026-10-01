'''
This function will convert values given in kilograms to pounds and ounces

Argument:
value - the integer or float in kilograms that the user wants converted

Returns: None (Will print the conversions out in the function instead)
'''
def convert_kg(value):
    # Converts kg to lb
    kg_to_pounds = value * 2.20462
    print(str(value) + " kilograms is " + str(kg_to_pounds) + " pounds.")

    # Converts kg to oz
    kg_to_oz = value * 35.274
    print(str(value) + " kilograms is " + str(kg_to_oz) + " ounces.")


'''
This function will convert values given in pounds to kilograms and ounces

Argument:
value - the integer or float in pounds that the user wants converted

Returns: None (Will print the conversions out in the function instead)
'''
def convert_pounds(value):
    # Converts lb to kg
    lb_to_kg = value * 0.453592
    print(str(value) + " pounds is " + str(lb_to_kg) + " kilograms.")

    # Converts lb to oz
    lb_to_oz = value * 16
    print(str(value) + " pounds is " + str(lb_to_oz) + " ounces.")


'''
This function will convert values given in ounces to kilograms and pounds

Argument:
value - the integer or float in ounces that the user wants converted

Returns: None (Will print the values out in the function instead)
'''
def convert_ounces(value):
    # Converts oz to kg
    oz_to_kg = value * 0.0283
    print(str(value) + " ounces is " + str(oz_to_kg) + " kilograms.")


    # Converts oz to lb
    oz_to_lb = value * 0.0625
    print(str(value) + " ounces is " + str(oz_to_lb) + " pounds.")


#Challenge: Extend you code to include conversions for liquid measurements such as fluid ounces, litres, pints, and quarts


'''
This function will convert values given in US fluid ounces to liters, US pints, and US quarts

Argument:
value - the integer or float in US fluid ounces that the user wants converted

Returns: None (Will print the values out in the function instead)
'''
def convert_floz(value):
    # Converts floz to l
    floz_to_l = value * 0.0295735
    print(str(value) + " US fluid ounces is " + str(floz_to_l) + " liters.")

    # Converts floz to pt
    floz_to_pt = value * 0.0625
    print(str(value) + " US fluid ounces is " + str(floz_to_pt) + " US pints.")

    # Converts floz to qt
    floz_to_qt = value * 0.03125
    print(str(value) + " US fluid ounces is " + str(floz_to_qt) + " US quarts.")


'''
This function will convert values given in liters to US fluid ounces, US pint, and US quarts

Argument:
value - the integer or float in liters that the user wants converted

Returns: None (Will print the values out in the function instead)
'''
def convert_liters(value):
    # Converts l to floz
    l_to_floz = value * 33.814
    print(str(value) + " liters is " + str(l_to_floz) + " US fluid ounces.")

    # Converts l to pt
    l_to_pt = value * 2.11338
    print(str(value) + " liters is " + str(l_to_pt) + " US pints.")

    # Converts l to qt
    l_to_qt = value * 1.05669
    print(str(value) + " liters is " + str(l_to_qt) + " US quarts.")


'''
This function will convert values given in US pints to US fluid ounces, liters, and US quarts

Argument:
value - the integer or float in US pints that the user wants converted

Returns: None (Will print the values out in the function instead)
'''
def convert_pints(value):
    # Converts pt to floz
    pt_to_floz = value * 16
    print(str(value) + " US pints is " + str(pt_to_floz) + " US fluid ounces.")

    # Converts pt to l
    pt_to_l = value * 0.473176
    print(str(value) + " US pints is " + str(pt_to_l) + " liters.")

    # Converts pt to qt
    pt_to_qt = value * 0.5
    print(str(value) + " US pints is " + str(pt_to_qt) + " US quarts.")


'''
This function will convert values given in US quarts to US fluid ounces, US pint, and liters

Argument:
value - the integer or float in US quarts that the user wants converted

Returns: None (Will print the values out in the function instead)
'''
def convert_quarts(value):
    # Converts qt to floz
    qt_to_floz = value * 32
    print(str(value) + " US quarts " + str(qt_to_floz) + " US fluid ounces.")

# Converts qt to l
    qt_to_l = value * 0.946353
    print(str(value) + " US quarts " + str(qt_to_l) + " liters.")

# Converts qt to pt
    qt_to_pt = value * 2
    print(str(value) + " US quarts " + str(qt_to_pt) + " US pints.")


if __name__ == "__main__":
    # Test your code here
    convert_kg(10)
    convert_pounds(10)
    convert_ounces(10)

    # Test challenge code here
    print("\n--- Challenge ---")
    convert_floz(10)
    convert_liters(10)
    convert_pints(10)
    convert_quarts(10)

