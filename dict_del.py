'''
Created on Jul 2, 2014

@author: viejoemer

Howto delete a key from a dict in python?

¿Cómo  eliminar una llave de un diccionario en python?

'''

#Creating a dict with data
d = {
     "red":100,
     "yellow":200,
     "blue" : 300
     }
print(d)

#Delete a key
del d["red"]
print(d)