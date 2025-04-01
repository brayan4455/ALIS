import re
from math import gcd

def parse_formula(formula):
    match = re.match(r'C(\d*)H(\d*)', formula)
    if not match:
        return None, None
    nC = int(match.group(1)) if match.group(1) else 1
    nH = int(match.group(2)) if match.group(2) else 1
    return nC, nH

def balance_combustion(formula):
    nC, nH = parse_formula(formula)
    if nC is None or nH is None:
        return "Fórmula inválida. Use formato como 'C2H6'"
    
    # Definir coeficientes iniciales
    a = 1  # Un mol del hidrocarburo
    c = nC  # Coeficiente del CO2
    d = nH // 2  # Coeficiente del H2O
    b = (2 * c + d) // 2  # Coeficiente del O2
    
    # Asegurar que todos los coeficientes sean enteros
    factor = gcd(gcd(a, b), gcd(c, d))
    a, b, c, d = (x // factor for x in (a, b, c, d))
    
    return f"{a} {formula} + {b} O₂ → {c} CO₂ + {d} H₂O"

def main():
    print("Balanceador de ecuaciones de combustión de hidrocarburos")
    while True:
        hidrocarburo = input("Ingrese la fórmula del hidrocarburo (ej. C2H6, 'salir' para terminar): ")
        if hidrocarburo.lower() == 'salir':
            break
        print(balance_combustion(hidrocarburo))

if __name__ == "__main__":
    main()
