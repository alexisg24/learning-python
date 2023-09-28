'''Es palindromo'''


def es_palindromo(text):
    evaltext = text.lower().strip().replace(' ', '')
    evaltextlen = len(evaltext)
    reversetext = ''

    # for char in evaltext:
    #     reversetext = char + reversetext

    while evaltextlen > 0:
        reversetext += evaltext[evaltextlen-1]
        evaltextlen -= 1
    return evaltext == reversetext


print(es_palindromo('Hola mundo'))
