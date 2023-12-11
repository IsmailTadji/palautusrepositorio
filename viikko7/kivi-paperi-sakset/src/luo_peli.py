from kps_kaksinpeli import KPSKaksinpeli
from kps_tekoaly import KPSTekoaly
from kps_viksu_tekoaly import KPSViksuTekoaly


def luo_peli(input):
    if input == "a":
        kp = KPSKaksinpeli()
        kp.pelaa()
    elif input == "b":
        tk = KPSTekoaly()
        tk.pelaa()
    elif input == "c":
        tk_v = KPSViksuTekoaly()
        tk_v.pelaa()
    
    return None