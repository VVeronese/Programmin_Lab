class CSVFile():
    
    def __init__(self, name):
        self.name = name #attributo che contiene il nome 
    def get_data(my_file):
        file = open (my_file, 'r') #apro my_file nella funzione
        values = []
        for line in file:
            lines = line.split ('\n')  #split delle linee nel file
            lines.append(list(values)) #ritorno ogni linea in una lista
        return values; #ritorno le liste
        
   
   
    