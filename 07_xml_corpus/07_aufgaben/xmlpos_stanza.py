import sys
import xml.etree.ElementTree as ET 
import stanza


def append_text(text, str):
    if not str or str == "":
        return text 
    
    str = str.strip()
    if text == "":
        return str 
    if text[-1] == '¬':
        return text[:-1] + str 
    return text + " " + str 


def gather_text(node, text):
    text = append_text(text, node.text)
    for c in  node:
        text = gather_text(c, text)
    return append_text(text, node.tail)
    

root = ET.fromstring(sys.stdin.read())    
out = ET.Element('doc')
nlp = stanza.Pipeline(lang='de', processors='tokenize, pos', download_method=None) #stanza-Pipeline
sid = 1 
tid = 1

ns = {'tei': 'http://www.tei-c.org/ns/1.0'}
text = gather_text(root.find('tei:text', ns), "")

doc = nlp(text)  #POS-Annotation mit stanza
sents = doc.sentences  #Tokenisierung: hier mit stanza statt NLTK.sent_tokenize
for sent in sents: 
    stag = ET.SubElement(out, 's')
    stag.attrib = {'id': f"s-{sid}"}
    sid += 1

    tokens = sent.tokens #stanza-Methode .tokens (statt .words, wegen MWT)
    for token in tokens:
        ttag = ET.SubElement(stag, 'w')
        ttag.text = token.text
        word_upos = "+".join([word.upos for word in token.words]) #join der durch MWT von stanza getrennt analysierten word-POS-tags
        ttag.attrib = {'pos': word_upos, 'id': f"w-{tid}"}  #stanza
        tid += 1

ET.dump(out)
