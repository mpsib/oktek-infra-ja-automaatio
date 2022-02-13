# Kirjoita postinumerot-moduulin testit tähän tiedostoon
from postinumerot import haeAineisto, haePostinumerot

def test_all_uppercase():
    assert 1 == len(haePostinumerot('TAMMELA', haeAineisto()))

def test_all_lowercase():
    assert 1 == len(haePostinumerot('tammela', haeAineisto()))

def test_tammela_has_one_postalcode():
    assert 1 == len(haePostinumerot('Tammela', haeAineisto()))

def test_forssa_has_five_postalcodes():
    assert 5 == len(haePostinumerot('Forssa', haeAineisto()))

def test_helsinki_has_many_postalcodes():
    assert 1 < len(haePostinumerot('Helsinki', haeAineisto()))

def test_austin_has_no_postalcodes():
    assert 0 == len(haePostinumerot('Austin', haeAineisto()))

def test_smartpost_and_smart_post_have_same_length():
    assert len(haePostinumerot('smartpost', haeAineisto())) == len(haePostinumerot('smart post', haeAineisto()))

def test_smartpost_and_smart_post_have_same_content():
    assert haePostinumerot('smartpost', haeAineisto()) == haePostinumerot('smart post', haeAineisto())
