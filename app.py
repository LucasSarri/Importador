import tkinter as tk
from tkinter import ttk
from clientes import ClientesGUI
from fornecedores import FornecedoresGUI
from produtos import ProdutosGUI
from PIL import Image, ImageTk

class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Esconde a janela principal inicialmente

        # ----------------- Tela de carregamento (Splash) -----------------
        self.splash = tk.Toplevel()
        self.splash.overrideredirect(True)  # Sem borda de janela
        self.splash.geometry("1920x1080+1920+1080")  # Tamanho e posição da tela de splash

        splash_logo_path = r".\logo de fundo do app.png" #C:\Users\tecdi\Desktop\tecdisa importador
        splash_img_original = Image.open(splash_logo_path)
        splash_img_resized = splash_img_original.resize((1920, 1080), Image.LANCZOS)
        self.splash_img = ImageTk.PhotoImage(splash_img_resized)

        tk.Label(self.splash, image=self.splash_img).pack(expand=True)

        # Após 3 segundos, fecha splash e mostra a tela principal
        self.splash.after(3000, self.show_main)

        self.root.mainloop()

    def show_main(self):
        self.splash.destroy()
        self.root.deiconify()  # Mostra a janela principal
        self.root.title("Tratamento de Planilhas")
        self.root.geometry("1920x1080")

        # ----------------- Ícone do app -----------------
        icone_path = r".\icone do app.png" #C:\Users\tecdi\Desktop\tecdisa importador
        icone_img = Image.open(icone_path)
        icone_photo = ImageTk.PhotoImage(icone_img)
        self.root.iconphoto(False, icone_photo)

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

        # ----------------- Logo no rodapé -----------------
        rodape_logo_path = r".\logo de fundo do app.png" #C:\Users\tecdi\Desktop\tecdisa importador
        rodape_img_original = Image.open(rodape_logo_path)
        rodape_img_resized = rodape_img_original.resize((1920, 1080), Image.LANCZOS)  # menor para rodapé
        self.rodape_img = ImageTk.PhotoImage(rodape_img_resized)

        rodape_label = tk.Label(self.root, image=self.rodape_img, bd=0)
        rodape_label.pack(side="bottom", pady=5)

    def open_clientes(self):
        ClientesGUI(self.root)

    def open_produtos(self):
        ProdutosGUI(self.root)

    def open_fornecedores(self):
        FornecedoresGUI(self.root)

if __name__ == "__main__":
    MainApp()