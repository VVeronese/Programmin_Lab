class CSVFile():
    
    def __init__(self, name):
        
        self.name = name #attributo che contiene il nome 
        
    def get_data(self, my_file):
       
        file = open (my_file, 'r') #apro my_file nella funzione
        lists = []
        for line in file:
            lines = line.split()  #split delle linee nel file
            item = lines
            lists.append(item) #ritorno ogni linea in una lista
        return lists; #ritorno le liste

#CSVFile().get_data('shampoo_sales.csv') test con shampoo_sales
   
    