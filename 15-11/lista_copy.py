
def sum_list(my_list):
    
    values = [] # added empty array
    list = open(my_list, 'r') #open list
    if (len(list)==0): #if list empty, return none
        print('None')
        return None
    for item in list: 
        values.append(item) #attach values of list into array
    
    sum(values)
    
