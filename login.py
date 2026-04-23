import customtkinter as ctk
from tkinter import messagebox
import menu_principal

USUARIO_VALIDO = "admin"
CONTRASENA_VALIDA = "1234"


def login():
    def verificar():
        usuario = entry_user.get().strip()
        contrasena = entry_pass.get().strip()
        if usuario == USUARIO_VALIDO and contrasena == CONTRASENA_VALIDA:
            root.destroy()
            menu_principal.abrir_menu()
        else:
            lbl_msg.configure(text="Usuario o contraseña incorrectos", text_color="red")

    root = ctk.CTk()
    root.title("Login")
    root.geometry("300x250")
    root.resizable(False, False)

    titulo = ctk.CTkLabel(root, text="inicio de sesion", font=ctk.CTkFont(size=24, weight="bold"))
    titulo.pack(pady=20)

    frame = ctk.CTkFrame(root)
    frame.pack(padx=20, pady=10, fill="both", expand=True)

    lbl_user = ctk.CTkLabel(frame, text="Usuario:")
    lbl_user.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    entry_user = ctk.CTkEntry(frame, width=150)
    entry_user.grid(row=0, column=1, padx=10, pady=10)

    lbl_pass = ctk.CTkLabel(frame, text="Contraseña:")
    lbl_pass.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    entry_pass = ctk.CTkEntry(frame, show="*", width=150)
    entry_pass.grid(row=1, column=1, padx=10, pady=10)

    btn = ctk.CTkButton(root, text="iniciar sesion", command=verificar, width=150)
    btn.pack(pady=15)

    lbl_msg = ctk.CTkLabel(root, text="", font=ctk.CTkFont(size=10))
    lbl_msg.pack(pady=5)

    entry_user.focus()
    root.bind('<Return>', lambda e: verificar())
    root.mainloop()


if __name__ == '__main__':
    login()
