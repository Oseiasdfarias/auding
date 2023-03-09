#!/usr/bin/env /home/bits/CursoIngles/Curso_de_Ingles_vm5_2022/programas_auxiliares/audIG/.venv/bin/python3.10
from paths import Caminhos
from mixer import TocarAudios


def run() -> None:
    # Diretório raiz do curso.
    path = "/home/bits/CursoIngles/Curso_de_Ingles_vm5_2022/01_Fundacao"
    # Subdiretórios a serem listado os áudios
    sub_dirs = ["Módulo 02", ]
    # Instanciando um objeto Caminhos
    caminhos = Caminhos(path=path, subdirs=sub_dirs)
    # obtendo os caminhos absolutos dos arquivos de áudios.
    paths_abs = caminhos.get_paths()

    toca_audios = TocarAudios(paths_abs=paths_abs)
    toca_audios.ouvir_lista()


if __name__ == "__main__":
    run()
