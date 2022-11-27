import os
import mysql.connector
from tkinter import *
from cores import *
from tkinter import messagebox
from dotenv import load_dotenv

load_dotenv('./env')


def conectar(event=None):
    try:
        conn = mysql.connector.connect(
            host=os.environ['host'],
            port=os.environ['port'],
            user= campo_nome.get(),
            passwd=campo_senha.get(),
            db =os.environ['db']
        )
    except:
        messagebox.showerror('Erro')
    else:
        messagebox.showinfo('Conectado')
    finally:
        campo_nome.delete(0,'end')
        campo_senha.delete(0,'end')
        campo_nome.focus()


janela =Tk()
janela.title('Projeto #1')
janela.geometry('310x310')
janela.resizable(width=FALSE, height=FALSE)
janela.bind('<Return>', conectar)


frame_superior =Frame(
    janela,
    width=310,
    height=50,
    bg=COR_FUNDO
)
frame_superior.grid(row=0,column=0,sticky=NSEW)

frame_inferior = Frame (
    janela,
    width=310,
    height=250,
    bg=COR_FUNDO
)
frame_inferior.grid(row=1, column=0, sticky=NSEW)

titulo = Label(
    frame_superior,
    text='Login',
    anchor=NW,
    font=('Malgun Gothic', 22),
    bg=COR_FUNDO,
    fg=COR_LETRA 
)
titulo.place(x=5, y=4)

linha =Label(
    frame_superior,
    width=275,
    anchor=NW,
    bg=COR_IN
)
linha.place(x=20, y=48)

nome =Label(
    frame_inferior,
    text='Nome',
    anchor=NW,
    font=('Malgun Gothic', 14),
    bg=COR_FUNDO,
    fg=COR_LETRA
)
nome.place(x=10, y=20)

campo_nome = Entry(
    frame_inferior,
    width=28,
    justify='left',
    font=('Malgun Gothic', 14),
    highlightthickness =1,
    relief='solid'
)
campo_nome.place(x=10, y=50)
campo_nome.focus()


senha =Label(
    frame_inferior,
    text='Senha',
    anchor=NW,
    font=('Malgun Gothic', 14),
    bg=COR_FUNDO,
    fg=COR_LETRA
)
senha.place(x=10,y=95)

campo_senha = Entry(
    frame_inferior,
    width=28,
    justify='left',
    show='>',
    font=('Malgun Gothic', 14),
    highlightthickness =1,
    relief='solid'
)
campo_senha.place(x=10, y=130)

btn_entrar =Button(
    frame_inferior,
    text='Entrar',
    font=('Malgun Gothic', 14),
    width=25,
    bg=COR_IN,
    fg=COR_FUNDO,
    command=conectar
)
btn_entrar.place(x=10,y=180)





if __name__ == '__main__':
        janela.mainloop()

