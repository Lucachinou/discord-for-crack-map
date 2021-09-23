from tkinter import *
import socket
import select



# creer la fenetre
window = Tk()
window.title("discord béta")
window.geometry("1280x740")
window.minsize(820, 750)
window.iconbitmap("logo.ico")
window.config(background='#5E6366')

file = open("account_settings", "w+")
file.write("Lucachinou\n")
file.write("developper mode : enabled\n")
file.write("nitro : enabled\n")
file.write("status : je suis un Lucachinou\n")
file.write("richpresence : online\n")

file.close()

# ajout du compteur
label_counter = Label(window, text="bienvenue sur discord béta", font=("Courrier", 30), bg="#5E6366")
label_counter.pack(side=BOTTOM)


# creer la frame principale
frame = Frame(window, bg='#5E6366')

# message de demande de connexion
label_title = Label(window, text="Veuillez vous connecter !", font=("Courrier", 40), bg='#5E6366')
label_title.pack()

entry1 = Entry(window, width = 20)
entry1.pack()

def button_command():
    entry1.delete(0, 200)
    return None

Button(window, text="Button", command=button_command).pack()

# creation d'image
width = 300
height = 400
image = PhotoImage(file="boutton.png").zoom(32).subsample(68)

# ajout du bouton/image
button = Button(frame, image=image, bg='#5E6366', bd=0, relief=SUNKEN)
button.pack(side=BOTTOM)

# ajout de la frame au centre
frame.pack(side=LEFT)

# Création du chat

# affichage
window.mainloop()