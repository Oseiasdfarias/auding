# AudIng Reprodutor de Áudio


<br>

## Estrutura do Projeto

```
.
├── audig
│   ├── __init__.py
│   ├── main.py
│   ├── mixer.py
│   ├── paths.py
│   └── __pycache__
│       ├── mixer.cpython-310.pyc
│       └── paths.cpython-310.pyc
├── dist
│   ├── audig-0.1.0-py3-none-any.whl
│   └── audig-0.1.0.tar.gz
├── poetry.lock
├── pyproject.toml
├── README.md
├── tests
│   └── __init__.py
└── utils
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
pygame 2.2.0 Python Game Developmen

```

---

<br>

## Demostração Código
![demo](./utils/demo.png)
