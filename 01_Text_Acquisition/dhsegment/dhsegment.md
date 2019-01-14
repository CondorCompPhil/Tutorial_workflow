---
title:  'dhSegment'
author: 
lang: en
documentclass: article
tags: [software, ocr, htr]
abstract: |
  
---

### dhSegment

[https://dhsegment.readthedocs.io/en/latest/](https://dhsegment.readthedocs.io/en/latest/)


#### Prerequisites

##### Training

- nvidia GPU server with 6GB RAM au moins, avec CUDA et cuDNN.
- 

##### Using



#### Data

Images / labels pairs, with the same name, and different extension (e.g., `.png` and `.txt`).



#### Demo

##### Installation

Prequisites: python3.6, git, 

```bash
# Creating virtualenv
virtualenv env -p /usr/bin/python3.6
source env/bin/activate
# Installing
pip3 install git+https://github.com/dhlab-epfl/dhSegment

# Missing deps?
pip3 install scikit-image==0.13.1
```

##### Demo

(Demo)[https://dhsegment.readthedocs.io/en/latest/start/demo.html]

```bash
git clone https://github.com/dhlab-epfl/dhSegment.git
cd dhSegment/demo/
wget https://github.com/dhlab-epfl/dhSegment/releases/download/v0.2/pages.zip
unzip pages.zip
cd ..
cd pretrained_models/
python download_resnet_pretrained_model.py
cd ..
# Train a model, or don't, and download an existing model (as follows)
cd demo/
wget https://github.com/dhlab-epfl/dhSegment/releases/download/v0.2/model.zip
unzip model.zip
cd ..
# Modification
python demo.py
```

- modifier `boxes_detection.py`, l. 28
- l. 28, retirer  `_,`  avant `contours`.

