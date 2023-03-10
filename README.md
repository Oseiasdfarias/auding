# AudIng Reprodutor de Áudio


<br>

## Estrutura do Projeto

```
.
├── audig
│   ├── __init__.py
│   ├── main.py
│   ├── mixer.py
│   └── paths.py
├── poetry.lock
├── pyproject.toml
├── README.md
├── tests
│   └── __init__.py
└── utils
    └── demo.png

```

---

<br>

## Dependências

```
❯ poetry show --tree
```

```

audioread 3.0.0 multi-library, cross-platform audio decoding
autopep8 2.0.2 A tool that automatically formats Python code to conform to the PEP 8 style guide
├── pycodestyle >=2.10.0
└── tomli *
flake8 6.0.0 the modular source code checker: pep8 pyflakes and co
├── mccabe >=0.7.0,<0.8.0
├── pycodestyle >=2.10.0,<2.11.0
└── pyflakes >=3.0.0,<3.1.0
mypy 1.1.1 Optional static typing for Python
├── mypy-extensions >=1.0.0
├── tomli >=1.1.0
└── typing-extensions >=3.10
pygame 2.2.0 Python Game Development

```


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

---

<br>

## Demostração Código

![demo](https://github.com/Oseiasdfarias/auding/blob/main/utils/demo.png?raw=true)
