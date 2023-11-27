import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called()

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsu_tarkistetaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.asssert_called_with("pekka",42,"12345","33333-44455",5)

    def test_koriin_lisataan_kaksi_tuotetta_jota_on_varastossa(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.asssert_called_with("pekka",42,"12345","33333-44455",8)

    def test_koriin_lisataan_kaksi_samaa_tuotetta_jota_on_varastossa(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.asssert_called_with("pekka",42,"12345","33333-44455",10)
    
    def test_koriin_lisataan_kaksi_tuotetta_joista_yhta_on_varastossa(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.asssert_called_with("pekka",42,"12345","33333-44455",5)

    def test_aloita_asiointi_nollaa(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.asssert_called_with("pekka",42,"12345","33333-44455",10)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.asssert_called_with("pekka",42,"12345","33333-44455",8)


    def test_uusi_viitenumero_jokaiselle_ostokselle(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.asssert_called_with("pekka",42,"12345","33333-44455",10)

        self.viitegeneraattori_mock.uusi.return_value = 41
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekkaa", "12345")

        self.pankki_mock.tilisiirto.asssert_called_with("pekkaa",42,"12345","33333-44455",8)        

    def test_poista_korista(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.asssert_called_with("pekka",42,"12345","33333-44455",5)


def varasto_saldo(tuote_id):
    if tuote_id == 1:
        return 10
    if tuote_id == 2:
        return 5
    if tuote_id == 3:
        return 0

# tehdään toteutus hae_tuote-metodille
def varasto_hae_tuote(tuote_id):
    if tuote_id == 1:
        return Tuote(1, "maito", 5)
    if tuote_id == 2:
        return Tuote(2, "vesi", 3)
    if tuote_id == 3:
        return Tuote(3, "mehu", 4)
