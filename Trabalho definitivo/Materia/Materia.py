import sqlite3
import tkinter as tk

# Criação e conexão com o banco de dados
conn = sqlite3.connect('diciplina.db')
cursor = conn.cursor()

# Criar as tabelas se elas não existirem
cursor.execute('''
                CREATE TABLE IF NOT EXISTS diciplina_key
                (name_dis TEXT, cod_dis TEXT)
                ''')

def configurar_estilos():
    root.tk_setPalette(background='#C9F3F5', foreground='#333333')
    root.option_add('*TButton.background', '#4CAF50')
    root.option_add('*TButton.foreground', '#ffffff')
    root.option_add('*TButton.font', ('Helvetica', 12))
    
    # Configurar a cor de fundo da Listbox como branca
    listbox.configure(bg='#FFFFFF')
    
    # Configurar a cor de fundo da caixa de entrada como branca
    name_dis_entry.configure(bg='#FFFFFF')
    cod_dis_entry.configure(bg='#FFFFFF')

    # Configurar a cor de fundo da caixa de registrar como branca
    add_button.configure(bg='#FFFFFF')

def add_disciplina():
    name_dis = name_dis_entry.get()
    cod_dis = cod_dis_entry.get()
    cursor.execute("INSERT INTO diciplina_key VALUES (?, ?)", (name_dis, cod_dis))
    conn.commit()
    name_dis_entry.delete(0, tk.END)
    cod_dis_entry.delete(0, tk.END)
    update_list()

def remover_disciplina(event):
    selecionado = listbox.curselection()
    if selecionado:
        nome_diciplina = listbox.get(selecionado).split(" - ")[0]
        codigo = listbox.get(selecionado).split(" - ")[1]
        cursor.execute("DELETE FROM diciplina_key WHERE name_dis = ? AND cod_dis = ?", (nome_diciplina, codigo))
        conn.commit()
        update_list()

def update_list():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT name_dis, cod_dis FROM diciplina_key")
    for row in cursor.fetchall():
        listbox.insert(tk.END, f"{row[0]} - {row[1]}")

# Criação da interface gráfica
root = tk.Tk()
root.title("Cadastro de Disciplina")

largura_janela = 900
altura_janela = 900

# Label e entrada para matrícula
label_cod_dis = tk.Label(root, text="Codigo", font="Arial 14 bold")
label_cod_dis.grid(row=1, column=0)
cod_dis_entry = tk.Entry(root)
cod_dis_entry.grid(row=1, column=1)

# Label e entrada para nome
label_name_dis = tk.Label(root, text="Nome da diciplina", font="Arial 14 bold")
label_name_dis.grid(row=0, column=0)
name_dis_entry = tk.Entry(root)
name_dis_entry.grid(row=0, column=1)

#Deixar um espaço vazio
header_void_2 = tk.Label(root, text=" ")
header_void_2.grid(row=4, column=1)

# Botão para adicionar aluno
add_button = tk.Button(root, text="Registrar", font="Arial 14 bold", command=add_disciplina)
add_button.grid(row=5, column=1)

#Deixar um espaço vazio
header_void = tk.Label(root, text=" ")
header_void.grid(row=6, column=1)

# Listagem para as chaves que foram pegas
header_2 = tk.Label(root, text="Codigo - Disciplina")
header_2.grid(row=7, column=1)
listbox = tk.Listbox(root, width=45)
listbox.grid(row=8, column=1)
listbox.bind('<Double-1>', remover_disciplina)

update_list()
configurar_estilos()

# Obter largura e altura da tela
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
pos_x = (largura_tela // 2) - (largura_janela // 2)
pos_y = (altura_tela // 2) - (altura_tela // 2)

# Define a posição da janela
root.geometry('{}x{}+{}+{}'.format(largura_janela, altura_janela, pos_x, pos_y))

# Manter a tela em funcionamento
root.mainloop()
