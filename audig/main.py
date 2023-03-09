#!/usr/bin/env /home/bits/CursoIngles/Curso_de_Ingles_vm5_2022/programas_auxiliares/audIG/.venv/bin/python3.10
from audig import Caminhos
from audig import TocarAudios
from typing import List


class Run:
    """
    Modelo Matemático do Aeropêndulo para simulação dinâmica
    """

    def __init__(self):
        self.run()

    def run(self, path: str, sub_dirs: List[str]) -> None:
        """
        Método executa o reprodutor de áudio.
        Args:
            path: Caminho absoluto do diretório raiz.
            sub_dirs: subdiretórios do diretório raiz.
        Returns:
            Não retorna nada.
        """

        # Instanciando um objeto Caminhos
        caminhos = Caminhos(path=path, subdirs=sub_dirs)
        # obtendo os caminhos absolutos dos arquivos de áudios.
        paths_abs = caminhos.get_paths()

        toca_audios = TocarAudios(paths_abs=paths_abs)
        toca_audios.ouvir_lista()


if __name__ == "__main__":
    # Diretório raiz do curso.
    path = "/home/bits/CursoIngles/Curso_de_Ingles_vm5_2022/01_Fundacao"
    # Subdiretórios a serem listado os áudios
    sub_dirs = ["Módulo 02", ]
    Run().run(path=path, sub_dirs=sub_dirs)
