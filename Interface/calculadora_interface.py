from customtkinter import *

# Interface da Calculadora.
ic = CTk()
ic.geometry('400x600')
ic.resizable(False, False)

ic.title('Calculadora')
ic._set_appearance_mode('light')

# O frame principal do sistema.
frame_ic = CTkFrame(
    master=ic,
    # Tamanho geral.
    width=400,
    height=600,
    fg_color='#ffffff',
    # Bordas.
    border_width=0,
    corner_radius=0
)
frame_ic.place(x=0, y=0)

# botões azul.
botao_ce = CTkButton(
    frame_ic,
    # tamanho.
    width=91.7,
    height=61.4,
    #cor.
    fg_color='#297ead',
    bg_color='#ffffff',
    hover_color="#1e6388",
    # borda.
    border_width=0,
    corner_radius=10,
    # texto.
    text='CE',
    text_color='#000',
    font=("Garet", 20, "bold"),
    # comando.
    command=None
)
botao_ce.place(x=107.7, y=211.7)

botao_c = CTkButton(
    frame_ic,
    # tamanho.
    width=91.7,
    height=61.4,
    #cor.
    fg_color='#297ead',
    bg_color='#ffffff',
    hover_color="#1e6388",
    # borda.
    border_width=0,
    corner_radius=10,
    # texto.
    text='C',
    text_color='#000',
    font=("Garet", 20, "bold"),
    # comando.
    command=None
).place(x=201.5, y=211.7)

botao_mostrar = CTkButton(
    frame_ic,
    # tamanho.
    width=91.7,
    height=61.4,
    #cor.
    fg_color='#297ead',
    bg_color='#ffffff',
    hover_color="#1e6388",
    # borda.
    border_width=0,
    corner_radius=10,
    # texto.
    text='=',
    text_color='#000',
    font=("Garet", 20, "bold"),
    # comando.
    command=None
).place(x=294.1, y=527.7)

# botões cinza.
botao_apagar = CTkButton(
    frame_ic,
    # tamanho.
    width=91.7,
    height=61.4,
    #cor.
    fg_color='#b4b4b4',
    bg_color='#ffffff',
    hover_color="#8A8A8A",
    # borda.
    border_width=0,
    corner_radius=10,
    # texto.
    text='<—',
    text_color='#000',
    font=("Garet", 20, "bold"),
    # comando.
    command=None
).place(x=295.2, y=211.7)

botao_porsentagem = CTkButton(
    frame_ic,
    # tamanho.
    width=91.7,
    height=61.4,
    #cor.
    fg_color='#b4b4b4',
    bg_color='#ffffff',
    hover_color="#8A8A8A",
    # borda.
    border_width=0,
    corner_radius=10,
    # texto.
    text='%',
    text_color='#000',
    font=("Garet", 20, "bold"),
    # comando.
    command=None
).place(x=14.2, y=274.8)

botao_elevado = CTkButton(
    frame_ic,
    # tamanho.
    width=91.7,
    height=61.4,
    #cor.
    fg_color='#b4b4b4',
    bg_color='#ffffff',
    hover_color="#8A8A8A",
    # borda.
    border_width=0,
    corner_radius=10,
    # texto.
    text='x²',
    text_color='#000',
    font=("Garet", 20, "bold"),
    # comando.
    command=None
).place(x=107.7, y=274.8)

botao_raiz = CTkButton(
    frame_ic,
    # tamanho.
    width=91.7,
    height=61.4,
    #cor.
    fg_color='#b4b4b4',
    bg_color='#ffffff',
    hover_color="#8A8A8A",
    # borda.
    border_width=0,
    corner_radius=10,
    # texto.
    text='²√x',
    text_color='#000',
    font=("Garet", 20, "bold"),
    # comando.
    command=None
).place(x=201.5, y=274.8)

botao_soma = CTkButton(
    frame_ic,
    # tamanho.
    width=91.7,
    height=61.4,
    #cor.
    fg_color='#b4b4b4',
    bg_color='#ffffff',
    hover_color="#8A8A8A",
    # borda.
    border_width=0,
    corner_radius=10,
    # texto.
    text='+',
    text_color='#000',
    font=("Garet", 20, "bold"),
    # comando.
    command=None
).place(x=294.1, y=464.5)

botao_diminui = CTkButton(
    frame_ic,
    # tamanho.
    width=91.7,
    height=61.4,
    #cor.
    fg_color='#b4b4b4',
    bg_color='#ffffff',
    hover_color="#8A8A8A",
    # borda.
    border_width=0,
    corner_radius=10,
    # texto.
    text='-',
    text_color='#000',
    font=("Garet", 20, "bold"),
    # comando.
    command=None
).place(x=294.1, y=401.4)

botao_multiplica = CTkButton(
    frame_ic,
    # tamanho.
    width=91.7,
    height=61.4,
    #cor.
    fg_color='#b4b4b4',
    bg_color='#ffffff',
    hover_color="#8A8A8A",
    # borda.
    border_width=0,
    corner_radius=10,
    # texto.
    text='x',
    text_color='#000',
    font=("Garet", 20, "bold"),
    # comando.
    command=None
).place(x=294.1, y=338.2)

botao_dividir = CTkButton(
    frame_ic,
    # tamanho.
    width=91.7,
    height=61.4,
    #cor.
    fg_color='#b4b4b4',
    bg_color='#ffffff',
    hover_color="#8A8A8A",
    # borda.
    border_width=0,
    corner_radius=10,
    # texto.
    text='/',
    text_color='#000',
    font=("Garet", 20, "bold"),
    # comando.
    command=None
).place(x=295.2, y=274.8)

# brancos.
botao_0 = CTkButton(
    frame_ic,
    # tamanho.
    width=91.7,
    height=61.4,
    #cor.
    fg_color='#d9d9d9',
    bg_color='#ffffff',
    hover_color="#afafaf",
    # borda.
    border_width=0,
    corner_radius=10,
    # texto.
    text='0',
    text_color='#000',
    font=("Garet", 20, "bold"),
    # comando.
    command=None
).place(x=106.6, y=527.7)

ic.mainloop()
