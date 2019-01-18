---
title:  'Tutorial example subsubfile'
author: J.B. Camps
lang: en
documentclass: article
tags: [example, empty]
abstract: |
  This is an exemple of subsubfile.
---

### Tracer

[etrap.eu/tutorials/2019-paris/tracer](etrap.eu/tutorials/2019-paris/tracer)

Or, inscribe and get it there: https://vcs.etrap.eu/users/sign_in

extract, cd, and launch:

```bash
java -Xmx600m -Deu.etrap.medusa.config.ClassConfig=conf/tracer_config.xml -jar tracer.jar
``` 

Look at the results in folder `data/corpora/Bible/TRACER_DATA`


config_tracer.xml,
fichier de configuration qui pourra servir à paramétrer l'appli

l. 13
    <property name="LINKING_IMPL" value="eu.etrap.tracer.linking.IntraCorpusLinkingImpl"/> -> comp. entre textes
    <property name="LINKING_IMPL" value="eu.etrap.tracer.linking.IntraCorpusLinkingImpl"/> -> comp. dans le même texte




    <category name="eu.etrap.tracer.scoring.feature.selected.symmetric.SelectedFeatureResemblanceSimilarityImpl">
        <property name="dblScoringThreshold" value="0.9" />
    </category>

