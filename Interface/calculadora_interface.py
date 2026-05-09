from customtkinter import *

# Interface da Calculadora.
ic = CTk()
ic.geometry('400x600')
ic.resizable(False, False)
ic._set_appearance_mode('light')
ic.title('Calculadora')

valores_e_resultados = 0.0

# O frame principal do sistema.
frame_ic = CTkFrame(
    master=ic,
    # Tamanho geral. Largura e Altura.
    width=400, height=600,
    # Cor do fundo.
    fg_color='#ffffff',
    # Tamanho das bordas e arredondamento.
    border_width=0,
    corner_radius=0
)
frame_ic.place(x=0, y=0)

# As configurações do botão.
b_azul = {
    # As cores do botão.
    'fg_color': '#297ead', # Cor dele.
    'bg_color': '#ffffff', # Cor do fundo.
    'hover_color': '#1e6388', # Cor clique.
    'text_color': '#000', # Texto.
    # Largura, altura, borda e arredondamento.
    'width': 91.7,
    'height': 61.4,
    'border_width': 0,
    'corner_radius': 10,
    # Fonte do texto.
    'font': ("Garet", 20, "bold")
}

b_cinza = {
    # As cores do botão.
    'fg_color': '#b4b4b4', # Dele.
    'bg_color': '#ffffff', # Fundo.
    'hover_color': '#8A8A8A', # Clique.
    'text_color': '#000', # Texto.
    # Largura, altura, borda e arredondamento.
    'width': 91.7,
    'height': 61.4,
    'border_width': 0,
    'corner_radius': 10,
    # Fonte do texto.
    'font': ("Garet", 20, "bold")
}

b_branco = {
    # As cores do botão.
    'fg_color': '#d9d9d9', # Dele.
    'bg_color': '#ffffff', # Fundo.
    'hover_color': '#afafaf', # Clique.
    'text_color': '#000', # Texto.
    # Largura, altura, borda e arredondamento.
    'width': 91.7,
    'height': 61.4,
    'border_width': 0,
    'corner_radius': 10,
    # Fonte do texto.
    'font': ("Garet", 20, "bold")
}

# Botões azul.
botao_ce = CTkButton(
    frame_ic, **b_azul,
    text='CE',
    command=None
)
botao_ce.place(x=107.7, y=211.7)

botao_c = CTkButton(
    frame_ic, **b_azul,
    text='C',
    command=None
)
botao_c.place(x=201.5, y=211.7)

botao_mostrar = CTkButton(
    frame_ic, **b_azul,
    text='=',
    command=None
)
botao_mostrar.place(x=294.1, y=527.7)

# botões cinza.
botao_apagar = CTkButton(
    frame_ic, **b_cinza,
    text='<-',
    command=None
)
botao_apagar.place(x=295.2, y=211.7)

botao_porsentagem = CTkButton(
    frame_ic, **b_cinza,
    text='%',
    command=None
)
botao_porsentagem.place(x=14.2, y=274.8)

botao_elevado = CTkButton(
    frame_ic, **b_cinza,
    text='x²',
    command=None
)
botao_elevado.place(x=107.7, y=274.8)

botao_raiz = CTkButton(
    frame_ic, **b_cinza,
    text='²√x',
    command=None
)
botao_raiz.place(x=201.5, y=274.8)

botao_soma = CTkButton(
    frame_ic, **b_cinza,
    text='+',
    command=None
)
botao_soma.place(x=294.1, y=464.5)

botao_diminui = CTkButton(
    frame_ic, **b_cinza,
    text='-',
    command=None
).place(x=294.1, y=401.4)

botao_multiplica = CTkButton(
    frame_ic, **b_cinza,
    text='x',
    command=None
)
botao_multiplica.place(x=294.1, y=338.2)

botao_dividir = CTkButton(
    frame_ic, **b_cinza,
    text='/',
    command=None
)
botao_dividir.place(x=295.2, y=274.8)

# Branco.
botao_0 = CTkButton(
    frame_ic, **b_branco,
    text='0',
    command=None
)
botao_0.place(x=106.6, y=527.7)

botao_1 = CTkButton(
    frame_ic, **b_branco,
    text='1',
    command=None
)
botao_1.place(x=13, y=464.5)

botao_2 = CTkButton(
    frame_ic, **b_branco,
    text='2',
    command=None
)
botao_2.place(x=106.6, y=464.5)

botao_3 = CTkButton(
    frame_ic, **b_branco,
    text='3',
    command=None
)
botao_3.place(x=200.3, y=464.5)

botao_4 = CTkButton(
    frame_ic, **b_branco,
    text='4',
    command=None
)
botao_4.place(x=13, y=401.4)

botao_5 = CTkButton(
    frame_ic, **b_branco,
    text='5',
    command=None
)
botao_5.place(x=106.6, y=401.4)

botao_6 = CTkButton(
    frame_ic, **b_branco,
    text='6',
    command=None
)
botao_6.place(x=200.3, y=401.4)

botao_7 = CTkButton(
    frame_ic, **b_branco,
    text='7',
    command=None
)
botao_7.place(x=13, y=338.2)

botao_8 = CTkButton(
    frame_ic, **b_branco,
    text='8',
    command=None
)
botao_8.place(x=106.6, y=338.2)

botao_9 = CTkButton(
    frame_ic, **b_branco,
    text='9',
    command=None
)
botao_9.place(x=200.3, y=338.2)

botao_virgula = CTkButton(
    frame_ic, **b_branco,
    text=',',
    command=None
)
botao_virgula.place(x=200.3, y=527.7)

resultado = CTkLabel(
    frame_ic,
    width=372.8,
    height=59.7,
    text=valores_e_resultados,
    text_color='#000',
    font=("Garet", 40, "bold"),
    anchor="e"
)
resultado.place(x=14.2, y=120)

ic.mainloop()
