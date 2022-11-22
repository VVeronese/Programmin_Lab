def sum_csv():
    file = open('list.csv','r')
    values = []
    for element in file:
        values.append(element)
    sum(float(values))
    if (len(values) == 0):
        return None
    else:
        return print(values)
    