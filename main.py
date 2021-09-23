from tkinter import *



# creer la fenetre
window = Tk()
window.title("discord béta")
window.geometry("720x480")
window.iconbitmap("")
window.config(background='#5E6366')

# ajout du compteur
label_counter = Label(window, text="bienvenue sur discord béta", font=("Courrier", 30), bg="#5E6366")
label_counter.pack(side=BOTTOM)

# creer la frame principale
frame = Frame(window, bg='#5E6366')

# creation d'image
width = 300
height = 800
image = PhotoImage(file="logo_crack_game.png").zoom(32).subsample(64)

# ajout du bouton/image
button = Button(frame, image=image, bg='#5E6366', bd=0, relief=SUNKEN)
button.pack()

# ajout de la frame au centre
frame.pack(expand=YES)

# affichage
window.mainloop()