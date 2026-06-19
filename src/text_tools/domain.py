def word_count(text:str)->int:
    splitted_text = text.split()
    contatore = len(splitted_text)
    return contatore

def char_count(text:str)->int:
    caratteri = len(text.replace(" ", ""))
    return caratteri

def reverse(text:str)->str:
    invertita = text[::-1]
    return invertita
