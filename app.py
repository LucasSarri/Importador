import tkinter as tk
from tkinter import ttk
from clientes import ClientesGUI
from fornecedores import FornecedoresGUI
from produtos import ProdutosGUI
from PIL import Image, ImageTk

class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw() 

        # ----------------- Tela de carregamento (Splash) -----------------
        self.splash = tk.Toplevel()
        self.splash.overrideredirect(True)  # Sem borda de janela
        self.splash.geometry("1280x720")  # Tamanho e posição da tela de splash
        self.splash.after(1, self.show_main)

        self.root.mainloop()

    def show_main(self):
        self.splash.destroy()
        self.root.deiconify()  # Mostra a janela principal
        self.root.title("Tratamento de Planilhas")
        self.root.geometry("1280x720")

        # ----------------- UI Principal -----------------
        self._build_ui()

    def _build_ui(self):
        # Frame principal (conteúdo)
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="O que deseja tratar?", font=("Arial", 16)).pack(pady=15)
        ttk.Button(frame, text="Clientes", width=20, command=self.open_clientes).pack(pady=5)
        ttk.Button(frame, text="Produtos", width=20, command=self.open_produtos).pack(pady=5)
        ttk.Button(frame, text="Fornecedores", width=20, command=self.open_fornecedores).pack(pady=5)

    def open_clientes(self):
        ClientesGUI(self.root)

    def open_produtos(self):
        ProdutosGUI(self.root)

    def open_fornecedores(self):
        FornecedoresGUI(self.root)

if __name__ == "__main__":
    MainApp()