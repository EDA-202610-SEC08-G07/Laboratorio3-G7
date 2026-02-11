from DataStructures.List import array_list as al

def new_list():
    new_list = {
        "elements": [],
        "size": 0,
    }
    return new_list

def add_first(my_list,element):
   
    


# Agrega un elemento al inicio
    my_list = al.add_first(my_list,element )
    print(my_list)

def add_last(my_list,element):
    


    my_list = al.add_first(my_list, element)
    print(my_list)

def size(my_list):
    print(al.size(my_list))
    
    
def first_element(my_list):
    print(al.first_element(my_list))
