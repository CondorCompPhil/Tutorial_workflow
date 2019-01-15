---
title:  'Transkribus'
author: 
- J.B. Camps
- 
lang: en
documentclass: article
tags: [transkribus, software, htr, ocr]
abstract: |
  This tutorial file is dedicated to the presentation of Transkribus.
---

### Transkribus

Simple use cases:

- digital edition;
- processing large collections (need a more robust model, so, more data, representative of the full collection); going for a CER below 10% is expected;

The success rate is directly dependent on the size of training data (as well as the software).

On data from the Himanis project, training set of 1197 pages (550 381 words), CER of c. 6%.

*Keyword spotting* is also available in Transkribus for all documents that have been recognised, with a confidence rate for results. It can find results even when the recognition is terrible even though it does not operate directly on the image, but, while transcription is just the result with the more confidence, other results with less confidence are stored in the data and can be searched.

The _use of dictionary_: wordlist with frequencies are created from GT data, and can be or not used. It could be possible to import an exterior wordlist. Improvements are currently not very important, especially for historical texts and when CER are already good.

`HTR+`: better neural networks than the previous version.

*Importing data into Transkribus* from already existing projects: for the Transkribus team, importing is not centric, and too difficult to handle given the variety of formats, except for simple text.
Can you import text regions recognised from other software? Yes, you can for instance use dhSegment and import in Transkribus (it has already been done for this specific software).

#### Other tools offered

- Web interface for transcription: [http://transkribus.eu/](http://transkribus.eu/);
- Teaching to transcribe and read historical handwriting, [https://learn.transkribus.eu](https://learn.transkribus.eu);
- Transkribus scanning tent; fast, perhaps 10 images per minute (the app on the phone takes the pictures automatically).


