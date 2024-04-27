import sqlite3
import tkinter as tk

# Criação e conexão com o banco de dados
conn = sqlite3.connect('professor.db')
cursor = conn.cursor()

# Criar as tabelas se elas não existirem
cursor.execute('''
                CREATE TABLE IF NOT EXISTS prof_key
                (name_prof TEXT, mat_prof TEXT)
                ''')

def configurar_estilos():
    root.tk_setPalette(background='#C9F3F5', foreground='#333333')
    root.option_add('*TButton.background', '#4CAF50')
    root.option_add('*TButton.foreground', '#ffffff')
    root.option_add('*TButton.font', ('Helvetica', 12))
    
    # Configurar a cor de fundo da Listbox como branca
    listbox.configure(bg='#FFFFFF')
    
    # Configurar a cor de fundo da caixa de entrada como branca
    name_prof_entry.configure(bg='#FFFFFF')
    mat_prof_entry.configure(bg='#FFFFFF')

    # Configurar a cor de fundo da caixa de registrar como branca
    add_button.configure(bg='#FFFFFF')

def add_professor():
    name_prof = name_prof_entry.get()
    mat_prof = mat_prof_entry.get()
    cursor.execute("INSERT INTO prof_key VALUES (?, ?)", (name_prof, mat_prof))
    conn.commit()
    name_prof_entry.delete(0, tk.END)
    mat_prof_entry.delete(0, tk.END)
    update_list()

def remover_professor(event):
    selecionado = listbox.curselection()
    if selecionado:
        nome_prof = listbox.get(selecionado).split(" - ")[0]
        matricula_prof = listbox.get(selecionado).split(" - ")[1]
        cursor.execute("DELETE FROM prof_key WHERE name_prof = ? AND mat_prof = ?", (nome_prof, matricula_prof))
        conn.commit()
        update_list()

def update_list():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT name_prof, mat_prof FROM prof_key")
    for row in cursor.fetchall():
        listbox.insert(tk.END, f"{row[0]} - {row[1]}")

# Criação da interface gráfica
root = tk.Tk()
root.title("Cadastro de Professores")

largura_janela = 900
altura_janela = 900

# Label e entrada para nome
label_name_prof = tk.Label(root, text="Nome do Professor", font="Arial 14 bold")
label_name_prof.grid(row=0, column=0)
name_prof_entry = tk.Entry(root)
name_prof_entry.grid(row=0, column=1)

# Label e entrada para matrícula
label_mat_prof = tk.Label(root, text="Matrícula", font="Arial 14 bold")
label_mat_prof.grid(row=1, column=0)
mat_prof_entry = tk.Entry(root)
mat_prof_entry.grid(row=1, column=1)

#Deixar um espaço vazio
header_void_2 = tk.Label(root, text=" ")
header_void_2.grid(row=4, column=1)

# Botão para adicionar aluno
add_button = tk.Button(root, text="Registrar", font="Arial 14 bold", command=add_professor)
add_button.grid(row=5, column=1)

#Deixar um espaço vazio
header_void = tk.Label(root, text=" ")
header_void.grid(row=6, column=1)

# Listagem para as chaves que foram pegas
header_2 = tk.Label(root, text="Nome do Professor - Matrícula")
header_2.grid(row=7, column=1)
listbox = tk.Listbox(root, width=45)
listbox.grid(row=8, column=1)
listbox.bind('<Double-1>', remover_professor)

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
