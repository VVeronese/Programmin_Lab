#
def sum_csv(my_file):
    file = open (my_file, 'r') #apro my_file nella funzione
    values = [] 
    total = 0
   
    for line in file:
        
        elements = line.split (',')  #split degli elementi nel file
        if elements[0] != 'Date':
            date = elements[0]
            value = elements[1]
        
            values.append(float(value)) #trasformo i valori in float
    
    if len(values) == 0:  #se my_file è vuoto
            return None
    for value in values:  #sommo i valori in variabile total
        total += value
   

    return total
    

