import random
pedido=[]

numero_pedido=random.randint(1,1000)
ruta=['Cliente','Comuna','Cantidad']


def crear_pedido (numero,nombre,apellido,comuna,detalle,cantidad):
    
    return{
        'numero' : numero,
        'nombre' : nombre,
        'apellido': apellido,
        'comuna' : comuna,
        'detalle' : detalle,
        'cantidad' : cantidad

    }




def registrar_pedido(pedido):
    nombre=input("Ingrese su Nombre :")
    apellido=input("Ingrese su Apellido :")
    comuna=input("Ingrese su Comuna :")
     
    print ("Opciones de Producto ")
    print ("1-Sacos de 5 kilos :")
    print ("2-Sacos de 10 kilos :")
    print ("3-Sacos de 20 kilos ")

    cantidad=int(input("Ingrese Cantidad de sacos :"))
    
    if not (nombre and apellido and comuna  and cantidad):
     print ("No se pudo realizar pedido , intente nuevamente ")
    
      

def listar_pedidos():
    print("n\ " ,"cliente","comuna","cantidad")
    pedido.append
    


def imprimir_ruta():
    
     print(numero_pedido,ruta)
     pedido.append
    
    
    
 

def salir_programa():
  print("fin programa")
   



while True:
    print("Bienvenidos a Catpremiun ")
    print("1-Registrar Pedido :")
    print("2- Listar Pedidos :")
    print("3- Imprimir Ruta :")
    print("4-Salir")



    opcion=int(input("Ingrese su Opcion: ")) 


    if opcion == 1 :
        registrar_pedido(pedido)
        
    if opcion== 2:
        listar_pedidos()

    if opcion == 3 :
        imprimir_ruta()
        
        
    if opcion == 4 :
        salir_programa() 
        break                         
    