from django.http import HttpResponse
from django.shortcuts import render

def verificar_palindromo(request, palabra):
    
    palabra_limpia = ''.join(palabra.split()).lower()
   
    es_palindromo = palabra_limpia == palabra_limpia[::-1]
    
    if es_palindromo:
        resultado = f'La palabra "{palabra}" es un palíndromo.'
    else:
        resultado = f'La palabra "{palabra}" NO es un palíndromo.'

    return HttpResponse(resultado)
