# Documentação AudIg

 Link do [PyPi](https://pypi.org/project/audig/).

Usando para reproduzir uma sequência de áudios em inglês.

## Instalação da Biblioteca

### Como Instalar o AudIg?
Para instalar o AudIg você pode usar o pip, conda ou o poetry.

A biblioteca está disponível para ser instalada via o gerenciador de pacotes do python, para instalar basta digitar o comando abaixo em seu terminal.

#### Instalação com o pip

```{.sh}
pip install audig
```

#### Instalação com o conda

```{.sh}
conda install audig
```

#### Instalação com o poetry

```{.sh}
poetry add audig
```

## Classes

* ==Caminhos()== - Obtem todos os caminhos absolutos dos arquivos `.mp3` dos subdiretórios do diretório raiz.
* ==TocarAudios()== - Recebe como parâmetro a lista contendo os caminhos absolutos dos arquivos `.mp3` e reproduz cada arquivo.
* 

## Código Exemplo

```{.py3 hl_lines="" linenums="" title="codigo_exemplo.py"}
from audig import Caminhos
from audig import TocarAudios
from typing import List


def run(path: str, sub_dirs: List[str]) -> None:
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
    path = "home/usuario1/seu_diretorio_raiz"
    # Subdiretórios a serem listado os áudios
    sub_dirs = ["nome_subpasta1", "nome_subpasta2",
                "nome_subpasta3", "nome_subpastax"]
    run(path=path, sub_dirs=sub_dirs)
```
