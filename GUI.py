from tkinter import *
from tkinter.font import Font
from playsound import playsound
import time

#===== Def das cores ======#
PRETO = '#000000'
CINZACLARO = '#D3DEE6'
AZULCLARO = '#7AC0E2'
AZULMEDIO = '#2C6fAB'
AZULESCURO = '#035094'

sons = ["sons/asmei.mp3","sons/c oc que da c fala.mp3", "sons/cavalo.mp3", "sons/como e amg.mp3", 
"sons/iiihhaa.mp3", "sons/masqueicu.mp3", "sons/pare!!.mp3", "sons/paro paro.mp3", "sons/PIU.mp3", "sons/q tiro foi esse.mp3",
"sons/rapaiz.mp3", "sons/sera.mp3", "sons/sexy sax.mp3", "sons/TEI.mp3", "sons/uepa.mp3", "sons/ze da manga.mp3", "sons/james 1.mp3",
"sons/james 2.mp3", "sons/felca ta certo isso.mp3", "sons/oskey.mp3"]
botao = []

def tocaAudio(som):
        playsound(sound=som, block=False)

class gui:
    def __init__(self, master, imgIcone, fonteTxt, frameTitulo, frameBotoes, txtTitulo, audios, botoes, icone):
        self.master = master
        self.imgIcone = imgIcone
        self.fonteTxt = fonteTxt
        self.frameTitulo = frameTitulo
        self.frameBotoes = frameBotoes
        self.txtTitulo = txtTitulo
        self.audios = audios
        self.botoes = botoes
        self.icone = icone

    def criaGUI(self):
        self.master = Tk()

        self.icone = PhotoImage(file="imagens/icon.png")

        self.master.title("Efeito Sonoros")
        self.master.iconphoto(False, self.icone) #colocar a img do icone
        self.master.geometry("1280x720")
        self.master.state("zoomed")
        self.master.config(background=AZULESCURO)

        #==== Fonte ====#
        self.fonteTxt = Font(
            family="Lovelo Black",
            size=19,
            weight="bold"
        )

        #==== Frames ====#
        self.frameTitulo = Frame(
            self.master,
            background=AZULESCURO,
            bd=4
        )
        self.frameTitulo.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.08)

        self.frameBotoes = Frame(
            self.master,
            background=AZULMEDIO,
            bd=4
        )
        self.frameBotoes.place(relx=0.02, rely=0.1, relwidth=0.96,relheight=0.88)
        

        #==== Txt título ====#
        self.txtTitulo = Label(
            self.frameTitulo,
            font=self.fonteTxt,
            fg=CINZACLARO,
            bd=10,
            text="MESA DE SOM",
            background=AZULESCURO
        )
        self.txtTitulo.place(relx=0, rely=0, relwidth=1, relheight=1)


        #==== Botões ====#
        self.audios = sons
        self.botoes = botao

        for i in range(len(self.audios)):
            txtBruto = self.audios[i]
            txt = txtBruto.replace("sons/", "").replace(".mp3", "")
            botaoCriado = Button(
                self.frameBotoes,
                text=txt,
                font=self.fonteTxt,
                background=CINZACLARO,
                foreground=PRETO,
                activebackground=AZULESCURO,
                activeforeground=PRETO,
                relief=RAISED,
                bd=4
            )
            self.botoes.append(botaoCriado)

        self.botoes[0]["command"] = lambda: tocaAudio(self.audios[0])
        self.botoes[1]["command"] = lambda: tocaAudio(self.audios[1])
        self.botoes[2]["command"] = lambda: tocaAudio(self.audios[2])
        self.botoes[3]["command"] = lambda: tocaAudio(self.audios[3])
        self.botoes[4]["command"] = lambda: tocaAudio(self.audios[4])
        self.botoes[5]["command"] = lambda: tocaAudio(self.audios[5])
        self.botoes[6]["command"] = lambda: tocaAudio(self.audios[6])
        self.botoes[7]["command"] = lambda: tocaAudio(self.audios[7])
        self.botoes[8]["command"] = lambda: tocaAudio(self.audios[8])
        self.botoes[9]["command"] = lambda: tocaAudio(self.audios[9])
        self.botoes[10]["command"] = lambda: tocaAudio(self.audios[10])
        self.botoes[11]["command"] = lambda: tocaAudio(self.audios[11])
        self.botoes[12]["command"] = lambda: tocaAudio(self.audios[12])
        self.botoes[13]["command"] = lambda: tocaAudio(self.audios[13])
        self.botoes[14]["command"] = lambda: tocaAudio(self.audios[14])
        self.botoes[15]["command"] = lambda: tocaAudio(self.audios[15])
        self.botoes[16]["command"] = lambda: tocaAudio(self.audios[16])
        self.botoes[17]["command"] = lambda: tocaAudio(self.audios[17])
        self.botoes[18]["command"] = lambda: tocaAudio(self.audios[18])
        self.botoes[19]["command"] = lambda: tocaAudio(self.audios[19])

        numDeSons = len(self.audios)

        numColunaUltimaL = numDeSons%4
        numLinhas = int(numDeSons/4) + 1

        alturaBotao = (0.98-(0.02*(numLinhas)))/numLinhas

        for linha in range(numLinhas):
            if linha == numLinhas-1:
                numColuna = numColunaUltimaL
            else:
                numColuna = 4
            for coluna in range(numColuna):
                self.botoes[4*linha + coluna].place(relx=((coluna*0.245) + 0.02), rely=(linha*(alturaBotao+0.02)+0.02), relwidth=0.225, relheight=alturaBotao)

        self.master.mainloop()
