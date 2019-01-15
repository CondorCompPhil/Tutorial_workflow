---
title:  'Kraken'
author: 
- J.B. Camps
- 
lang: en
documentclass: article
tags: [software, ocr, htr]
abstract: |
  This is the software card for the Kraken OCR software.
---

### Kraken

<!-- Install à copier/coller -->

- Script detection, mixed languages (works fine for print, not yet fully for manuscripts);
- Jinja template, to enrich the OCR output directly, and e.g. export it to TEI;
- output: bounding boxes for word and characters, along with the recognition, so it can be used to link characters to images;
- 


Architecture of the neural network can be redefined through a graph specification language. Better to tweak it a bit for manuscripts:

Layout analysis: currently being replaced with a *trainable x-height labeller* (and reading order determination tool).

It will be trainable, on baseline data. It will also be possible to do transfer learning, by taking an existing layout analysis model, and then retraining on a few pages from a manuscript.

Possible to do segmentation outside, get a json file similar to the one in Kraken, and then use it inside. **External segmentation can be feeded to ketos transcribe through the use of the -l option.**
(see `ketos transcribe --help`).



Options to ketos train:

- `-s` : specifications of the network can be tweaked using -s option, and VGSL.

  For instance, it is useful for using color input. This specific example is treated in the documentation.
  
  > In some cases, such as color inputs, 
  > changing the network architecture might be useful:
  >     $ ketos train -s '[1,0,0,3 Cr3,3,16 Mp3,3 Lfys64 Lbx128 Lbx256 Do]' syr/*.png

- it is possible to resize the codec, when retraining on a previously existing model;

preloading speeds up training considerably, especially in CPU.

To export data from, e.g., Transkribus to use to train a Kraken model, using an alto export might be the simplest way.




