import tkinter as tk
from tkinter import messagebox

# Fatores de Conversão
CONVERSAO_MJ_KWH = 3.6
EFICIENCIA = 0.30  # Eficiência fixa de 30%

# Dicionário com PCI (Poder Calorífico Inferior) de diferentes tipos de biomassa
pci_biomassa = {
    "residuos_agricolas": 15,   # MJ/kg
    "residuos_madeira": 17,     # MJ/kg
    "residuos_alimentares": 5,  # MJ/kg
    "estrume_animal": 4         # MJ/kg
}

# Função para calcular a energia gerada
def calcular_energia(pci, quantidade):
    energia = (pci * EFICIENCIA * quantidade) / CONVERSAO_MJ_KWH
    return energia

# Função para adicionar biomassa e calcular a energia
def adicionar_biomassa():
    try:
        tipo_opcao = tipo_var.get()
        quantidade = float(quantidade_entry.get())

        if quantidade <= 0:
            messagebox.showerror("Erro", "A quantidade deve ser maior que zero.")
            return

        if tipo_opcao == "1":
            tipo = "residuos_agricolas"
        elif tipo_opcao == "2":
            tipo = "residuos_madeira"
        elif tipo_opcao == "3":
            tipo = "residuos_alimentares"
        elif tipo_opcao == "4":
            tipo = "estrume_animal"
        else:
            messagebox.showerror("Erro", "Opção inválida.")
            return

        # Limpa o último cálculo antes de adicionar novos valores
        biomassa_lista.delete(0, tk.END)
        energia_lista.delete(0, tk.END)

        # Adiciona a quantidade ao total
        total_quantidade.set(total_quantidade.get() + quantidade)
        quantidades[tipo] = quantidades.get(tipo, 0) + quantidade

        # Atualiza a lista de biomassa adicionada
        biomassa_lista.insert(tk.END, f"{tipo.replace('_', ' ').title()}: {quantidade} kg")

        # Atualiza energia total
        calcular_energia_total()

        # Limpa o campo de entrada
        quantidade_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Erro", "Digite um valor numérico válido para a quantidade.")

# Função para calcular a energia total
def calcular_energia_total():
    energia_total = 0
    energia_individual = []
    for tipo, quantidade in quantidades.items():
        pci = pci_biomassa[tipo]
        energia = calcular_energia(pci, quantidade)
        energia_total += energia
        porcentagem = (quantidade / total_quantidade.get()) * 100
        energia_individual.append(f"{tipo.replace('_', ' ').title()}: {quantidade} kg - Energia: {energia:.2f} kWh - Porcentagem: {porcentagem:.2f}%")
    
    energia_total_label.config(text=f"Energia Total: {energia_total:.2f} kWh")
    energia_lista.delete(1, tk.END)
    for item in energia_individual:
        energia_lista.insert(tk.END, item)

# Função para salvar dados em um arquivo
def salvar_dados():
    with open("dados_biomassa.txt", "w") as file:
        for tipo, quantidade in quantidades.items():
            file.write(f"{tipo},{quantidade}\n")
        messagebox.showinfo("Sucesso", "Dados salvos em 'dados_biomassa.txt'.")

# Função para carregar dados de um arquivo
def carregar_dados():
    try:
        with open("dados_biomassa.txt", "r") as file:
            quantidades.clear()
            total_quantidade.set(0)
            biomassa_lista.delete(0, tk.END)
            energia_lista.delete(0, tk.END)

            for line in file:
                tipo, quantidade = line.strip().split(",")
                quantidade = float(quantidade)
                quantidades[tipo] = quantidade
                total_quantidade.set(total_quantidade.get() + quantidade)
                biomassa_lista.insert(tk.END, f"{tipo.replace('_', ' ').title()}: {quantidade} kg")

            calcular_energia_total()
            messagebox.showinfo("Sucesso", "Dados carregados com sucesso.")

    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo 'dados_biomassa.txt' não encontrado.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao carregar os dados: {e}")

# Função para encerrar
def encerrar():
    root.quit()

# Interface Gráfica com Tkinter
root = tk.Tk()
root.title("Calculadora de Energia Renovável a partir de Biomassa")

# Descrição e instruções para o usuário
descricao_label = tk.Label(
    root,
    text=(
        "Instruções:\n"
        "1. Escolha o tipo de biomassa usando os números abaixo:\n"
        "   1 - Resíduos Agrícolas\n"
        "   2 - Resíduos de Madeira\n"
        "   3 - Resíduos Alimentares\n"
        "   4 - Estrume Animal\n"
        "2. Insira a quantidade de biomassa em quilogramas (kg).\n"
        "3. Clique em 'Adicionar Biomassa' para calcular a energia gerada.\n"
        "4. Clique em 'Salvar Dados' para armazenar os dados inseridos em um arquivo de texto.\n"
        "5. Clique em 'Carregar Dados' para ler e exibir os dados salvos anteriormente.\n"
        "6. A lista 'Biomassa Adicionada' mostra o tipo e a quantidade inserida.\n"
        "7. A lista 'Energia por Tipo de Biomassa' mostra o tipo, a energia gerada (em kWh) e a porcentagem relativa ao total."
    ),
    justify=tk.LEFT,
    padx=10,
    pady=10
)
descricao_label.pack()

# Variáveis
total_quantidade = tk.DoubleVar(value=0)
quantidades = {}

# Layout
descricao_label = tk.Label(root, text="Escolha o tipo de biomassa e insira a quantidade (kg):")
descricao_label.pack(pady=10)

frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)

tipo_var = tk.StringVar()
tipo_combobox = tk.OptionMenu(frame_entrada, tipo_var, "1", "2", "3", "4")
tipo_combobox.grid(row=0, column=1)

quantidade_label = tk.Label(frame_entrada, text="Quantidade (kg):")
quantidade_label.grid(row=1, column=0)

quantidade_entry = tk.Entry(frame_entrada)
quantidade_entry.grid(row=1, column=1)

adicionar_button = tk.Button(root, text="Adicionar Biomassa", command=adicionar_biomassa)
adicionar_button.pack(pady=10)

biomassa_lista = tk.Listbox(root, height=5, width=100)
biomassa_lista.pack()

energia_total_label = tk.Label(root, text="Energia Total: 0 kWh")
energia_total_label.pack()

energia_lista = tk.Listbox(root, height=5, width=100)
energia_lista.pack()

# Botões de salvar e carregar
salvar_button = tk.Button(root, text="Salvar Dados", command=salvar_dados)
salvar_button.pack(pady=5)

carregar_button = tk.Button(root, text="Carregar Dados", command=carregar_dados)
carregar_button.pack(pady=5)

encerrar_button = tk.Button(root, text="Encerrar", command=encerrar)
encerrar_button.pack(pady=10)

root.mainloop()
