def calcular_media_tres_numeros():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    num3 = float(input("Ingresa el tercer número: "))
    
    media = (num1 + num2 + num3) / 3
    return media

media_resultado = calcular_media_tres_numeros()
print("La media de los tres números es:", media_resultado)
