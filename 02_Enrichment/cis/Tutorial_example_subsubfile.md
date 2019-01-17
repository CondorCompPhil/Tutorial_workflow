---
title:  'Tutorial example subsubfile'
author: 
- Helmut Schmid (speaker)
- J.B. Camps (notes)
- 
lang: en
documentclass: article
tags: [example, empty]
abstract: |
  This is an exemple of subsubfile.
---

### Münich CIS Tools

### POS tagging

#### Theory

Steps:

- tokenisation;
- POS tagging;

Types of POS tagger: most use a statistical model

- hidden markov model (HMM), like TreeTagger;
- conditional random field (CRF), like Marmot;
- recurrent neural networks (RNN), like Pie;

##### HMM

$p(tag|word)$ 
$p(tag_i|tag_i-1,tag_i-2)$

probabilities estimated from freqs

$p(t|w) = \frac{freq(w,t)}{freq(w)}$

Joint probability of a sequence of words and tags, as a product of context and lexical probs

$p(w_1 , …, w_n, t_1, ..., t_n) =  $

The tagger chooses the most probable tag sequence, instead of disambiguating each word.
Unknown words are problematic for HMM.

HMM can only model a few dependency types:

- tag - previous tag
- tag - word

Other are difficult to integrate

- tag - previous word
- tag - whether a comma precedes

Unseen POS tags of know words: prob of 0…

#### Conditional Random Fields

Allow to integrate arbitrary dependencies into the model.

Conditional probability of the tags given the words.
Weights for combinations.
The sum of all combination of words and tags has the value 1.

p(t_1, …, t_n|w_1, …, w_n) = \frac{1}{Z(w_1, …, w_n)} e\sum_i^{n+1}\sum_k=1^M\theta_k f_k (t_i-1,t_i, w_1, …, w_n,i)

In training, what you learn are the values of the weights ($\theta$). Iterative 
training algorithm with *gradient ascent*.

#### RNN

Words mapped to trainable vectors (embeddings), processed by a RNN, with a forward
and backward RNN.

Conditional probability, multiplication of probabilities for context words and context tags.

RNN: current state-of-the-art in POS tagging, and can use any information in the network. In CRF, you have to define a feature function, but in RNN, you leave that to the network.

Word representations can be pretrained on raw text data, to help if labeled training data is small.

#### Common points

All methods need training on manually annotated data ($ 100 000 tokens$)

Typical accuracy, 90-98%.

Special problems of medieval texts: large dialectal and spelling variation,… 
Many unknown word forms, but NN can learn spelling variations.


### Lemmatisation

- table lookup;
- morphological analyzer (finite state transducer), p. ex. LatMor (Münich), that could be used to add vowel length information;
- guessers (Marmot): that learns lemmatization rules from a corpus, and predicts the most probable lemmatisation rule with a classifier;
- NN (encoder-decoder networks, as for machine translation) -> most flexible and accurate method


### Processing of historical texts

Strategy 1: normalize and then use a modern tagger -> doesn't work for medieval texts;
S. 2: normalisation followed by annotation with a tagger trained on normalized data (but automatic normalisation is error prone);
S. 3: train on annotated raw text (large n. of unkn. word forms, but a RNN would be the best choice).

### CIS TOOLS

- TreeTagger;
- Marmot+Lemming;
- PyRNN -> new RNN tagger developed by Helmut Schmid
- LatMor, SMOR (morphological analyzers).


### PyRNN

Can run on GPU with Cuda. Needs PyTorch.

```bash
cmd/rnn-tagger-german.sh test.txt


# Training


```





