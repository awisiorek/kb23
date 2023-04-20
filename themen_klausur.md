# Wichtige Themen:


## 1. shell-Grundlagen 

- Dateiverarbeitung: ls, cd etc.
- Variablen, Quoting, Globbing, Kommandozeilenargumente
- Operatoren und Pipes
- Shell- und Python-Skripte ausführen: chmod, argparse etc.



## 2. Korpusverarbeitung mit der shell 

- Textwerkzeuge: echo, wc, grep, tr, sort, uniq, sed, awk
- Frequenzlisten



## 3. Unicode und Zeichenkodierung 

- Kodierungen: ASCII, Latin/ISO-8859, UTF8
- UNIX-Kodierungstools: uconv/iconv, recode, hexdump, file
- Encoding in Python: encode/decode, unicodedata, chardet
- kombinierende Zeichen



## 4. Korpusverarbeitung in Python mit NLTK

- Frequenzlisten nativ
- NLTK-Preprocessing-Methoden: word_tokenize, CorpusReader
- NLTK-Resourcen: Plain-Text-Korpora, Tagged-Korpora, Treebanks, Wordlisten
- NLTK-Korpus-Statistik: Frequenzlisten mit (Conditional)FreqDist, Kollokationen/ngrams



## 5. Korpusverarbeitung in Python mit pandas und scikit-learn

- pandas: Arbeiten mit Dataframes
- Berechnung von Frequenzlisten mit pandas-Methoden bzw. Counter
- scikit-learn: Train-Test-Split
- scikit-learn: CountVectorizer, TfidfVectorizer



## 6. Korpusannotation mit stanza

- Processors: Tokenization, Lemmatization, POS Tagging, Syntactic Parsing, Named Entity Recognition, Sentiment Analysis
- regelbasierte vs. statistische Annotationsmodelle
- UD-Korpora



## 7. Parsing semistrukturierter Korpusformate

- JSON-Parser, XML-Parser
- XML-Syntax: Elemente, Attribute, Entitäten
- Namespaces
- Download von Korpusfiles: requests, urllib
- Korpus-Formate: TEI-XML, TCF-XML


## 8. Erzeugung eigener Tagger

- Mapping verschiedener Tagsets
- Training und Serialisierung/Speicherung eigener Tagger mit NLTK-Elternklasse
- Verknüpfung von Taggern über Backoff-Tagger
