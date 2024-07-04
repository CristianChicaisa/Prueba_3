import os
os.system("cls")

lista = []

def datos():
    print("Datos de la Identificacion Fiscal")
    v_nombre = input("Ingrese nombre y apellido: ")
    if v_nombre >= str(8) :
        print()
            
        print("El nombre tiene que contener Nombre y Apellido (ejemplo: Alejandro Leal))")
    else:
        print()     
    v_edad = int(input("Ingrese edad: "))
    if v_edad <= 0:
        print("Edad invalida")
        
    v_nif = float(input("Ingrese nif: "))       
    if v_nif >= 99999999 or v_nif < 999999999 :
        print("El NIF debe contener 8 digitos guion y 3 caracteres (ejemplo: 99999999-RTX o 00000000-03F)")
        
    v_nacimiento = float(input("Ingrese Fecha de Nacimiento: "))
    if v_nacimiento > 0 or v_nacimiento < 3000:
        print()
    v_estado = input("Ingrese Estado Conyugal: ")
    v_pertenencia = int(input("Ingrese (NIF/RUT/RUN): "))
    
     
    lista.append(lista)
    lista = (v_nombre,v_edad,v_nif,v_nacimiento,v_estado,v_pertenencia)
    return



def buscar():
    print("NIF de la persona que decea buscar ")
    buscar_nif = input("Ingrese NIF de la persona: ")
    v_nif =[0] in buscar_nif
    if lista():
        print("NIF Encontrado")
        print(f"Nombre de la persona: ['v_nombre']")
        print(f"Edad de la persona: ['v_edad']")
        print(f"NIF de la persona: ['v_nif']")
        print(f"Fecha de Nacimiento: ['v_nacimiento']")
        print(f"Estado Conyugal: ['v_estado']")
        print(f"Pertenencia: ['v_pertenencia']")
    else:
        print(f"{v_nif} no se encuentra en la lista")
    

    
    
def imprimir_certificado():
    print("Imprimir Certificado")
    v_nif = input("Ingrese NIF de la persona: ")
    v_nif = buscar(v_nif)
    if v_nif:
        print(f"Certificado {v_nif['v_nif']}:")
        for v_nombre in v_nombre["v_nombre"]:
            print(f'v_nombre','v_edad','v_nif','v_nacimiento','v_estado','v_pertenencia')
    else:
        print(f"{v_nif} no se encuentra en la lista")   
def imprimir_certificado():
    print("¿Desea imprimir el certificado? ")
           
        
def salir():
    print('''Ah salido correctamente del programa
\tAtt: Cristian Chicaisa
          
          ''')
#creamos el menu
while True:
    # Mostrar menu de opciones
    print("\tIdentificacion Fiscal")
    print('''         
        1. Ingresar Datos
        2. Buscar persona
        3. Imprimir certificado
        4. Salir
        
        ''')
    
    try:
        op = int(input("Ingrese una Opcion:\n ")) 
    except:
        op = 0 
    
    if op < 1 or op > 4:
        print("Ingrese una opcion valida")
    else:
        if op == 1:
            datos()  
        elif op == 2:
            buscar() 
        elif op == 3:
            imprimir_certificado()  
        else:
            salir()  
            break
        # fin if
    # fin if
# fin while
    