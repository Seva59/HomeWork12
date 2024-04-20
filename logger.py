from data_create  import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data ( )
    phone = phone_data ( )
    address = address_data()
    var = int(input(f"Какой формат вам больше нравиться ? \n\n"
    f" 1) Вариант : \n "
    f" {name}\n {surname}\n {phone}\n  {address}\n\n"
    f"2) Вариант : \n"
    f" {name};{surname};{phone};{address}\n"
    f" Выберите  :  " ))
    while var !=1 and var  !=2 :
        print( " Введите коректные данные ")
        var = int(input("print number "))
    if var==1 :
        with open ("data_first_variant.csv" , "a", encoding = "utf-8 ") as f:
            f.write(f" {name}\n {surname}\n {phone}\n  {address}\n\n")
    elif var==2 :
        with open ("data_first_variant.csv" , "a", encoding = "utf-8 ") as f:
            f.write(f" {name};{surname};{phone};{address}\n")            
    
input_data()

def print_data():
    pass
