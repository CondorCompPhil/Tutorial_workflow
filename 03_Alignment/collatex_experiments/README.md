---
title:  'Experiments with CollateX'
author:
- J.B. Camps
- L. Ing
- E. Spadini
date: \today
lang: fr
documentclass: article
tags: [collation, alignment, collatex]
abstract: |
  Presentation of CollateX. Use linguistic analysis for refining the output and identifying categories of variants
---


# Experiments with CollateX

## 1. CollateX

### 1.a. Short intro to CollateX 
Slides <https://elespdn.github.io/talks/20190117_condorcet.html>

### 1.b. Demo and hands-on

Try the Demo on CollateX website <https://collatex.net/demo/>

Or (if you have Python3 on your machine) try the Python version, following the instructions here.

**Install and run CollateX (python) in Jupyter notebooks**

- Clone or download the repository <https://github.com/CondorCompPhil/Tutorial_workflow>.
    - To clone: ```git clone URL ```
    - To download: download this Github repository, using the green button 'Clone or download' above. Choose 'Download ZIP'; move the zip file to a safe place in your computer where you can find it later, e.g. the 'Documents' folder; unzip it.

- Install Jupyter notebook (for details, see <https://jupyter.org/install.html>)
```bash
pip3 install --upgrade pip
pip3 install jupyter
```

- (Optional!) Virtualenv
```bash
virtualenv env -p python3.6
source env/bin/activate
```

- install collatex (for details, see <https://pypi.org/project/collatex/>)
```bash
pip3 install collatex python-levenshtein graphviz lxml
```

- launch Jupyter notebook and go to the folder where you downloaded the repo (or navigate to the repo in command line and then launch Juypter notebook). A page will open in your default browser at 'http://localhost:8888'. Now you can navigate the files and open them using double click.

```bash
jupyter notebook
```

- Open the Notebook and run it.
    - Double click on 'example1.ipynb'; it will be opened in a new tab.
    - Select the first code cell (you'll see 'In [1]' on the left) just by clicking into it. Then run the code using the 'Play' button in the bar above (8th button from left). The result will be (re)generated immediately. You can try with all the code cells below (all those having 'In' and a number on the left). The result will appear below each cell code.


## 2. Identifying categories of variants

Slides [Approach and basic categorization of variants](<https://elespdn.github.io/talks/20190117_condorcet.html#/10>)

Slides [Categorization of variants and future perspectives](https://github.com/CondorCompPhil/Tutorial_workflow/blob/master/03_Alignment/collatex_experiments/collation_categorisation_variants.pdf)



