# AeroReader
### Setup install environment
Setting up AeroReader is simple!
If you do not have Conda, first install [MiniConda](https://docs.conda.io/en/latest/miniconda.html).
```bash
cd AeroReader # This should be your install location

conda create --name AeroReader python=3.8
source activate AeroReader

pip install nltk, scipy, PyMuPDF, sklearn, PyQt5, PyDictionary, tensorflow, keras-bert
```  
Setting up the BERT Neural Network for supervised searching.  
Download the BERT config folder from: https://drive.google.com/drive/folders/1m6zB_0eNYH0F_br6pj3OGIPDk4wpgaop?usp=sharing  
Place the folder within the `/CS_SS_AeroReader_v1.0/bert/` directory  

### Run AeroReader
Running AeroReader is very simple!
```bash
source activate AeroReader

# book.pdf is any file to analyze
# Depth is an optional argument specifying cluster tree height

python Tree.py book.pdf --depth=3
```
