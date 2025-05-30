
import random



def coordenadas(cantidad_de_pares):
    lista = []  
    for i in range(cantidad_de_pares):
        x = random.randint(-81, 81)  
        y = random.randint(-81, 81)  
        par = [x, y]  
        lista.append(par)  
    return lista


# usando el Teorema de Pitágoras
def distancia_pitagoras(coordenada):
    x = coordenada[0]
    y = coordenada[1]
    distancia = (x**2 + y**2)**0.5
    return distancia

#  metodo divide y venceras

def coordenadaLejana(coordenadas):
    
    if len(coordenadas) == 0:
        return print("esta vacio")
    
    if len(coordenadas) == 1:
        x = coordenadas[0][0]
        y = coordenadas[0][1]
        if x > 0 and y < 0:
            return coordenadas[0]
        else:
            return None
        

   
    mitad = len(coordenadas) // 2
    lado_izquierdo = coordenadas[:mitad]
    lado_derecho = coordenadas[mitad:]

    
    mejor_izquierda = coordenadaLejana(lado_izquierdo)
    mejor_derecha = coordenadaLejana(lado_derecho)

   
    if mejor_izquierda and mejor_derecha:
        distancia_izquierda = distancia_pitagoras(mejor_izquierda)
        distancia_derecha = distancia_pitagoras(mejor_derecha)
        if distancia_izquierda > distancia_derecha:
            return mejor_izquierda
        else:
            return mejor_derecha
    elif mejor_izquierda:
        return mejor_izquierda
    elif mejor_derecha:
        return mejor_derecha
    else:
        return None


def main():
    
    
    cantidad = int(input("Ingrese la cantidad de pares de coordenadas que desea generar: "))

    
    lista_de_coordenadas = coordenadas(cantidad)

    
    print("\nCoordenadas generadas:")
    for coordenada in lista_de_coordenadas:
        print(coordenada)

    
    mejor_coordenada = coordenadaLejana(lista_de_coordenadas)

    
    if mejor_coordenada:
        distancia = distancia_pitagoras(mejor_coordenada)
        print(f"\n coordenada mas lejana del origen con X positivo e Y negativo es : {mejor_coordenada}")
        print(f"la  distancia desde el origen es: {distancia:.2f}")
    else:
        print("\nNo se encontro ninguna coordenada con X positov e Y negativo .")




main()
