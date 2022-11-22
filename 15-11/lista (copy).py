def sum_list(my_list):
    values = [] # added empty array
    list = open('my_list', 'r') #open list
    for item in list: 
        values.append(item) #attach values in in list into array
    
    sum(values)
    
    if (len(list)==0): #if list empty, return none
        return None