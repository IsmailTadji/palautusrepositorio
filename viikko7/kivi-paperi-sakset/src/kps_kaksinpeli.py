from kps import KiviPaperiSakset

class KPSKaksinpeli(KiviPaperiSakset):
    
    def _toisen_siirto(self, ensimmäisen_siirto):
        return input("Toisen pelaajan siirto: ")