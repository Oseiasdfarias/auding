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
* ==main.Run()== - Já possui um `método` que reproduz os áudios dos subdiretórios de um diretório raiz.
* 


