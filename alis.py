from sympy import symbols, Eq, solve
import re

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
    
    # Definir coeficientes
    a, b, c, d = symbols('a b c d', integer=True, positive=True)
    
    # Ecuaciones de balance
    eq1 = Eq(nC * a, c)  # Carbono
    eq2 = Eq(nH * a, 2 * d)  # Hidrógeno
    eq3 = Eq(2 * b, 2 * c + d)  # Oxígeno
    
    # Resolver ecuaciones con un valor inicial para 'a'
    solution = solve((eq1, eq2, eq3), (a, b, c, d), dict=True)
    
    if solution:
        sol = solution[0]
        coef_a, coef_b, coef_c, coef_d = sol[a], sol[b], sol[c], sol[d]
        equation = f"{coef_a} {formula} + {coef_b} O₂ → {coef_c} CO₂ + {coef_d} H₂O"
        return equation
    else:
        return "No se pudo balancear la ecuación."

def main():
    print("Balanceador de ecuaciones de combustión de hidrocarburos")
    while True:
        hidrocarburo = input("Ingrese la fórmula del hidrocarburo (ej. C2H6, 'salir' para terminar): ")
        if hidrocarburo.lower() == 'salir':
            break
        print(balance_combustion(hidrocarburo))

if __name__ == "__main__":
    main()
