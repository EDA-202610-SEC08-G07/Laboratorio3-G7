

def new_list():
    new_list = {
        "elements": [],
        "size": 0,
    }
    return new_list

def add_first(my_list,element):
    my_list["size"] += 1
    if my_list["size"] != 0:
       my_list["elements"].insert(0,element)
    else:
       my_list["elements"].append(element)
    return my_list
    



def add_last(my_list,element):
    my_list["size"] += 1
    my_list["elements"].append(element)
    return my_list

     
def size(my_list):
    return my_list["size"]
    
    
def first_element(my_list):
    return my_list["elements"][0]
