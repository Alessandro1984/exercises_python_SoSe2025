"""
Erklärung wie die Funktion funkioniert
"""

def cagr_berechung(AK, EK, t):
    AK_abs = abs(AK)
    t_abs = abs(t)
    cagr = (EK/AK_abs)**(1/t_abs)-1
    return cagr

cagr = cagr_berechung(AK = 100,
                      EK = 700, 
                      t = 30)

print(120 * (1 + cagr)**30)


