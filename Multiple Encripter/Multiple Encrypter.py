import random
from tkinter import *
from tkinter import ttk
import base64
import librariesIdioms as idiom
import math
from PIL import ImageTk, Image
import os
import sys

def base64_code(in_phrase,in_solution):
    try:
        if encrypting == True:
            in_solution.delete(0, END)
            phrase = in_phrase.get()
            b_phrase = phrase.encode()
            menBase64 = base64.b64encode(b_phrase)
            in_solution.insert(0, menBase64)
        elif decrypting == True:
            in_solution.delete(0, END)
            phrase = in_phrase.get()
            menBase64 = base64.b64decode(phrase)
            in_solution.insert(0, menBase64)
        else:
            in_solution.insert(0, "Choose if you want to Encrypt or Decrypt")
    except:
        in_solution.insert(0, "You haven't select DECRYPT or ENCRYPT or there is an error in the message or in the program, report to creator please - https://github.com/Bl41d")

def base32_code(in_phrase,in_solution):
    try:
        if encrypting == True:
            in_solution.delete(0, END)
            phrase = in_phrase.get()
            b_phrase = phrase.encode()
            menBase32 = base64.b32encode(b_phrase)
            in_solution.insert(0, menBase32)
        elif decrypting == True:
            in_solution.delete(0, END)
            phrase = in_phrase.get()
            menBase32 = base64.b32decode(phrase)
            in_solution.insert(0, menBase32)
        else:
            in_solution.insert(0, "Choose if you want to Encrypt or Decrypt")
    except:
        in_solution.insert(0, "You haven't select DECRYPT or ENCRYPT or there is an error in the message or in the program, report to creator please - https://github.com/Bl41d")

def base16_code(in_phrase,in_solution):
    try:
        if encrypting == True:
            in_solution.delete(0, END)
            phrase = in_phrase.get()
            b_phrase = phrase.encode()
            menBase16 = base64.b16encode(b_phrase)
            in_solution.insert(0, menBase16)
        elif decrypting == True:
            in_solution.delete(0, END)
            phrase = in_phrase.get()
            menBase16 = base64.b16decode(phrase)
            in_solution.insert(0, menBase16)
        else:
            in_solution.insert(0, "Choose if you want to Encrypt or Decrypt")
    except:
        in_solution.insert(0, "You haven't select DECRYPT or ENCRYPT or there is an error in the message or in the program, report to creator please - https://github.com/Bl41d")

def binary_code(in_phrase,in_solution):
    try:
        if encrypting == True:
            in_solution.delete(0, END)
            menBinary = ""
            phrase = in_phrase.get()
            for n in phrase:
                menBinary += format(ord(n), 'b')
                menBinary += " "
            in_solution.insert(0, menBinary)
        elif decrypting == True:
            in_solution.delete(0, END)
            phrase = in_phrase.get()
            menBinary = ""
            for binario in phrase.split(" "):
                for i in range(0, len(binario), 7):
                    temp_data = int(binario[i:i + 7])
                    decimal_data = BinaryToDecimal(temp_data)
                    menBinary = menBinary + chr(decimal_data)
            in_solution.insert(0, menBinary)
        else:
            in_solution.insert(0, "Choose if you want to Encrypt or Decrypt")
    except:
        in_solution.insert(0, "You haven't select DECRYPT or ENCRYPT or there is an error in the message or in the program, report to creator please - https://github.com/Bl41d")

def BinaryToDecimal(binary):
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return (decimal)

def blaid_code(in_phrase,in_solution):
    try:
        menBlaid = ""
        if encrypting == True:
            in_solution.delete(0, END)
            phrase = in_phrase.get()
            for n in phrase.lower():
                if n in idiom.letter:
                    menBlaid += idiom.blaid[idiom.letter.index(n)]
                    menBlaid += " "
            in_solution.insert(0, menBlaid)
        elif decrypting == True:
            in_solution.delete(0, END)
            phrase = in_phrase.get()
            for i in phrase.split(" "):
                if i in idiom.blaid:
                    menBlaid += idiom.letter[idiom.blaid.index(i)]
                else:
                    menBlaid += ""
            in_solution.insert(0, menBlaid)
        else:
            in_solution.insert(0, "Choose if you want to Encrypt or Decrypt")
    except:
        in_solution.insert(0, "You haven't select DECRYPT or ENCRYPT or there is an error in the message or in the program, report to creator please - https://github.com/Bl41d")

def octal_code(in_phrase,in_solution):
    try:
        menOctal = ""
        if encrypting == True:
            in_solution.delete(0, END)
            phrase = in_phrase.get()
            for n in phrase.lower():
                if n in idiom.letter:
                    menOctal += idiom.octal[idiom.letter.index(n)]
                    menOctal += " "
            in_solution.insert(0, menOctal)
        elif decrypting == True:
            in_solution.delete(0, END)
            phrase = in_phrase.get()
            for i in phrase.split(" "):
                if i in idiom.octal:
                    menOctal += idiom.letter[idiom.octal.index(i)]
                else:
                    menOctal += ""
            in_solution.insert(0, menOctal)
        else:
            in_solution.insert(0, "Choose if you want to Encrypt or Decrypt")
    except:
        in_solution.insert(0, "You haven't select DECRYPT or ENCRYPT or there is an error in the message or in the program, report to creator please - https://github.com/Bl41d")

def hexa_code(in_phrase,in_solution):
    try:
        menHexa = ""
        if encrypting == True:
            in_solution.delete(0, END)
            phrase = in_phrase.get()
            for n in phrase.lower():
                if n in idiom.letter:
                    menHexa += idiom.hexa[idiom.letter.index(n)]
                    menHexa += " "
            in_solution.insert(0, menHexa)
        elif decrypting == True:
            in_solution.delete(0, END)
            phrase = in_phrase.get()
            for i in phrase.split(" "):
                if i in idiom.hexa:
                    menHexa += idiom.letter[idiom.hexa.index(i)]
                else:
                    menHexa += ""
            in_solution.insert(0, menHexa)
        else:
            in_solution.insert(0, "Choose if you want to Encrypt or Decrypt")
    except:
        in_solution.insert(0, "You haven't select DECRYPT or ENCRYPT or there is an error in the message or in the program, report to creator please - https://github.com/Bl41d")

def caesar_code(in_phrase,in_solution,in_layers):
    try:
        letters = "abcdefghijklmnñopqrstuvwxyz"
        numbers = "0123456789"
        if encrypting == True:
            menCaesar = ""
            layers = int(in_layers.get())
            in_solution.delete(0, END)
            phrase = in_phrase.get().lower()

            layersLet = layers
            layersNum = layers

            if layersLet > 27:
                mates = math.ceil(layersLet / 27)
                for n in range(mates - 1):
                    layersLet -= 27

            if layersNum > 10:
                mates = math.ceil(layersNum / 11)
                for n in range(mates - 1):
                    layersNum -= 10

            for n in phrase:
                if n in letters:
                    position = letters.find(n) + layersLet
                    if position > 26:
                        menCaesar += letters[position - 27]
                    else:
                        menCaesar += letters[position]
                elif n == " ":
                    menCaesar += " "
                elif n in numbers:
                    position = numbers.find(n) + layersNum
                    if position > 9:
                        menCaesar += numbers[position - 10]
                    else:
                        menCaesar += numbers[position]
            in_solution.insert(0, menCaesar)
        elif decrypting == True:
            menCaesar = ""
            layers = int(in_layers.get())
            in_solution.delete(0, END)
            phrase = in_phrase.get().lower()

            layersLet = layers
            layersNum = layers

            if layersLet > 27:
                mates = math.ceil(layersLet / 27)
                for n in range(mates - 1):
                    layersLet -= 27

            if layersNum > 10:
                mates = math.ceil(layersNum / 11)
                for n in range(mates - 1):
                    layersNum -= 10

            for n in phrase:
                if n in letters:
                    position = letters.find(n) - layersLet
                    if position >= 26:
                        menCaesar += letters[position - 26]
                    else:
                        menCaesar += letters[position]
                elif n == " ":
                    menCaesar += " "
                elif n in numbers:
                    position = numbers.find(n) - layersNum
                    if position >= 9:
                        menCaesar += numbers[position - 9]
                    else:
                        menCaesar += numbers[position]
            in_solution.insert(0, menCaesar)

    except:
        in_solution.insert(0, "You haven't select DECRYPT or ENCRYPT or there is an error in the message or in the program, report to creator please - https://github.com/Bl41d")

def encrypt_act(button_choose, button_other):
    global decrypting
    global encrypting

    button_choose.config(bg="Red")
    button_other.config(bg="White")

    if button_choose.cget('text') == "Encrypt":
        encrypting = True
        decrypting = False

    elif button_choose.cget('text') == "Decrypt":
        encrypting = False
        decrypting = True

def clear_function(in_phrase):
    in_phrase.delete(0, END)

def copy_function(in_solution, root):
    root.clipboard_clear()
    root.clipboard_append(in_solution.get())

def get_path(filename):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    else:
        return filename

def interfaz():
    root = Tk()
    root.geometry("850x675")
    root.title("Multiple Encrypter")
    root.iconbitmap(get_path("logo.ico"))
    root.config(bg="Black")
    root.resizable(width=False, height=False)

    in_phrase = ttk.Entry(font=35)
    in_phrase.place(x=100, y=130, width=650, height=30)
    in_phrase.insert(0, "")

    title = Label(root, text="MULTIPLE ENCRYPTER")
    title.config(bg="black", fg="red", font = ('Arial', 20, 'bold'))
    title.place(x=0, y=10, width=850, height=50)

    about = Label(root, text="== BLAID ==")
    about.config(bg="black", fg="red", font=('Arial', 12, 'bold'))
    about.place(x=0, y=65, width=850, height=20)

    label_phrase = Label(root, text="Phrase: ")
    label_phrase.config(bg="black", fg="red", font = ('Arial', 15, 'bold'))
    label_phrase.place(x=100, y=90, width=85, height=40)

    label_choose = Label(root, text="Enrypt/Decrypt: ")
    label_choose.config(bg="black", fg="red", font=('Arial', 15, 'bold'))
    label_choose.place(x=100, y=190, width=160, height=40)

    label_language = Label(root, text="Language: ")
    label_language.config(bg="black", fg="red", font=('Arial', 15, 'bold'))
    label_language.place(x=100, y=320, width=110, height=40)

    encrypt = Button(root, text="Encrypt", font=('Arial', 12, 'bold'), command=lambda : encrypt_act(encrypt, decrypt))
    encrypt.place(x=100, y=230, width=120, height=60)

    decrypt = Button(root, text="Decrypt", font=('Arial', 12, 'bold'), command=lambda : encrypt_act(decrypt, encrypt))
    decrypt.place(x=230, y=230, width=120, height=60)

    boton1 = Button(root, text="Base64", font = ('Arial', 12, 'bold'), command=lambda : base64_code(in_phrase,in_solution))
    boton1.place(x=100, y=360, width=120, height=60)

    boton2 = Button(root, text="Base32", font=('Arial', 12,  'bold'), command=lambda : base32_code(in_phrase,in_solution))
    boton2.place(x=230, y=360, width=120, height=60)

    boton3 = Button(root, text="Base16", font=('Arial', 12, 'bold'), command=lambda : base16_code(in_phrase,in_solution))
    boton3.place(x=360, y=360, width=120, height=60)

    boton4 = Button(root, text="Blaid", font=('Arial', 12, 'bold'), command=lambda : blaid_code(in_phrase,in_solution))
    boton4.place(x=490, y=360, width=120, height=60)

    boton5 = Button(root, text="Binary", font=('Arial', 12, 'bold'), command=lambda : binary_code(in_phrase,in_solution))
    boton5.place(x=620, y=360, width=120, height=60)

    boton6 = Button(root, text="Octal", font=('Arial', 12, 'bold'), command=lambda : octal_code(in_phrase,in_solution))
    boton6.place(x=100, y=430, width=120, height=60)

    boton7 = Button(root, text="Hexadecimal", font=('Arial', 12, 'bold'), command=lambda : hexa_code(in_phrase,in_solution))
    boton7.place(x=230, y=430, width=120, height=60)

    boton8 = Button(root, text="Caesar", font=('Arial', 12, 'bold'), command=lambda : caesar_code(in_phrase,in_solution,in_layers))
    boton8.place(x=360, y=430, width=120, height=60)

    clear = Button(root, text="Clear", font=('Arial', 12, 'bold'), command=lambda: clear_function(in_phrase))
    clear.place(x=770, y=130, width=60, height=30)

    clipboard = Button(root, text="Copy", font=('Arial', 12, 'bold'), command=lambda: copy_function(in_solution, in_layers))
    clipboard.place(x=770, y=570, width=60, height=30)

    in_layers = ttk.Entry(font=('Arial', 20, 'bold'))
    in_layers.place(x=490, y=430, width=250, height=60)
    in_layers.insert(0, "*Layers*")

    label_message = Label(root, text="Message: ")
    label_message.config(bg="black", fg="red", font=('Arial', 15, 'bold'))
    label_message.place(x=100, y=530, width=95, height=40)

    in_solution = ttk.Entry(font=35)
    in_solution.place(x=100, y=570, width=650, height=30)
    in_solution.insert(0, "")

    img = ImageTk.PhotoImage(Image.open(get_path("logo.png")))
    image = Label(image=img, bg="black")
    image.place(x=620, y=190)

    root.mainloop()

interfaz()