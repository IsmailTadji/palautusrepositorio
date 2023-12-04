class IntJoukko:
    KAPASITEETTI = 5
    OLETUSKASVATUS = 5

    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = kapasiteetti or self.KAPASITEETTI
        self.kasvatuskoko = kasvatuskoko or self.OLETUSKASVATUS
        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def _luo_lista(self, koko):
        return [0] * koko

    def kuuluu(self, n):
        return n in self.ljono[:self.alkioiden_lkm]

    def lisaa(self, n):
        if not self.kuuluu(n):
            if self.alkioiden_lkm == len(self.ljono):
                self._kasvata_taulukkoa()
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1
            return True
        return False

    def poista(self, n):
        if n in self.ljono[:self.alkioiden_lkm]:
            self.ljono.remove(n)
            self.alkioiden_lkm -= 1
            return True
        return False

    def _kasvata_taulukkoa(self):
        self.ljono += self._luo_lista(self.kasvatuskoko)

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def _yhdiste_tai_leikkaus(a, b, union=True):
        result = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in a_taulu:
            result.lisaa(i)

        for i in b_taulu:
            if (union and not result.kuuluu(i)) or (not union and result.kuuluu(i)):
                result.lisaa(i)

        return result

    @staticmethod
    def yhdiste(a, b):
        return IntJoukko._yhdiste_tai_leikkaus(a, b, union=True)

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j] and not y.kuuluu(b_taulu[j]):
                    y.lisaa(b_taulu[j])

        return y


    @staticmethod
    def erotus(a, b):
        result = IntJoukko()
        a_taulu = a.to_int_list()

        for i in a_taulu:
            if not b.kuuluu(i):
                result.lisaa(i)

        return result

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            elements = ", ".join(map(str, self.ljono[:self.alkioiden_lkm]))
            return "{" + elements + "}"