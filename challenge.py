from spotipy.oauth2 import SpotifyClientCredentials
from cred import CLIENT_ID, CLIENT_SECRET
import spotipy

def buscar_canciones():
    artista = input("Ingrese el nombre del artista: ")

    results = sp.search(q=f'artist:{artista}', type='artist')

    if not results['artists']['items']:
        print(f"No se encontró información para el artista {artista}.")
        return None

    artist_id = results['artists']['items'][0]['id']
    top_tracks = sp.artist_top_tracks(artist_id)

    # Almacenar las canciones populares
    canciones_populares = top_tracks['tracks']

    mostrar_canciones_populares(canciones_populares)

    return canciones_populares

def mostrar_canciones_populares(canciones):
    print("\nLas 10 canciones más populares:")
    for i, cancion in enumerate(canciones):
        print(f"{i + 1}. {cancion['name']} - Popularidad: {cancion['popularity']}")

def crear_lista_reproduccion():
    playlist = []

    while True:
        try:
            seleccion = int(input("Seleccione una canción (1-10) o ingrese 0 para salir: "))
            if seleccion == 0:
                break
            elif 1 <= seleccion <= 10:
                cancion_seleccionada = canciones_populares[seleccion - 1]
                playlist.append(cancion_seleccionada)
                print(f"{cancion_seleccionada['name']} agregada a la lista de reproducción.")
            else:
                print("Por favor, ingrese un número válido (1-10).")
        except ValueError:
            print("Por favor, ingrese un número válido (1-10).")

    return playlist

def mostrar_lista_reproduccion(playlist):
    if not playlist:
        print("\nNo hay canciones en la lista de reproducción.")
    else:
        print("\nLista de reproducción:")
        for i, cancion in enumerate(playlist):
            print(f"{i + 1}. {cancion['name']} - Duración: {cancion['duration_ms']} ms")

        duracion_total = sum([cancion['duration_ms'] for cancion in playlist])
        duracion_total_minutos = duracion_total / 60000
        print(f"\nDuración total de la lista de reproducción: {duracion_total_minutos:.2f} minutos.")

# Configuración de Spotify con las credenciales
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET))

# Búsqueda de canciones y creación de la lista de reproducción
canciones_populares = buscar_canciones()

if canciones_populares:
    lista_reproduccion = crear_lista_reproduccion()
    mostrar_lista_reproduccion(lista_reproduccion)
