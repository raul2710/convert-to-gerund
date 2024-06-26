def isVowel(letter):
    vowels = ["a", "e", "i", "o", "u"]
    return letter in vowels

def isConsoant(letter):
    return not isVowel(letter)

def consoant_vowel_consoant(word):
    return isConsoant(word[-3]) and isVowel(word[-2]) and isConsoant(word[-1])

def consoant_vowel(word):
    return isConsoant(word[-2]) and isVowel(word[-1])

# Return if the CV case is true
def end_with_ie(word):
    """Return if the CV case is true"""
    return word[-2] == "i" and word[-1] == "e"

def end_with_e(word):
    """Return if the CV case is true"""
    return word[-1] == "e"

# Mas fique atento, pois se o final do verbo for -W, -X ou -Y, seguimos a regra original.
def end_with_w_x_y(word):
    aux = ['w', 'x', 'y']
    return word[-1] in aux

# Mas fique atento, pois se o final do verbo for -EE, -YE ou -OE, seguimos a regra original.
def end_with_ee_ye_oe_er_en_st(word):
    aux = ["ee", "ye", "oe", "er", "en", "st"]
    return word[-2:] in aux

def transformVerbToIngForm(verb):

    verbLowCase = verb.lower()
    lenVerb = len(verb)

    excessionWords = {
        "refer" : "referring",
        "visit" : "visiting",
    }

    if verbLowCase in excessionWords:
        return excessionWords.get(verbLowCase) 

    # Terminated with I and E words
    if end_with_ie(verbLowCase):
        return verbLowCase[:-2] + "ying"

    if lenVerb <= 3:
        # Consoant + Vowel (VC) case
        if consoant_vowel(verbLowCase):
            return verbLowCase + "ing"
    
    # Vowel + Consoant + Consoant (VCC) case OR Vowel + Consoant (VC) case
    if end_with_ee_ye_oe_er_en_st(verbLowCase) or end_with_w_x_y(verbLowCase):
        return verbLowCase + "ing"
    
    # Consoant + Vowel + Consoant (CVC) case
    if consoant_vowel_consoant(verbLowCase):
        return verbLowCase + verbLowCase[-1] + "ing"
    
    # Terminated in "e"
    if end_with_e(verbLowCase):
        return verbLowCase[:-1] + "ing"

    return verbLowCase + "ing"

"""ConvertVerbToGerund.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OQHy8gPfCnzkPcMm0ew9D6RtdRsCkDYF

Escreva um programa em Python que transforme os verbos em sua forma de gerúndio em inglês, adicionando o sufixo '-ing' de maneira adequada aos verbos fornecidos pelo usuário.
Em inglês, para adicionar o sufixo "-ing" aos verbos, geralmente seguem-se estas regras:

1. Verbos Monossilábicos Terminados em Consoante + Vogal + Consoante (CVC):
Nesse caso, a última consoante é duplicada antes de adicionar "-ing". Exemplos:
- a. "Run" (correr) se torna "running" (correndo).
- b. "Sit" (sentar) se torna "sitting" (sentado).

2. Verbos Monossilábicos Terminados em Vogal + Consoante (VC): Nesse caso, a última consoante não é duplicada antes de adicionar "-ing". Exemplos:
- a. "Go" (ir) se torna "going" (indo).
- b. "Read" (ler) se torna "reading" (lendo).

3. Verbos Polissilábicos: Nesses casos, se a sílaba tônica (a sílaba mais forte) estiver na última sílaba do verbo e o verbo terminar em consoante + vogal + consoante, a
última consoante é duplicada antes de adicionar "-ing". Exemplos:
- a. "Begin" (começar) se torna "beginning" (começando).
- b. "Forget" (esquecer) se torna "forgetting" (esquecendo).

4. Verbos Terminados em "e": Se o verbo terminar em "e", ela é geralmente removida antes de adicionar "-ing". Exemplos:
- a. "Write" (escrever) se torna "writing" (escrevendo).
- b. "Dance" (dançar) se torna "dancing" (dançando).

5. Verbos Irregulares: Alguns verbos têm formas irregulares no gerúndio. Eles não seguem as regras padrão de adicionar "-ing". Alguns exemplos comuns incluem:
- a. "Be" (ser/estar) se torna "being" (sendo).
- b. "Have" (ter) se torna "having" (tendo).
"""