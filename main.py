import json
from decimal import Decimal
from pathlib import Path

#Inicializar las variables
path = Path("portafolioprueba.json") #Obtener el path del json

#Variables para saber el total invertido en los brokers 
total_invertido_GBM = Decimal("0")
total_invertido_Bitso = Decimal("0")



#Obtener la informacion de json para poder leerlo
with path.open("r", encoding = "utf-8") as f:
     data = json.load(f)


for account_name, account_data in data['accounts'].items(): #Este es path para recorrer cada tikcer que esta en cada holding
     holdings = account_data['holdings'] #Aqui le asignamos cada campo del json por cada iteracion EJEMPLO 
                                         #{ "ticker": "DANHOS13", "type": "FIBRA", "shares": 17, "avg_cost": 28.39}
                                          
     #Variables para aguardar el total de lo que se invierto en cada semana
     nota_actual = None #se declara None para que al principio no tenga nada
                       #ya que al principio de cada json hay una nota y pues el caso es que se imprima 
                       # el total de la semana cuando venga la segunda nota
     total_semana= Decimal("0")#Aqui aguardaremos el total de la semana

     for i, item in enumerate(holdings): #Aqui a la variable "i" le asiganremos el la longitud del json 
          es_ultimo = (i == len(holdings) -1 ) #Aqui verificaremos si es el ultimo holding
          if 'notes' in item:
               if nota_actual is not None:#Esta condicion es para saber si "nota_actual_gbm" tiene valor
                                          #si lo tiene imprimiremos el valor de "total_semana_gbm"
                   print("______________________________\n")
                   print(f'El total de la {primera_palabra} del {tercera_palabra} fue: {total_semana}')
                   print("______________________________\n")
               nota_actual = item['notes']
               #Estas variables son para agarrar la primera y ultima palabra que viene en 'notes'
               primera_palabra = nota_actual.split()[0]
               tercera_palabra = nota_actual.split()[2]
               total_semana= 0 #le damos el valor de 0 para que no se acomule la cantidad de cada semana
               print(f"\n{nota_actual}") #Imprimimos la nota actual
               continue

          total = Decimal(str(item["shares"])) * Decimal(str(item["avg_cost"])) #aqui calculamos el dinero total de ese ticker
          
          if account_name == 'GBM':
                #Aqui lo vamos sumando cada precio del ticker para saber cuanto fue lo que se invirtio
                total_invertido_GBM += total 
          else:
                total_invertido_Bitso += total

          total_semana += total #Aqui almacenamos la suma de la semana
          print (f'{item["ticker"]}: {item["shares"]} * {item["avg_cost"]} = {total:.2f}')
          if es_ultimo: #Aqui imprimiremos la semana total en dado caso que sea el ultimo holding y despues de este no venga un "notes"
               print("______________________________\n")
               print(f'El total de la {primera_palabra} del {tercera_palabra} fue: {total_semana}')
               print("______________________________\n")

     if account_name == 'GBM':
                print("_________________________________\n")
                print(f'Total invertido en GBM es : {total_invertido_GBM}')
                print("_________________________________\n") 
     else: 
                print("_________________________________\n")
                print(f'Total invertido en Bitso es : {total_invertido_Bitso}')
                print("_________________________________\n")  

print("_________________________________\n")
print(f'Total invertido es: {total_invertido_Bitso + total_invertido_GBM}')
print("_________________________________\n")




     




