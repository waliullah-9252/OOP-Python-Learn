def full_name(first,last):
    name = f'Full name is : {first} {last}'
    return name

# take name paramenters in order or serial wise

# name = full_name('Kodom' , 'Ali')
# name = full_name(first='Kodom',last='Ali')
name = full_name(last='Ali',first='Kodom')
# print(name)

# famous name 
def famous_name(first,last,**addition):
    name = f'The famous name is : {first} {last}'
    print(addition)
    for key,value in addition.items():
        print(key,value)
    return name

name = famous_name(first='Abduls',last='Salam',title='Doctor',addition='Md.',title2='Shayek',last2='alhadisi')
print(name)

#return multiple values
def a_lot(num1,num2):
    summation = num1 + num2
    multi = num1 * num2
    sub = num1 - num2
    divid = num1 / num2
    remainder = num1 % num2
    return summation,multi,sub,divid,remainder
    # return [summation,multi,sub,divid,remainder]

everything = a_lot(7,5)
print(everything)

def display_person(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")


display_person(Name="Amir Khan", Age="45")