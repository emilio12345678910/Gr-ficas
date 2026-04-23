import pandas as pd
import customtkinter as ctk
import matplotlib.pyplot as plt

df_calificaciones = pd.read_csv("calificaciones.csv")
df_inmuebles = pd.read_csv("Sacramentorealestatetransactions.csv")

df_calificaciones["calificacion"] = (
    df_calificaciones["calificacion"].astype(str).str.replace(",", ".", regex=False).astype(float)
)

df_inmuebles["price"] = pd.to_numeric(df_inmuebles["price"], errors="coerce").fillna(0)


def abrir_menu():
    ventana = ctk.CTk()
    ventana.title("Menu Principal")
    ventana.geometry("600x500")

    frame_botones = ctk.CTkFrame(ventana)
    frame_botones.pack(fill="both", expand=True, padx=10, pady=10)

    etiqueta_titulo = ctk.CTkLabel(ventana, text="Consultas con interfaz gráfica", font=ctk.CTkFont(size=24, weight="bold"))
    etiqueta_titulo.pack(pady=10)

    etiqueta_instruccion = ctk.CTkLabel(
        ventana,
        text="Presiona un botón para ver la gráfica correspondiente.",
        font=ctk.CTkFont(size=14),
    )
    etiqueta_instruccion.pack(pady=10)

    def consulta_1():
        print("\nConsulta 1: Top 10 ciudades por cantidad")
        conteo = df_inmuebles["city"].value_counts().head(10)
        print(conteo)
        plt.figure()
        conteo.plot(kind="bar")
        plt.title("Top 10 ciudades con más propiedades")
        plt.xlabel("Ciudad")
        plt.ylabel("Cantidad")
        plt.show()


    def consulta_2():
        print("\nConsulta 2: Top 10 ciudades con más propiedades caras (>200k)")
        conteo = df_inmuebles[df_inmuebles["price"] > 200000]["city"].value_counts().head(10)
        print(conteo)
        plt.figure()
        conteo.plot(kind="bar")
        plt.title("Top 10 ciudades con más propiedades caras (>200k)")
        plt.xlabel("Ciudad")
        plt.ylabel("Cantidad")
        plt.show()


    def consulta_3():
        print("\nConsulta 3: Conteo por rango de precio")
        rangos = [0, 100000, 200000, 300000, 400000, 500000, float('inf')]
        etiquetas = ['0-100k', '100k-200k', '200k-300k', '300k-400k', '400k-500k', '500k+']
        df_inmuebles['rango_precio'] = pd.cut(df_inmuebles['price'], bins=rangos, labels=etiquetas, right=False)
        conteo = df_inmuebles['rango_precio'].value_counts().sort_index()
        print(conteo)
        plt.figure()
        conteo.plot(kind="bar")
        plt.title("Número de propiedades por rango de precio")
        plt.xlabel("Rango de precio")
        plt.ylabel("Número de propiedades")
        plt.show()


    def consulta_4():
        print("\nConsulta 4: Top 10 codigos postales por precio medio")
        promedio = df_inmuebles.groupby("zip")["price"].mean().sort_values(ascending=False).head(10)
        print(promedio)
        plt.figure()
        promedio.plot(kind="bar")
        plt.title("Top 10 codigos postales por precio medio")
        plt.xlabel("ZIP")
        plt.ylabel("Precio medio")
        plt.show()


    def consulta_5():
        print("\nConsulta 5: Tipos de propiedad")
        conteo = df_inmuebles["type"].value_counts()
        print(conteo)
        plt.figure()
        conteo.plot(kind="bar")
        plt.title("Tipos de propiedad")
        plt.show()


    def consulta_6():
        print("\nConsulta 6: Precio medio por baños")
        promedio = df_inmuebles.groupby("baths")["price"].mean()
        print(promedio)
        plt.figure()
        promedio.plot(kind="bar")
        plt.title("Precio medio por baños")
        plt.xlabel("Baños")
        plt.ylabel("Precio medio")
        plt.show()


    def consulta_7():
        print("\nConsulta 7: Top 10 más caras")
        top = df_inmuebles.nlargest(10, "price")[["street", "price"]]
        print(top)
        plt.figure()
        plt.bar(top["street"], top["price"])
        plt.title("Top 10 propiedades más caras")
        plt.ylabel("Precio")
        plt.xticks(rotation=45)
        plt.show()


    def consulta_8():
        print("\nConsulta 8: Top 10 más baratas")
        top = df_inmuebles.nsmallest(10, "price")[["street", "price"]]
        print(top)
        plt.figure()
        plt.bar(top["street"], top["price"])
        plt.title("Top 10 propiedades más baratas")
        plt.ylabel("Precio")
        plt.xticks(rotation=45)
        plt.show()


    def consulta_9():
        print("\nConsulta 9: Conteo por rango de calificación")
        rangos = [0, 5, 7, 9, 10.1]
        etiquetas = ['0-5', '5-7', '7-9', '9-10']
        df_calificaciones['rango_cal'] = pd.cut(df_calificaciones['calificacion'], bins=rangos, labels=etiquetas, right=False)
        conteo = df_calificaciones['rango_cal'].value_counts().sort_index()
        print(conteo)
        plt.figure()
        conteo.plot(kind="bar")
        plt.title("Número de estudiantes por rango de calificación")
        plt.xlabel("Rango")
        plt.ylabel("Número")
        plt.show()


    def consulta_10():
        print("\nConsulta 10: Número de estudiantes por inicial")
        df_calificaciones["inicial"] = df_calificaciones["Nombre"].str[0].str.upper()
        conteo = df_calificaciones.groupby("inicial")["Nombre"].count().sort_values(ascending=False).head(10)
        print(conteo)
        plt.figure()
        conteo.plot(kind="bar")
        plt.title("Número de estudiantes por inicial del nombre")
        plt.xlabel("Inicial")
        plt.ylabel("Número")
        plt.show()

    botones = [
        ("Top 10 ciudades por cantidad", consulta_1),
        ("Top 10 ciudades con más propiedades caras", consulta_2),
        ("Rango de precio", consulta_3),
        ("Top 10 codigos postales por precio medio", consulta_4),
        ("Tipos de propiedad", consulta_5),
        ("Precio medio por baños", consulta_6),
        ("Top 10 más caras", consulta_7),
        ("Top 10 más baratas", consulta_8),
        ("Rango de calificación", consulta_9),
        ("Número por inicial", consulta_10),
    ]

    for texto, funcion in botones:
        boton = ctk.CTkButton(frame_botones, text=texto, width=220, command=funcion)
        boton.pack(pady=8)

    ventana.mainloop()


if __name__ == '__main__':
    abrir_menu()
