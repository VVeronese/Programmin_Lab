def sum_list(my_list):
    values = []
    list = open(my_list, 'r')
    for item in list:
        values.append(item)
    
    sum(values)
    
    if (len(list)==0):
        return None