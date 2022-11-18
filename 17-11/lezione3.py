values = [] 
my_file = open ('shanpoo_sales.csv', 'r')
for line in my_file:
    elements = line.split (',')
    if elements[0] != 'Date':
        date = elemnts[0]
        value = elements[1]
        values.append(value)