from tkinter import *
import bouton_math
import os
from PIL import ImageTk, Image
fenetre = Tk()
fenetre.geometry("1080x720")

class Code:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        chemin_actuel = os.path.abspath(__file__)
        self.boite = Frame(self.fenetre )

        self.boite.place(x=0,y=0, height=720, width= 1080)
        chemin_actuel = chemin_actuel.replace("code_principal.py", "image\\menu_prin\\Révision.png")
        image = Image.open(chemin_actuel)
        image = image.resize((1080, 720))
        self.image = ImageTk.PhotoImage(image)
        self.labelimage = Label(self.boite, image = self.image)
        self.labelimage.image = self.image 
        self.labelimage.place(x=0,y=0)
        g = bouton_math.init(fenetre = self.fenetre, boite =  self.boite)


run = Code(fenetre)
fenetre.mainloop()