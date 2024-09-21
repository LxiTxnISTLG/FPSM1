meses = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, 
    "mayo": 5, "junio": 6, "julio": 7, "agosto": 8, 
    "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
}

días = {
    "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5, 
    "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10,
    "once": 11, "doce": 12, "trece": 13, "catorce": 14, "quince": 15,
    "dieciseis": 16, "diecisiete": 17, "dieciocho": 18, "diecinueve": 19,
    "veinte": 20, "veintiuno": 21, "veintidos": 22, "veintitres": 23,
    "veinticuatro": 24, "veinticinco": 25, "veintiseis": 26, "veintisiete":27,
    "veintiocho":28, "veintinueve": 29, "treinta":30, "treinta y uno": 31
}

fecha_usual = input("Ingresa la fecha en formato usual (por ejemplo, 15, Febrero 1989): ")

fecha_usual = fecha_usual.replace(",", "")

i = 0
while i < len(fecha_usual) and fecha_usual[i] != ' ':
    i += 1
dia = fecha_usual[:i]

j = i + 1
while j < len(fecha_usual) and fecha_usual[j] != ' ':
    j += 1
mes_texto = fecha_usual[i+1:j].lower()

año = fecha_usual[j+1:]

mes_numero = meses[mes_texto]

print(f"{dia} {mes_numero} {año}")
