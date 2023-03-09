import os
from os.path import isfile
from collections.abc import Iterable
from typing import List
import re


class Caminhos(object):
    """
    Obtem os caminhos absolutos dos arquivos de audio mp3o.

    Args:
        path: Diretório raiz.
        subdirs: Lista de subdiretórios para serem varidos pelo
        código afim de obter os caminhos dos arquivos mp3.
    """

    def __init__(self, path: str, subdirs: Iterable[str]) -> None:
        self.path = path
        self.subdirs = subdirs
        self.__entrar_dir()
        self.verificar = re.compile(r"Comple")
        self.complete_path: List[str] = []

    def get_paths(self) -> List[str]:
        """
        Orquestra os métodos desse módulo para obter todos os arquivos
        mp3 das subpastas.
        Args:

        Returns:
            retorna uma lista contendo todos os caminhos absolutos de
        todos os arquivos mp3 das subpastas.
        """
        self.__entrar_subdir()
        self.__sair_subdir()
        return self.complete_path

    def __entrar_dir(self) -> None:
        """
        Entra um diretório em relação ao diretório atual.
        Args:

        Returns:
        """
        os.chdir(self.path)

    def __entrar_subdir(self) -> None:
        """
        Entra nos subdiretórios a partir da lista de subdiretório.
        Args:

        Returns:
        """
        for subdir in self.subdirs:
            os.chdir(subdir)
            for i in sorted(os.listdir()):
                if not isfile(i) and not self.verificar.search(i):
                    self.list_file_mp3(i)
            self.__sair_subdir()

    @staticmethod
    def __sair_subdir() -> None:
        """
        Volta um diretório em relação ao diretório atual.
        Args:

        Returns:
        """
        os.chdir("..")

    def list_file_mp3(self, subdir: str) -> None:
        """
        Adiciona para cada arquivo mp3 lido, seu caminho absoluto em
        uma lista python.
        Args:

        Returns:
        """
        # Entra no subdiretório da Aula xx
        os.chdir(subdir)

        # lista todas as pastas e arquivos do diretório
        for i in sorted(os.listdir()):
            # filtra apenas os arquivos .mp3 para adicionar
            # a lista de reprodução
            if i[-4:] == ".mp3":
                # obtem o caminho completo do arquivo .mp3
                path_abs = os.getcwd() + "/" + i

                # Adiciona o caminho absoluto obtido a lista de reprodução
                self.complete_path.append(path_abs)
        self.__sair_subdir()


if __name__ == "__main__":
    path = "/home/bits/CursoIngles/Curso_de_Ingles_vm5_2022/01_Fundacao"
    sub_dirs = ["Módulo 02", ]
    caminhos = Caminhos(path=path, subdirs=sub_dirs)
    paths_abs = caminhos.get_paths()
