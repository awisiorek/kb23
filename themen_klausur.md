# Wichtige Themen:


## 1. shell-Grundlagen 

- Dateiverarbeitung: ls, cd etc.
- Variablen, Quoting, Globbing, Kommandozeilenargumente
- Operatoren und Pipes
- Shell- und Python-Skripte ausführen: chmod, argparse etc.



## 2. Korpusverarbeitung mit der shell 

- Textwerkzeuge: echo, wc, grep, tr, sort, uniq
- Frequenzlisten, Bigramme
- Tools für Textverabreitung: sed (aktiv), awk (passiv)



## 3. Unicode und Zeichenkodierung 

- Kodierungen: ASCII, Latin/ISO-8859, UTF8
- kombinierende Zeichen
- Zählen von Bytes und Zeichen mit wc 
- Encoding in Python: unicodedata,  encode/decode
- *(nicht relevant: UNIX-Tools für Kodierung: uconv/iconv, recode, hexdump, file)*



## 4. Korpusverarbeitung in Python mit NLTK

- Frequenzlisten mit Python
- Frequenzlisten und Bigramme mit NLTK: (Conditional)FreqDist, ngrams, CollocationFinder
- NLTK-Preprocessing-Methoden: word_tokenize, CorpusReader
- NLTK-Resourcen: Stopwortlisten, plain-text vs. tagged Korpora



## 5. Korpusverarbeitung in Python mit pandas und scikit-learn

- pandas: Arbeiten mit Dataframes
- Berechnung von Frequenzlisten mit pandas-Methoden bzw. Counter
- scikit-learn: Train-Test-Split
- scikit-learn: CountVectorizer 



## 6. Korpusannotation mit stanza

- Processors: Tokenization, Lemmatization, POS Tagging, Syntactic Parsing, Named Entity Recognition, Sentiment Analysis
- regelbasierte vs. statistische Annotationsmodelle
- UD-Korpora (Kenntnis CONLL-Format)



## 7. Parsing semistrukturierter Korpusformate

- XML-Syntax: Elemente, Attribute, Entitäten
- Arbeiten mit Namespaces
- XML-Parsing und -Erzeugung mit etree
- Download von Korpusfiles: requests, urllib
- Korpus-Formate: TEI-XML

