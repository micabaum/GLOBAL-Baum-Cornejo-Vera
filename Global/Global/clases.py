class Detector:
    adn = []
    def __init__(self, adn):
        self.adn = adn

    def detectarMutanteHorizontal(self, adn):

        for filas in adn:

            contador = 0
            contador1 = 0
            contador2 = 0
            contador3 = 0

            for base in filas:
                if base == 'A':
                    contador += 1
                    if contador >= 4:
                        return True
                elif base == 'T':
                    contador1 += 1
                    if contador1 >= 4:
                        return True
                elif base == 'C':
                    contador2 += 1
                    if contador2 >= 4:
                        return True
                elif base == 'G':
                    contador3 += 1
                    if contador3 >= 4:
                        return True
        return False


    def detectorDeMutantesVertical(self, adn):
        num_columnas = len(adn[0])
        resultado = []

        for j in range(num_columnas):
            conteo = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
            for fila in adn:
                conteo[fila[j]] += 1
            resultado.append(conteo)

        for i, columna in enumerate(resultado):
            if columna['A'] >= 4:
                return True
            elif columna['T'] >= 4:
                return True
            elif columna['C'] >= 4:
                return True
            elif columna['G'] >= 4:
                return True

        return False

    def detectorDeMutantesDiagonal(self, adn):
        n = len(adn)
        diagonal_principal = []
        diagonal_secundaria = []
        conteoPrincipal1 = 0
        conteoPrincipal2 = 0
        conteoPrincipal3 = 0
        conteoPrincipal4 = 0
        conteoSecundario1 = 0
        conteoSecundario2 = 0
        conteoSecundario3 = 0
        conteoSecundario4 = 0

        for i in range(n):
            # Diagonal principal
            diagonal_principal.append(adn[i][i])
            # Diagonal secundaria
            diagonal_secundaria.append(adn[i][n - i - 1])
        for i in diagonal_principal:
            if i == 'A':
                conteoPrincipal1 += 1
                if conteoPrincipal1 >= 4:
                    return True
            elif i == 'T':
                conteoPrincipal2 += 1
                if conteoPrincipal2 >= 4:
                    return True
            elif i == 'C':
                conteoPrincipal3 += 1
                if conteoPrincipal3 >= 4:
                    return True
            elif i == 'G':
                conteoPrincipal4 += 1
                if conteoPrincipal4 >= 4:
                    return True
        for i in diagonal_secundaria:
            if i == 'A':
                conteoSecundario1 += 1
                if conteoSecundario1 >= 4:
                    return True
            elif i == 'T':
                conteoSecundario2 += 1
                if conteoSecundario2 >= 4:
                    return True
            elif i == 'C':
                conteoSecundario3 += 1
                if conteoSecundario3 >= 4:
                    return True
            elif i == 'G':
                conteoSecundario4 += 1
                if conteoSecundario4 >= 4:
                    return True

        return False

    def detectarMutante(self,adn):
        if self.detectorDeMutantesDiagonal(adn) or self.detectorDeMutantesVertical(adn) or self.detectarMutanteHorizontal(adn):
            return True

        return False

class Mutador:
    base_nitrogenada = ""
    cantidad_repetida = 0
    adn = []

    def __init__(self, base_nitrogenada, cantidad_repedida, adn):
        self.base_nitrogenada = base_nitrogenada
        self.cantidad_repetida = cantidad_repedida
        self.adn = adn

    def crear_semilla_horizontal(self):
        miAdn = self.adn
        base = self.base_nitrogenada
        fila = list(miAdn[0])
        contador = 0
        cantidad = self.cantidad_repetida

        for i in range(len(miAdn)):
            for j in range(i):
                contador += 1
                if contador <= cantidad:
                    fila[i] = base
                else:
                    fila = ''.join(fila)
                    return fila

    def crear_semilla_vertical(self):
        miAdn = self.adn
        base = self.base_nitrogenada
        columna = [fila[1] for fila in miAdn]
        contador = 0
        cantidad = self.cantidad_repetida
        for i in range(len(miAdn)):
            for j in range(i):
                contador += 1
                if contador <= cantidad:
                    columna[i] = base
                else:
                    columna = ''.join(columna)
                    columna_transpuesta = [[x] for x in columna]
                    return columna_transpuesta

    def crear_mutante(self):
        miAdn = self.adn
        for i in range(len(miAdn)):
            for j in range(i):
                miAdn[0] = self.crear_semilla_horizontal()
        return miAdn









