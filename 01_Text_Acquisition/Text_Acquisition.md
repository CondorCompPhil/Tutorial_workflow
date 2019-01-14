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


## Title 2

### Title 3

A paragraph with *italic*.

Another one with **bold**.

And some ~~cancelled text~~.

And one with a link: [Wikipedia](http://www.wikipedia.org)

Or a link to a file on this repository: [more specific doc](./Tutorial_example_folder/Tutorial_example_subfile.md)

A list:

- some thing;
- an other thing.

An enumeration:

1. the first thing;
2. the second one

A more complex list

1. First thing
  - hello;
  - world

    This is just saying hello.
    
2. Second thing:
  - how do you do?
  - where is the coffee?
  
    This is typical conference morning behaviour.

3. Third thing:
  - this list is long enough.
  - don't you think?
    1. probably
    

Some code:

```xml
<hello>World</hello>
```

```python
import condorcet
for i in workshop.days():
    tutorial.write()

```

Some inline code: `print("Hello world")`

An image:

![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Nicolas_de_Condorcet.PNG/800px-Nicolas_de_Condorcet.PNG "Not the official Condorcet logo")

A table
com/CondorCompPhil/Tutorial_workflow
N  | Time | Coffee
---|------|-------
1  | 10h  | 2
10 | 12h  | 8
1  |  9h  | 3

The same, in an easier to write, harder to read, fashion:

N|Time|Coffee
---|---|---
1|10h|2
10|12h|8
1|9h|3

A quotation:

> Rollant a dit: gloton desmesurez! Mar fustes vos nez !
> et neant plus bel ne lui volt dire.


A line

---

Some html

<del>Goodbye world</del>


** /!\ D O N O T F O R G E T T O C O M M I T Y O U R C H A N G E S /!\ **


