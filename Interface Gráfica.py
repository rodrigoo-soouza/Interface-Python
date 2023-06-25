from tkinter import *
from tkinter import ttk
import sqlite3

janela = Tk()

class Funcs():
    def limpa_tela(self):
        self.codigo_entrada.delete(0, END)
        self.nome_entrada.delete(0, END)
        self.telefone_entrada.delete(0, END)
        self.cidade_entrada.delete(0, END)
    def conecta_bd(self):
        self.conecta = sqlite3.connect('clientes.bd')
        self.cursor = self.conecta.cursor()
        print('Conectando ao Banco de Dados')
    def desconecta_bd(self):
        self.conecta.close()
        print('Desconetando ao banco de dados')
    def monta_tabela(self):
        self.conecta_bd()
        #Criar Tabela
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            cod INTEGER PRIMARY KEY,
            nome_cliente CHAR(40) NOT NULL,
            telefone INTEGER(20),
            cidade CHAR(40)        
        );
    """)
        self.conecta.commit(); print('Banco de Criado')
        self.desconecta_bd()
    def adiciona_cliente(self):
        self.codigo = self.codigo_entrada.get()
        self.nome = self.nome_entrada.get()
        self.telefone = self.telefone_entrada.get()
        self.cidade = self.cidade_entrada.get()
        self.conecta_bd()

        self.cursor.execute("""INSERT INTO clientes (nome_cliente, telefone, cidade)
         VALUES (?, ?, ?)""", (self.nome, self.telefone, self.cidade))
        self.conecta.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes
        ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconecta_bd()

class Aplicacao(Funcs):

    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames_da_tela()
        self.criando_widgets()
        self.lista_frame2()
        self.monta_tabela()
        self.select_lista()
        janela.mainloop()

#Configuração da Janela

    def tela(self):
        self.janela.title('Cadastro de Clientes')
        self.janela.configure(background='#1e3743')
        self.janela.geometry("700x600")
        self.janela.resizable(True, True)
        self.janela.maxsize(width=900, height=700)
        self.janela.minsize(width=400, height=300)

#Configuração dos frames

    def frames_da_tela(self):
        self.frame_1 = Frame(self.janela, bd=4, bg='#dfe3ee', highlightbackground='#759feb', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.frame_2 = Frame(self.janela, bd=4, bg='#dfe3ee', highlightbackground='#759feb', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

#Criando botões

    def criando_widgets(self):
        # Botão Limpar
        self.bt_limpar = Button(self.frame_1, text='Limpar', bd=2, bg='#107db2', fg='white',
                                font=('verdana', 8, 'bold'), command=self.limpa_tela)
        self.bt_limpar.place(relx=0.2, rely=0.1, relheight=0.1, relwidth=0.15)
        #Botão Buscar
        self.bt_buscar = Button(self.frame_1, text='Buscar', bd=2, bg='#107db2', fg='white',
                                font=('verdana', 8, 'bold'), command=self.limpa_tela)
        self.bt_buscar.place(relx=0.35, rely=0.1, relheight=0.1, relwidth=0.15)
        #Botão Novo
        self.bt_novo = Button(self.frame_1, text='Novo', bd=2, bg='#107db2', fg='white',
                              font=('verdana', 8, 'bold'), command=self.adiciona_cliente)
        self.bt_novo.place(relx=0.55, rely=0.1, relheight=0.1, relwidth=0.15)
        #Botão Alterar
        self.bt_alterar = Button(self.frame_1, text='Alterar', bd=2, bg='#107db2', fg='white',
                                 font=('verdana', 8, 'bold'), command=self.limpa_tela)
        self.bt_alterar.place(relx=0.7, rely=0.1, relheight=0.1, relwidth=0.15)
        #Botão Apagar
        self.bt_apagar = Button(self.frame_1, text='Apagar', bd=2, bg='#107db2', fg='white',
                                font=('verdana', 8, 'bold'), command=self.limpa_tela)
        self.bt_apagar.place(relx=0.85, rely=0.1, relheight=0.1, relwidth=0.15)

#Criando Label e entrada
        #Label e entrada código
        self.lb_entrada = Label(self.frame_1, text='Código', bg='#dfe3ee', fg='#107db2')
        self.lb_entrada.place(relx=0.05, rely=0.05)
        self.codigo_entrada = Entry(self.frame_1)
        self.codigo_entrada.place(relx=0.05, rely=0.15, relwidth=0.08)

        #Label e entrada de nome
        self.lb_nome = Label(self.frame_1, text='Nome', bg='#dfe3ee', fg='#107db2')
        self.lb_nome.place(relx=0.05, rely=0.35)
        self.nome_entrada = Entry(self.frame_1)
        self.nome_entrada.place(relx=0.05, rely=0.45, relwidth=0.8)

        #Label e entrada da telefone
        self.lb_telefone = Label(self.frame_1, text='Telefone', bg='#dfe3ee', fg='#107db2')
        self.lb_telefone.place(relx=0.05, rely=0.6)
        self.telefone_entrada = Entry(self.frame_1)
        self.telefone_entrada.place(relx=0.05, rely=0.7, relwidth=0.2)

        #Label e entrada da cidade
        self.lb_cidade = Label(self.frame_1, text='Cidade', bg='#dfe3ee', fg='#107db2')
        self.lb_cidade.place(relx=0.5, rely=0.6)
        self.cidade_entrada = Entry(self.frame_1)
        self.cidade_entrada.place(relx=0.5, rely=0.7, relwidth=0.4)

#Criando Treeview com colunas

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3, columns=('coluna_1', 'coluna_2', 'coluna_3', 'coluna_4'))
        self.listaCli.heading('#0', text='')
        #Coluna Codigo
        self.listaCli.heading('#1', text='Código')
        #Coluna Nome
        self.listaCli.heading('#2', text='Nome')
        #Coluna Telefone
        self.listaCli.heading('#3', text='Telefone')
        #Coluna Cidade
        self.listaCli.heading('#4', text='Cidade')

        #Especifica o tamanho da coluna com relação a lista
        self.listaCli.column('#0', width=1)
        self.listaCli.column('#1', width=50)
        self.listaCli.column('#2', width=200)
        self.listaCli.column('#3', width=125)
        self.listaCli.column('#4', width=125)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        # self.barra_rol_lista = Scrollbar(self.frame_2, orient='vertical')
        # self.listaCli.configure(yscrollcommand=self.barra_rol_lista.set)
        # self.barra_rol_lista.place(relx=0.96, rely=0.1, relwidth=0.84, relheight=0.85)


Aplicacao()
