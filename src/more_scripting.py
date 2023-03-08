#load packages
import spacy #import large spacy model
#initialize spaCy
nlp = spacy.load("en_core_web_md")

def main():
    text = "This is a string"
    doc = nlp(text)
    for token in doc:
        print(token.text)

if __name__=="__main__":
    main()