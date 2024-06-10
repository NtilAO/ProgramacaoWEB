# script_importacao.py
import json
from .models import Banda, Album, Musica

def importar_dados(arquivo_bandas, arquivo_albuns):
    with open(arquivo_bandas, 'r') as f:
        bandas_data = json.load(f)
        for banda_info in bandas_data:
            Banda.objects.create(
                nome=banda_info['nome'],
                nacionalidade=banda_info['nacionalidade'],
                ano_de_criacao=banda_info['ano_de_criacao']
            )

    with open(arquivo_albuns, 'r') as f:
        albuns_data = json.load(f)
        for album_info in albuns_data:
            banda = Banda.objects.get(nome=album_info['banda'])
            album = Album.objects.create(
                tituloAlbum=album_info['titulo'],
                anoDeLancamento=album_info['ano_de_lancamento'],
                banda=banda
            )
            for musica_info in album_info['musicas']:
                Musica.objects.create(
                    tituloMusica=musica_info['titulo'],
                    duracao=musica_info['duracao'],
                    album=album
                )