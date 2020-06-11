#!/usr/bin/python3
#coding: utf-8
from tkinter import *
import time
class Interface(Frame): 
    # On créé un UI Interface qui hérite de Frame
    # 
    
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, **kwargs) # Le widget Interface est un cadre (Frame) qui va conten,ir tous les autres widgets
        self.master.title("Exemple d'UI")
        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)
        self.rowconfigure(5, pad=3)
        self.rowconfigure(6, pad=3)
        self.rowconfigure(7, pad=3)

        self.nb_clic = 0
        self.default_color = self.cget("bg")

        # Message
        self.ask_name = Label(self, text="Entrer votre nom ici : ")
        self.ask_name.grid(column=0,row=0)

        # Réponse
        self.var_name = StringVar()
        self.var_name.trace("w",self.change_name)
        self.entry_name = Entry(self, textvariable=self.var_name)
        self.entry_name.grid(column=1,row=0)

        # Texte compteur de clics
        self.message = Label(self, text="Vous n'avez pas cliqué sur le bouton.")
        self.message.grid(row=1,columnspan=2)

        # Bouton quitter
        self.button_quit = Button(self, text="Quitter", command=self.quit)
        self.button_quit.grid(column=0,row=2)
        
        # Bouton cliquer
        self.button_click = Button(self, text="Cliquez ici", fg="red", command=self.click)
        self.button_click.grid(column=1,row=2)

        self.pack() # Tout afficher

        # Bouton à cocher
        self.show_colors = IntVar()
        self.show_colors.trace("w",self.color_display)
        self.check_colors = Checkbutton(self, text="Changer la couleur de la fenêtre ?", variable=self.show_colors)
        self.check_colors.grid(column=0,row=3,columnspan=2)

    def click(self):
        # Déclenché au moment d'un clic
        self.nb_clic += 1
        self.change_name()

    def change_name(self,*args):
        if self.var_name.get():
            self.message["text"] = "{} a cliqué {} fois.".format(self.var_name.get(),self.nb_clic)
        else:
            self.message["text"] = "Vous avez cliqué {} fois.".format(self.nb_clic)

    def color_display(self,*args):
        if self.show_colors.get():
            self.color_choice = StringVar()
            self.color_choice.trace("w",self.change_colors)


            self.grey_radio = Radiobutton(self, text="Défaut", variable=self.color_choice, value=self.default_color)
            self.red_radio = Radiobutton(self, text="Rouge", variable=self.color_choice, value="red")
            self.green_radio = Radiobutton(self, text="Vert", variable=self.color_choice, value="green")
            self.blue_radio = Radiobutton(self, text="Bleu", variable=self.color_choice, value="blue")    
            
            self.grey_radio.grid(column=0,row=4,columnspan=2)
            self.red_radio.grid(column=0,row=5,columnspan=2)
            self.green_radio.grid(column=0,row=6,columnspan=2)
            self.blue_radio.grid(column=0,row=7,columnspan=2)

        else:
            self.grey_radio.destroy()
            self.red_radio.destroy()
            self.green_radio.destroy()
            self.blue_radio.destroy()
            del self.color_choice
            self.configure(bg=self.default_color)

        
    def change_colors(self,*args):
        self.configure(bg=self.color_choice.get())


        
if __name__ == "__main__":
    print("Tests :")

    fenetre = Tk()
    interface = Interface(fenetre,width=768, height=576, borderwidth=1)

    interface.mainloop()
    interface.destroy()