# Performar uma simples leitura bíblica no dictionary 'database.Data.Bible', usando ou a função '.getCompleteNAA()' ou '.getCompleteACF()'
# Lista dos casos de input:
# - (1) Abreviação
# - (2) Abreviação/Capítulo
# - (3) Abreviação/Capítulo:Versiculo-Versiculo
# - (4) Abreviação/Capítulo:Versiculo

# Perform a simple biblical read using the dictionary 'database.Data.Bible' using the function '.getCompleteNAA()' or '.getCompleteACF()'
# List of input cases:
# - (1) Abbreviation
# - (2) Abbreviation/Chapter
# - (3) Abbreviation/Chapter:Versicle-Versicle
# - (4) Abbreviation/Chapter:Versicle

from database.Data import Bible
import textwrap
import sys

bible = Bible().getCompleteNAA() if str(sys.argv[1].lower()) == 'naa' else Bible().getCompleteACF()
_input = str(sys.argv[2].lower())

def book(_input):
    """Printar todo o livro.
       Print whole book.
    """
    for book in bible:
        name, sep, abbr = book.partition("/")

        if (name.lower() == _input or abbr.lower().replace(" ", "") == _input):
            print(name.upper())

            for chapter in bible[book]:
                print('\n-- Capítulo', chapter)
                for verse in bible[book][chapter]:
                    print(verse, bible[book][chapter][verse])

def chapter(_input):
    """Printar todo o capítulo.
       Print whole chapter.
    """
    for book in bible:
        name, sep, abbr = book.partition("/")
        input_name, sep, input_chapter = _input.partition("/")

        if (name.lower() == input_name or abbr.lower().replace(" ", "") == input_name):
            for chapter in bible[book]:
                if (chapter == input_chapter):
                    print(name.upper(), chapter, '\n')
                    for verse in bible[book][chapter]:
                        print(verse, bible[book][chapter][verse])

def verses(_input):
    """Printar a referência de versículos.
       Print the versicle's reference.
    """
    for book in bible:
        name, sep, abbr = book.partition("/")
        input_name, sep, input_info = _input.partition("/")
        input_chapter, sep, input_verses = input_info.partition(":")
        beggining, sep, end = input_verses.partition("-")

        if (name.lower() == input_name or abbr.lower().replace(" ", "") == input_name):
            for chapter in bible[book]:
                if (chapter == input_chapter):
                    print("{} {}:{}-{}\n". format(name.upper(), chapter, beggining, end))
                    for verse in bible[book][chapter]:
                        if (int(verse) >= int(beggining) and int(verse) <= int(end)):
                            print(bible[book][chapter][verse])

def verse(_input):
    """Printar o versículo específico.
       Print the specific versicle.
    """
    for book in bible:
        name, sep, abbr = book.partition("/")
        input_name, sep, input_info = _input.partition("/")
        input_chapter, sep, input_verse = input_info.partition(":")

        if (name.lower() == input_name or abbr.lower().replace(" ", "") == input_name):
            for chapter in bible[book]:
                if (chapter == input_chapter):
                    for verse in bible[book][chapter]:
                        if (verse == input_verse):
                            print('"{}" ({} {}:{})'.format(bible[book][chapter][verse], abbr, chapter, verse))


if '/' in _input and ':' in _input and '-' in _input: # Caso (4)
    verses(_input)
elif '/' in _input and ':' in _input: # Caso (3)
    verse(_input)
elif '/' in _input: # Caso (2)
    chapter(_input)
else: # Caso (1)
    book(_input)
