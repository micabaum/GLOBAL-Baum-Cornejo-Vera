import clases
str(input ("Ingrese una caadena de adn"))
print (adn [])

miAdn = clases.Detector(adn)
miMutante = clases.Mutador('T', 4, adn)

print(miMutante.crear_mutante())

print(miAdn.detectarMutante(adn))
