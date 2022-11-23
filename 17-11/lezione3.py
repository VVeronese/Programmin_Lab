# my_file = open ('shampoo_sales.csv', 'r')
def sum_csv(my_file):
    values = [] 
    total = "0"
   
    for line in my_file:
        elements = line.split (',')
        if elements[0] != 'Date':
            date = elements[0]
            value = elements[1]
        
            values.append(value)

    for value in values:
        total += value

    return total
    

