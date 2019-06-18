from morse import *
import time
from docx import Document

mensaje = input("Dime algo: ")

telegrama = toMorse(mensaje)
print(telegrama)
original = toPlain(telegrama)
print(original)

print(time.strftime("%d/%m/%Y", time.gmtime()))