from pygame import mixer
import pygame
import audioread
import time
from typing import List


class TocarAudios(object):
    """
    Classe que executa os áudios.
    Args:
        paths_abs: lista contendo os caminhos absolutos
                   dos arquivos *.mp3*.
    """
    def __init__(self, paths_abs: List[str]) -> None:
        self.paths_ans = paths_abs
        # Iniciando o mixer
        mixer.init()

    def ouvir_lista(self) -> None:
        """
        Método responsável por reproduzir os áudios.
        Returns:
            None
        """
        atual = 1
        print()
        for i in self.paths_ans:
            print(f"Qt. Áudio: {len(self.paths_ans)} | Qt. Escutado: {atual}")
            atual += 1
            self.tocar(i)
            # infinite loop
            tempo = self.__get_audio_duration(i)
            end_time = time.time() + tempo
            while time.time() <= end_time:
                continue    # futura atualização
                print("Precione 'p' para [Pausar], 'r' para reiniciar.")
                print("Precione 'e' para [Sair].")
                query = input("  ")
                if query == 'p':
                    # Pausing the music
                    mixer.music.pause()
                elif query == 'r':
                    # Resuming the music
                    mixer.music.unpause()
                elif query == 'e':
                    # Stop the mixer
                    mixer.music.stop()
                    break

    def tocar(self, audio: str) -> None:
        """
        Carrega e reproduz o áudio a partir do  caminho absoluto dele.

        Args:
            audio: caminho absoluto do áudio.
        Returns:
            None
        """
        # Carregando audio
        mixer.music.load(audio)
        # Configurando volume
        mixer.music.set_volume(0.7)
        # Tocar áudio
        mixer.music.play()

    @staticmethod
    def __get_audio_duration(audio: str) -> float:
        """
        Obtem a duração de tempo do áudio.
        Args:
            audio: caminho absoluto do áudio.
        Returns:
            Duração do áudio em segundos.
        """
        with audioread.audio_open(audio) as f:
            # total de tempo em segundo do arquivo de audio
            totalsec = f.duration
        return totalsec
