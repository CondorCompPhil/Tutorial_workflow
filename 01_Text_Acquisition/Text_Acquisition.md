---
title:  'Text Acquisition'
author:
- J.B. Camps
date: \today
lang: en
documentclass: article
tags: [text acquisition,ocr,htr,post-correction,tutorial]
abstract: |
  This is the main file of the tutorial on text acquisition.
---

# Text Acquisition

## Introduction

### Operations

1. Preprocessing;
2. Layout analysis and line segmentation;
  - Format (baseline / line / text region);
  - Curviline / rectangle shape?
3. Text recognition;
4. Training;
5. Applying model to texts;
6. Post-correction.

### Import / export 

### User interactions

### Specificities of medieval languages

_Out of vocabulary words_ are always present in a given new text, which has an impact on many processing steps, be it OCR post-correction, lemmatisation, etc.

### Reading the image / infering from the image

OCR/HTR is supposed to _read_ from the image, but, sometimes, we want the model to read what is not on the image, i.e.

- abbreviation expansion;
- normalised forms;
- etc.




## Pour la suite: ce que vous ne trouverez pas dans ce chapitre (mais dans les suivants) 

- lemmatisation / canonicalisation / normalisation
- 

## Conceiving your workflow

- Test the different tools.

## The softwares

Detailed information can be found in the **relevant subsections**:

- [dhSegment](./dhsegment/dhsegment.md);
- [Transkribus](./transkribus/transkribus.md);







