from DataStructures.List import list_node as ln

def new_list():
    new_list = {
        "first": None,
        "last": None,
        "size": 0,
    }
    return new_list
def get_element(my_list,pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos :
        node = node["next"]
        searchpos += 1
    return node["info"]
def is_present(my_list,element,cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
    if not is_in_array:
        count = -1
    return count 
def add_first(my_list,element):
    my_list["size"] += 1
    new = ln.new_single_node(element)
    if my_list["first"] == None:
        my_list["first"] = new
        my_list["last"] = new
    else:
     new["next"] = my_list["first"]
     my_list["first"] = new

def add_last(my_list,element):
    
    new = ln.new_single_node(element)
    
    if my_list["size"] == 0:
        my_list["first"] = new
        my_list["last"] = new
    else:
        my_list["last"]["next"] = new
    my_list["size"] += 1
    return my_list
        
def is_empty(my_list):
    if my_list["size"] == 0:
        return True
    else:
        return False
    
def size(my_list):
    return my_list["size"]

def first_element(my_list):
    return["first"]
    
def last_element(my_list):
    return["last"]
        
        
        
        
    
        