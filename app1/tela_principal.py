from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
from funcoes import*


caminho = "PROJETO-PROGRAMACAO/app1/images/"


janela_principal =Tk()
janela_principal.geometry ("640x480+300+100")
janela_principal.title("Library Sis")
janela_principal.iconbitmap(caminho+"icon.ico")   
janela_principal.resizable(0,0)

#imagem de fundo
img_bg = ImageTk.PhotoImage(Image.open(caminho+"bg.jpg"))
label_tela = Label(janela_principal, image = img_bg).place(x=-5,y=0)

#logo
logo = ImageTk.PhotoImage(Image.open(caminho+"logo.png"))
label_logo = Label(janela_principal, image = logo, borderwidth=0).place(x=220,y=2)

#Imagens do botões
imagem_pesquisa = ImageTk.PhotoImage(Image.open(caminho+"busca_2.png"))
imagem_cadastro = ImageTk.PhotoImage(Image.open(caminho+"cadastro.png"))
imagem_cadastro_cliente = ImageTk.PhotoImage(Image.open(caminho+"cadastro_pessoa.png"))
imagem_venda = ImageTk.PhotoImage(Image.open(caminho+"venda.png"))

#Botoes que iniciam as funcionalidades do código
button_pesquisa = Button(janela_principal, image=imagem_pesquisa)
button_pesquisa.place(x=80, y=130)

button_cadastro = Button(janela_principal, image=imagem_cadastro,command=criar_tela_cadastro)
button_cadastro.place(x=210, y=130)

button_cadastro_cliente = Button(janela_principal, image=imagem_cadastro_cliente)
button_cadastro_cliente.place(x=340, y=130)

button_venda = Button(janela_principal,image=imagem_venda)
button_venda.place(x=470, y=130)

#Botão para sair do programa!
botao1 = Button(janela_principal, text='Sair',font=('Helvetica', 8, 'bold'), width=10, command=lambda:sair(janela_principal))
botao1.place(x=550, y=445)

#mainloop executa o loop que permite a janela permanecer aberta
janela_principal.mainloop()


