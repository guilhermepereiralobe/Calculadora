from customtkinter import *
from backend.calculadora_logic import *

# Interface da Calculadora.
# Tamannho da interface, ela não pode aumentar e está no modo claro,
ic = CTk()
ic.geometry('400x600')
ic.resizable(False, False)
ic._set_appearance_mode('light')
ic.title('Calculadora')

# Aqui, é para mostrar os valores que seram calculadores e o resultado.
valores_e_resultados = 0


def clicar_numero(numero):
    global adicionar_numero

    resultado_backend = adicionar_numero(numero)

    resultado.configure(text=resultado_backend)




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
frame_ic.place(x=0, y=0) # Corrdenadas.

# As configurações do botão.
b_azul = {
    # As cores do botão.
    'fg_color': '#297ead', # Cor dele.
    'bg_color': '#ffffff', # Cor do fundo.
    'hover_color': '#1e6388', # Cor quando passar por cima.
    'text_color': '#000', # Cor do texto.
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
# Ce é limpar entrada.
botao_ce = CTkButton(
    frame_ic, **b_azul, # Aqui mostra que botao_ce está dentro da hierarquia do frame_ic e, além disso, está usando a configuração do botão azul (b_azul).
    text='CE', # O texto do botão.
    command=None # Onde é para ser colocado o comando.
)
botao_ce.place(x=107.7, y=211.7) # Onde fica o botão.
# Esse padrão vai se repetir em todo o arquivo.


# C é limpar tudo.
botao_c = CTkButton(
    frame_ic, **b_azul,
    text='C',
    command=lambda: resultado.configure(text=limpar_tela())
)
botao_c.place(x=201.5, y=211.7)

botao_mostrar = CTkButton(
    frame_ic, **b_azul,
    text='=',
    command=lambda: resultado.configure(text=calcular())
)
botao_mostrar.place(x=294.1, y=527.7)

# botões cinza.
# Esse botão é para apagar um digito na entrada.
botao_apagar = CTkButton(
    frame_ic, **b_cinza,
    text='<-',
    command=None
)
botao_apagar.place(x=295.2, y=211.7)

# Essa teclada é para fazer a porsentagem.
botao_porsentagem = CTkButton(
    frame_ic, **b_cinza,
    text='%',
    command=None
)
botao_porsentagem.place(x=14.2, y=274.8)

# Essa teclada ser para fazer os calculos de eleveção. 2 elevado ao quadrado (2²).
botao_elevado = CTkButton(
    frame_ic, **b_cinza,
    text='x²',
    command=lambda: resultado.configure(text=def_operação("x²"))
)
botao_elevado.place(x=107.7, y=274.8)

# Esse serve para calcular a raiz quadrada (²√x)
botao_raiz = CTkButton(
    frame_ic, **b_cinza,
    text='²√x',
    command=lambda: resultado.configure(text=def_operação("²√x"))
)
botao_raiz.place(x=201.5, y=274.8)

# Somar valores (1+1)
botao_soma = CTkButton(
    frame_ic, **b_cinza,
    text='+',
    command=lambda: def_operação("+")
    

)
botao_soma.place(x=294.1, y=464.5)

# Diminuir valores (1-1)
botao_diminui = CTkButton(
    frame_ic, **b_cinza,
    text='-',
    command=lambda: resultado.configure(text=def_operação("-"))
).place(x=294.1, y=401.4)

# Multiplicar valores (2 * 2)
botao_multiplica = CTkButton(
    frame_ic, **b_cinza,
    text='x',
    command=lambda: resultado.configure(text=def_operação("x"))
)
botao_multiplica.place(x=294.1, y=338.2)

# Dividir valores (4/2), lembrando que, não pode ter divisão de 0.
botao_dividir = CTkButton(
    frame_ic, **b_cinza,
    text='/',
    command=lambda: resultado.configure(text=def_operação("/"))
)
botao_dividir.place(x=295.2, y=274.8)

# Branco.
# Botão do numero 0.
botao_0 = CTkButton(
    frame_ic, **b_branco,
    text='0',
    command=lambda: clicar_numero(0)
)
botao_0.place(x=106.6, y=527.7)

# Botão do numero 1.
botao_1 = CTkButton(
    frame_ic, **b_branco,
    text='1',
    command=lambda:  clicar_numero(1)
)
botao_1.place(x=13, y=464.5)

# Botão do numero 2.
botao_2 = CTkButton(
    frame_ic, **b_branco,
    text='2',
    command=lambda: clicar_numero(2)
)
botao_2.place(x=106.6, y=464.5)

# Botão do numero 3.
botao_3 = CTkButton(
    frame_ic, **b_branco,
    text='3',
    command=lambda: clicar_numero(3)
)
botao_3.place(x=200.3, y=464.5)

# Botão do numero 4.
botao_4 = CTkButton(
    frame_ic, **b_branco,
    text='4',
    command=lambda: clicar_numero(4)
)
botao_4.place(x=13, y=401.4)

# Botão do numero 5.
botao_5 = CTkButton(
    frame_ic, **b_branco,
    text='5',
    command=lambda: clicar_numero(5)
)
botao_5.place(x=106.6, y=401.4)

# Botão do numero 6.
botao_6 = CTkButton(
    frame_ic, **b_branco,
    text='6',
    command=lambda:clicar_numero(6)
)
botao_6.place(x=200.3, y=401.4)

# Botão do numero 7.
botao_7 = CTkButton(
    frame_ic, **b_branco,
    text='7',
    command=lambda: clicar_numero(7)
)
botao_7.place(x=13, y=338.2)

# Botão do numero 8.
botao_8 = CTkButton(
    frame_ic, **b_branco,
    text='8',
    command=lambda: clicar_numero(8)
)
botao_8.place(x=106.6, y=338.2)

# Botão do numero 9.
botao_9 = CTkButton(
    frame_ic, **b_branco,
    text='9',
    command=lambda: clicar_numero(9)
)
botao_9.place(x=200.3, y=338.2)

# Botão do numero da virgula (,).
botao_virgula = CTkButton(
    frame_ic, **b_branco,
    text=',',
    command=None
)
botao_virgula.place(x=200.3, y=527.7)

# Onde os valores de números e resultados seram mostrados.
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
