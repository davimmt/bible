# Escrever em um arquivo, que leva por título a palavra-chave escolhida como argumento, os versículos relacionados à palavra-chave especificada.
# Write in a file, which takes by title the keyword chosen as an argument, the verses related to the specified keyword.

from database.Spliters import Division
from database.Data import Bible
import string
import sys
import os

def inputMain():
    """Prompt CLI user-frindly para o usuário escolher o range da Bíblia (entre nome de capítulos)
    em que ele quer filtrar o processamento.
       Prompt CLI user-friendly for the user to choose the range of the Bible (between chapter names) 
    in which he wants to filter the processing.
    """
    try:
        inputRange = int(input("\n[1] Toda Bíblia\n[2] Velho Testamento\n[3] Novo Testamento\n[4] Personalizado\n\nVocê quer gerar (padrão = 1): "))
        if inputRange == 1: returnRange = None
        if inputRange == 2: returnRange = Division().OldTestament()
        if inputRange == 3: returnRange = Division().NewTestament()
        if inputRange == 4:
            book_list = []
            for i in range(0, 2):
                book_list.append(input('(Livro/Abreviação): '))
            returnRange = book_list
    except:
        returnRange = None

    return main(returnRange)

def main(forRange):
    """Escreve no arquivo entitulada após a palavra-chave os versículos.
       Write in the file titled after the keyword the verses.
    """
    version = str(sys.argv[1].lower())

    bible = Bible().getCompleteNAA() if version == 'naa' else Bible().getCompleteACF()

    if (forRange):
        bible = Division().between_two_values(bible, forRange[0], forRange[1])

    keyword = str(sys.argv[2].lower())
    keywords = [x.strip() for x in keyword.split(',')]
    fileName = version + "-" + keyword.strip().replace(' ', '_') + ".txt"

    with open(fileName, 'a+', encoding='utf-8') as file:
        filesize = os.path.getsize(fileName)
        if filesize == 0:
            file.write(keyword.upper() + '\n\n')

    for book in bible:
        name, sep, abbr = book.partition("/")

        for chapter in bible[book]:
            for verse in bible[book][chapter]:
                thisVerse = bible[book][chapter][verse]
                refVerse = thisVerse.translate(str.maketrans('', '', string.punctuation)).lower()
                counter = 0

                for word in keywords:
                    if refVerse.startswith(word + ' ') or refVerse.endswith(' ' + word) or (' ' + word + ' ') in refVerse:
                        counter += 1
                
                if counter == len(keywords):
                    with open(fileName, 'a+', encoding='utf-8') as file:        
                        file.write('\n"' + thisVerse + '" (' + abbr + ' ' + chapter + ':' + verse + ')\n')

inputMain()