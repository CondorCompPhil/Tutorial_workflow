---
title:  'Tutorial example subsubfile'
author: J.B. Camps, E. Manjavacas
lang: en
documentclass: article
tags: [example, empty]
abstract: |
  This is an exemple of subsubfile.
---

# README

## This directory contain some pretrained models for PIE

`capitula.model.tar`: Lemmatizer pretrained on a non-open source dataset of medieval latin

`french-Geste.model.tar`: Lemmatizer pretrained on the Geste corpus

`german-ren.model.tar`: Lemmatizer pretrained on a subset of the Referenzkorpus Mittelniederdeutsch/Niederrheinisch: https://www.slm.uni-hamburg.de/ren.html

`spanish-AnCora.model.tar`: Lemmatizer pretrained on the AnCora corpus for Spanish (part of the Universal Dependencies)

`turkish-IMST.model.tar`: Lemmatizer pretrained on the IMST corpus for Turkish (part of the Universal Dependencies)

`fro-poslemmes.tar`: POS-tagger and lemmatizer trained on the Geste corpus

`model_fro_poslemmesmorph.tar`: POS-tagger, lemmatizer and morphological analyzer trained on the Geste corpus

## Example config file for training a lemmatizer

`lemma.config.json` is an example config file for training a lemmatizer to reasonable good accuracy.

## PIE

#### Installation

For more information check the repo at [](https://www.github.com/emanjavacas/pie), but in short:

```bash
virtualenv env -p python3.7
source env/bin/activate
pip3 install -r requirements.txt
```
