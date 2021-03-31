#AeroReader
### Setup install environment
Setting up AeroReader is simple because we have included a requirements.txt file.
If you do not have Conda, first install [MiniConda](https://docs.conda.io/en/latest/miniconda.html).
```bash
cd AeroReader # This should be your install location

conda create --name AeroReader python=3.8
source activate AeroReader

pip install nltk, scipy, PyMuPDF, sklearn, PyQt5
```

### Run AeroReader
Running AeroReader is very simple!
```bash
source activate AeroReader

# book.pdf is any file to analyze
# Depth is an optional argument specifying cluster tree height

python Tree.py book.pdf --depth=3
```
