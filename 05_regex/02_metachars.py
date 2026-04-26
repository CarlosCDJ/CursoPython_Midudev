###
# 02 - Meta caracteres
# Los metacaracteres son simbolos especiales con significados especificos en las expresiones regulares
###

# CDJ ¿Por qué ponemos la r delante de las cadenas de texto en los patrones de regex?
# La r delante de una cadena de texto indica que es una cadena de tipo "pattern raw" o "cadena cruda". 
# Esto significa que los caracteres de escape dentro de la cadena se interpretan literalmente, en lugar de ser tratados como caracteres especiales. Por ejemplo, en una cadena normal, el carácter de escape \n se interpreta como un salto de línea, pero en una cadena raw, se interpreta como los caracteres \ y n. Esto es especialmente útil en las expresiones regulares, donde a menudo se utilizan caracteres de escape para definir patrones específicos. Al usar una cadena raw, puedes escribir tus patrones de regex sin preocuparte por escapar los caracteres especiales, 
# lo que hace que el código sea más legible y fácil de escribir. 
# Cuando hablamos de caracteres de escape nos referimos a caracteres como \, que se utilizan para 
# indicar que el siguiente carácter debe ser tratado de manera especial. 
# Por ejemplo, en una cadena normal, si quieres incluir una barra invertida (\) en tu patrón de regex, 
# tendrías que escribirla como \\, lo que puede resultar confuso. 
# Sin embargo, al usar una cadena raw (con la r delante), puedes escribir la barra invertida directamente 
# como \, sin necesidad de escapar, lo que hace que el patrón sea más claro y fácil de entender.
# La contrabarra invertida (\) es un carácter de escape en las expresiones regulares, lo que significa que se utiliza 
#   para indicar que el siguiente carácter debe ser tratado de manera especial.
# El + significa que el carácter o grupo anterior debe aparecer una o más veces.
# El * significa que el carácter o grupo anterior debe aparecer cero o más veces.
# El ? significa que el carácter o grupo anterior es opcional, es decir, puede aparecer cero o una vez.

import re

# 1. El punto (.)
# Coincidir con cualquier caracter excepto una nueva linea

text = "Hola mundo, H0la de nuevo, H$la otra vez"
pattern = "H.la" # Hola, H0la, H$la

found = re.findall(pattern, text)

if (found):
  print(found)
else:
  print("No se ha encontrado el patrón")


text = "casa caasa cosa cisa cesa causa"
pattern = "c.sa"

matches = re.findall(pattern, text)
print(matches)

# --------------------

text = "Hola mundo, H0la de nuevo, H$la otra vez"
pattern = r"H.la" # Hola, H0la, H$la

found = re.findall(pattern, text)

if (found):
  print(found)
else:
  print("No se ha encontrado el patrón")


# Cómo usar la barra invertida para anular el significado especial de un símbolo
text = "Mi casa es blanca. Y el coche es negro."
pattern = r"\."

matches = re.findall(pattern, text)

print(matches)

# \d: coincide con cualquier dígito (0-9)
# CDJ: las llaves sirven para especificar el número de veces que debe repetirse un patrón
text = "El número de teléfono es 123456789"
found = re.findall(r'\d', text)
print(found)

text = "El número de teléfono es 123456789"
found = re.findall(r'\d\d\d', text)
print(found)

text = "El número de teléfono es 123456789"
found = re.findall(r'\d{9}', text)
print(found)

# Ejercicio: Detectar si hay un número de España en el texto gracias al prefijo +34

text = "Mi número de teléfono es +34 688999999 apúntalo vale?"
pattern = r"\+34 \d{9}"
found = re.search(pattern, text)
if found: print(f"Encontré el número de teléfono {found.group()}")
else: print("No se encontró el número de teléfono")

# \w: Coincide con cualquier caracter alfanumerico (a-z, A-Z, 0-9, _)

text = "el_rubius_69"
pattern = r"\w"
found = re.findall(pattern, text)
print(found)

# \s: Coincide con cualqueir espacio en blanco (espacio, tabulación, salto de línea)
text = "Hola mundo\n¿Cómo estás?\t"
pattern = r"\s"
matches = re.findall(pattern, text)
print(matches)

# ^: Coincide con el principio de una cadena
username = "423_name%22" 
pattern = r"^\w" # validar nombre de usuario

valid = re.search(pattern, username)

if valid: print("El nombre de usuario es válido")
else: print("El nombre de usuario no es válido")

phone = "+34 688999999"
pattern = r"^\+\d{1,3} "

valid = re.search(pattern, phone)

if valid: print("El número de teléfono es válido")
else: print("El número de teléfono no es válido")

# $: Coincide con el final de una cadena
text = "Hola mundo."
pattern = r"mundo$"

valid = re.search(pattern, text)

if valid: print("La cadena es válida")
else: print("La cadena no es válida")

# EJERCICIO
# Valida que un correo sea de gmail
text = "miduga@hotmail.com"
pattern = r"@gmail.com$"
valid = re.search(pattern, text)

if valid: print("El correo es gmail válido")
else: print("El correo no es válido")

# EJERCICIO:
# Tenemos una lista de archivos, necesitamos saber los nombres de los ficheros con extension .txt
files = "file1.txt file2.pdf midu-of.webp secret.txt"
pattern = r"\b[\w-]+\.txt\b"
found = re.findall(pattern, files)
print(found)

# \b: Coincide con el principio o final de una palabra
text = "casa casada cosa cosas casado casa"
pattern = r"\bc.sa\b"

found = re.findall(pattern, text)
print(found)

# |: Coincidr con una opción u otra
fruits = "platano, piña, manzana, aguacate, palta, pera, aguacate, aguacate"
pattern = r"palta|aguacate|p..a|\b\w{7}\b"

matches = re.findall(pattern, fruits)
print(matches)