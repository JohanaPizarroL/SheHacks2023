import folium
import webbrowser
import tkinter as tk
from tkinter import ttk

def criar_mapa():
    # Criar um objeto de mapa com coordenadas para Austin, Texas
    mapa = folium.Map(location=[30.2500, -97.7500], zoom_start=12)

    # Adicionar marcador no mapa com Popup
    adicionar_marcador_austin(mapa)

    # Adicionar informações sobre animais encontrados
    animais_encontrados = [
        {
            'location': [30.2600, -97.7400],
            'data': '11/11/23 11:51',
            'tipo_animal': 'Cachorro',
            'cor': 'Amarela',
            'nome_rua': 'Rua 1',
            'imagem': 'cachorro.jpg'  # Coloque o caminho da imagem aqui
        },
        {
            'location': [30.2400, -97.7600],
            'data': '11/11/23 12:30',
            'tipo_animal': 'Gato',
            'cor': 'Branco',
            'nome_rua': 'Rua 2',
            'imagem': 'gato.jpg'  # Coloque o caminho da imagem aqui
        }
    ]

    adicionar_marcadores_animais(mapa, animais_encontrados)

    # Salvar o mapa como um arquivo HTML
    mapa.save('mapa.html')

def adicionar_marcador_austin(mapa):
    # Adicionar marcador no mapa com Popup para Austin
    folium.Marker(
        location=[30.2500, -97.7500],
        popup=folium.Popup("Austin, Texas", parse_html=True),
        icon=folium.Icon(color='blue')
    ).add_to(mapa)

def adicionar_marcadores_animais(mapa, animais):
    # Adicionar marcadores para animais encontrados
    for animal in animais:
        popup_content = (
            f"<b>Data:</b> {animal['data']}<br>"
            f"<b>Tipo de Animal:</b> {animal['tipo_animal']}<br>"
            f"<b>Cor:</b> {animal['cor']}<br>"
            f"<b>Encontrado na rua:</b> {animal['nome_rua']}<br>"
            f"<img src='{animal['imagem']}' alt='Imagem do animal' width='150'>"
        )

        folium.Marker(
            location=animal['location'],
            popup=folium.Popup(popup_content, parse_html=True),
            icon=folium.Icon(color='red')
        ).add_to(mapa)


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
