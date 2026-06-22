from text_tools.domain import word_count, char_count, reverse

def test_word_count_basic():
    risultato = word_count("ciao mondo")
    assert risultato == 2


def test_char_count_basic():
    risultato = char_count("ciao mondo")
    assert risultato == 8 #9

def test_reverse_basic():
    risultato = reverse("ciao")
    assert risultato == ("oai") #oaic