import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

# Configurações de autenticação
SPOTIPY_CLIENT_ID = '540646e29de2448596b8a6f70e662f0e'
SPOTIPY_CLIENT_SECRET = '1e42a0b2fdba4da9b27fbe6bc33cb385'
SPOTIPY_REDIRECT_URI = 'http://localhost:9898/callback'
scope = 'playlist-modify-public'

# Autenticação no Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))

# Leitura do arquivo TXT
with open(r'C:\Users\Administrator\Desktop\Lista de musicas.txt', 'r', encoding='utf-8') as file:
    tracks = [line.strip() for line in file]

# ID da playlist onde as músicas serão adicionadas
playlist_id = '3DtIWeY5uXM9EwwZl3SP4o'

# Lista para armazenar URIs das músicas encontradas
track_uris = []

# Busca das músicas no Spotify
for track in tracks:
    result = sp.search(q=track, type='track', limit=1)
    if result['tracks']['items']:
        track_uri = result['tracks']['items'][0]['uri']
        track_uris.append(track_uri)
    else:
        print(f"Música '{track}' não encontrada no Spotify.")

# Adiciona as músicas à playlist
if track_uris:
    sp.playlist_add_items(playlist_id, track_uris)
    print(f'{len(track_uris)} músicas foram adicionadas à playlist.')
else:
    print('Nenhuma música foi encontrada para ser adicionada.')

