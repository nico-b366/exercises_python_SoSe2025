def cagr_berechnung(EK, AK, t):
    AK_abs = abs(AK)
    t_abs = abs(t)
    cagr = (EK/AK_abs)**(1/t_abs)-1
    return cagr

cagr = cagr_berechnung (AK = 100,
                        t = 30,
                        EK = 700)
print(120*(1+cagr)**30)