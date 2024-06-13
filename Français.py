from tkinter import *
import random
fenetre = Tk()
fenetre.geometry("1080x720")

class Code:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.titre_mth = Label(self.fenetre, text = "Français", font = ("French Script MT",80))
        self.titre_mth.place(x=420,y=0)
        self.parti_qts = Frame(self.fenetre, height= 720, width= 1080)
        self.parti_qts.place(x=0,y=125)

        self.choisir_question_aléatoirement()


    def choisir_question_aléatoirement(self):
        self.parti_qts.destroy()
        self.parti_qts = Frame(self.fenetre, height= 720, width= 1080)
        self.parti_qts.place(x=0,y=125)
        qts = random.randint(0,1)
        match qts:
            case 0:
                pass

    class conjugaion:

run  = Code(fenetre)
fenetre.mainloop()