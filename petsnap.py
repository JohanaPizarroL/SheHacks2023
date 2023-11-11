import folium
import webbrowser
import tkinter as tk
from tkinter import ttk

def criar_mapa():
    # Criar um objeto de mapa com coordenadas para Austin, Texas
    mapa = folium.Map(location=[30.2500, -97.7500], zoom_start=12)

    # Adicionar marcador no mapa com Popup
    adicionar_marcador_personalizado(mapa)

    # Salvar o mapa como um arquivo HTML
    mapa.save('mapa.html')

def adicionar_marcador_personalizado(mapa):
    # URL da imagem
    imagem_url = 'https://www.amoviralata.com/wp-content/uploads/2021/04/pipi-vira-lata-nota-200-reais.jpg'

    html = f"""
        <h1>Informações de Animais</h1><br>
        <p>
        ID: A986590<br>
        Data: 11/11/23 11:51<br>
        Tipo de Animal: Cachorro<br>
        Cor: Caramelo<br>
        Encontrado na rua: EMERALD FOREST AUSTIN 78745<br>
        <img src='{imagem_url}' alt='Imagem do animal' width='150'>
        </p>
    """
    iframe = folium.IFrame(html=html, width=500, height=300)
    popup = folium.Popup(iframe, max_width=2650)

    folium.Marker([30.2500, -97.7500], popup=popup).add_to(mapa)

def abrir_mapa():
    # Criar um mapa
    criar_mapa()

    # Abrir o mapa no navegador padrão
    webbrowser.open("mapa.html")

def exibir_mapa():
    # Criar uma janela tkinter
    root = tk.Tk()
    root.title("Mapa")

    # Adicionar um botão para abrir o mapa
    button = ttk.Button(root, text="Abrir Mapa", command=abrir_mapa)
    button.pack(padx=10, pady=10)

    # Iniciar o loop de eventos da interface gráfica
    root.mainloop()

if __name__ == "__main__":
    exibir_mapa()
