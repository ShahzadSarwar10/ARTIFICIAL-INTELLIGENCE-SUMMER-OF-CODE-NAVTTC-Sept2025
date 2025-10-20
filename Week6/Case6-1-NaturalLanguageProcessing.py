
#Open the text file :
text_file = open("Week6/Natural_Language_Processing_Text.txt")

#Read the data :
text = text_file.read()

#Datatype of the data read :
print (type(text))
print("\n")

#Print the text :
print(text)
print("\n")
#Length of the text :
print (len(text))

#Import required libraries :
import nltk
from nltk import sent_tokenize
from nltk import word_tokenize


# reriews: https://www.nltk.org/api/nltk.downloader.html

nltk.download('punkt') 
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker_tab')

#Tokenization: Splitting text into words or sentences.

# Review :  https://www.nltk.org/api/nltk.tokenize.sent_tokenize.html

#Tokenize the text by sentences :
sentences = sent_tokenize(text)

#How many sentences are there? :
print (len(sentences))

#Print the sentences :
#print(sentences)
print(sentences)

#Review: https://www.nltk.org/api/nltk.tokenize.word_tokenize.html

#Tokenize the text with words :
words = word_tokenize(text)

#How many words are there? :
print (len(words))
print("\n")

#Print words :
print (words)

#Import required libraries :
from nltk.probability import FreqDist

#Review: https://www.nltk.org/api/nltk.probability.FreqDist.html 

#Find the frequency :
fdist = FreqDist(words)

#Print 10 most common words :
fdist.most_common(10)

#Plot the graph for fdist :
import matplotlib.pyplot as plt

fdist.plot(10)

#Empty list to store words:
words_no_punc = []

#Removing punctuation marks :
for w in words:
    if w.isalpha():
        words_no_punc.append(w.lower())

#Print the words without punctution marks :
print (words_no_punc)

print ("\n")

#Length :
print (len(words_no_punc))

#Frequency distribution :
fdist = FreqDist(words_no_punc)

fdist.most_common(10)


#Plot the most common words on grpah:

fdist.plot(10)

from nltk.corpus import stopwords

#Stop Words Removal: Removing common words (e.g., "the", "is").
#stopwords are commonly defined as uninformative words that do not add significant meaning to a sentence, such as "and," "the," and "is."
#List of stopwords
stopwords = stopwords.words("english")
print(stopwords)

#Empty list to store clean words :
clean_words = []

for w in words_no_punc:
    if w not in stopwords:
        clean_words.append(w)
        
print(clean_words)
print("\n")
print(len(clean_words))

#Frequency distribution :
fdist = FreqDist(clean_words)

fdist.most_common(10)


#Plot the most common words on grpah:

fdist.plot(10)

#Library to form wordcloud :
from wordcloud import WordCloud

#Library to plot the wordcloud :
import matplotlib.pyplot as plt

#Generating the wordcloud :
wordcloud = WordCloud().generate(text)

#Plot the wordcloud :
plt.figure(figsize = (12, 12)) 
plt.imshow(wordcloud) 

#To remove the axis value :
plt.axis("off") 
plt.show()

#Import required libraries :
import numpy as np
from PIL import Image
from wordcloud import WordCloud

#Here we are going to use a circle image as mask :
char_mask = np.array(Image.open("Week6/circle.png"))

#Generating wordcloud :
wordcloud = WordCloud(background_color="black",mask=char_mask).generate(text)

#Plot the wordcloud :
plt.figure(figsize = (8,8))
plt.imshow(wordcloud)

#To remove the axis value :
plt.axis("off")
plt.show()

#Simplifying words to their most basic form is called stemming, and it is made easier by stemmers or stemming algorithms. For example,
# “chocolates” becomes “chocolate” and “retrieval” becomes “retrieve.” This is crucial for pipelines for natural language processing,
#  which use tokenized words that are acquired from the first stage of dissecting a document into its constituent words.
#  In contrast to stemming, lemmatization is a lot more powerful. It looks beyond word reduction and considers a language’s full vocabulary 
#  to apply a morphological analysis to words, aiming to remove inflectional endings only and to return the base or dictionary form of a word,
#   which is known as the lemma.

# https://www.geeksforgeeks.org/lemmatization-vs-stemming-a-deep-dive-into-nlps-text-normalization-techniques/
# https://www.geeksforgeeks.org/introduction-to-stemming/
# https://www.geeksforgeeks.org/python-lemmatization-approaches-with-examples/

#Stemming Example :

#Import stemming library :
from nltk.stem import PorterStemmer

porter = PorterStemmer()

#Word-list for stemming :
word_list = ["Study","Studying","Studies","Studied"]

for w in word_list:
    print(porter.stem(w))
    
#Stemming Example :

#Import stemming library :
from nltk.stem import SnowballStemmer

snowball = SnowballStemmer("english")

#Word-list for stemming :
word_list = ["Study","Studying","Studies","Studied"]

for w in word_list:
    print(snowball.stem(w))
    
#Stemming Example :

#Import stemming library :
from nltk.stem import SnowballStemmer

#Print languages supported :
print(SnowballStemmer.languages)

from nltk import WordNetLemmatizer

lemma = WordNetLemmatizer()
word_list = ["Study","Studying","Studies","Studied"]

for w in word_list:
    print(lemma.lemmatize(w ,pos="v"))

from nltk import WordNetLemmatizer

lemma = WordNetLemmatizer()
word_list = ["am","is","are","was","were"]

for w in word_list:
    print(lemma.lemmatize(w ,pos="v"))
    
from nltk.stem import PorterStemmer
 
stemmer = PorterStemmer()
 
print(stemmer.stem('studies'))

from nltk.stem import WordNetLemmatizer
 
lemmatizer = WordNetLemmatizer()
 
print(lemmatizer.lemmatize('studies'))


from nltk.stem import WordNetLemmatizer
 
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('studying', pos="v"))
print(lemmatizer.lemmatize('studying', pos="n"))
print(lemmatizer.lemmatize('studying', pos="a"))
print(lemmatizer.lemmatize('studying', pos="r"))

from nltk import WordNetLemmatizer

lemma = WordNetLemmatizer()
word_list = ["studies","leaves","decreases","plays"]

for w in word_list:
    print(lemma.lemmatize(w))

"""
What is POS(Parts-Of-Speech) Tagging?
Parts of Speech tagging is a linguistic activity in Natural Language Processing (NLP) wherein each word in a document is given a particular part of speech (adverb,
 adjective, verb, etc.) or grammatical category. Through the addition of a layer of syntactic and semantic information to the words, this procedure makes it easier 
 to comprehend the sentence’s structure and meaning.

 https://www.nltk.org/api/nltk.tag.pos_tag.html

 See:
 https://stackoverflow.com/questions/15388831/what-are-all-possible-pos-tags-of-nltk

"""
#PoS tagging :
tag = nltk.pos_tag(["Studying","Study"])
print (tag)

#PoS tagging example :

sentence = "A very elegant young lady is walking on the street"

#Tokenizing words :
tokenized_words = word_tokenize(sentence)

for words in tokenized_words:
    tagged_words = nltk.pos_tag(tokenized_words)
    
print( tagged_words)


""""What is Chunking?
Chunking involves grouping together individual pieces of information from a sentence, such as nouns, verbs, adjectives, and adverbs, into larger units known as chunks.
 The most common type of chunking is noun phrase (NP) chunking, which involves identifying and extracting noun phrases from a sentence, such as "the cat," "a book,"
   or "my friend." Another type of chunking is verb phrase (VP) chunking, which involves identifying and extracting verb phrases from a sentence, such as 
   "ate breakfast," "is running," or "will sing."

What is Chinking?
Chinking, on the other hand, is the process of excluding certain words or phrases from a chunk. This is useful when we want to exclude specific types of words, 
such as prepositions, conjunctions, or determiners, from the chunks we extract. Chinking is typically used in combination with chunking, and it involves identifying 
the words or phrases that we want to exclude from a chunk and marking them with the tag O (outside) in a named entity recognition (NER) system.

See: https://stackoverflow.com/questions/15388831/what-are-all-possible-pos-tags-of-nltk

See: https://www.nltk.org/api/nltk.chunk.RegexpParser.html?highlight=chunkscore


nltk.chunk.RegexpParser
class nltk.chunk.RegexpParser[source]
Bases: ChunkParserI

A grammar based chunk parser. chunk.RegexpParser uses a set of regular expression patterns to specify the behavior of the parser. The chunking of the text is encoded using a ChunkString, and each rule acts by modifying the chunking in the ChunkString. The rules are all implemented using regular expression matching and substitution.

A grammar contains one or more clauses in the following form:

NP:
  {<DT|JJ>}          # chunk determiners and adjectives
  }<[\.VI].*>+{      # strip any tag beginning with V, I, or .
  <.*>}{<DT>         # split a chunk at a determiner
  <DT|JJ>{}<NN.*>    # merge chunk ending with det/adj
                     # with one starting with a noun
The patterns of a clause are executed in order. An earlier pattern may introduce a chunk boundary that prevents a later pattern from executing. Sometimes an individual pattern will match on multiple, overlapping extents of the input. As with regular expression substitution more generally, the chunker will identify the first match possible, then continue looking for matches after this one has ended.

"""

#Extracting Noun Phrase from text :

# ? - optional character
# * - 0 or more repetations
grammar = "NP : {<DT>?<JJ>*<NN>} "
import matplotlib.pyplot as plt
#Creating a parser :
parser = nltk.RegexpParser(grammar)

#Parsing text :
output = parser.parse(tagged_words)
print (output)

#To visualize :
#output.draw()


#Chinking example :
# * - 0 or more repetations
# + - 1 or more repetations

#Here we are taking the whole string and then
#excluding adjectives from that chunk.

grammar = r""" NP: {<.*>+} 
               }<JJ>+{"""

#Creating parser :
parser = nltk.RegexpParser(grammar)

#parsing string :
output = parser.parse(tagged_words)
print(output)

#To visualize :
#output.draw()

""""Named Entity Recognition (NER) in NLP focuses on identifying and categorizing important information known as entities in text. These entities can be names of people,
 places, organizations, dates, etc. It helps in transforming unstructured text into structured information which helps in tasks like text summarization, knowledge graph
   creation and question answering.

Understanding Named Entity Recognition
NER helps in detecting specific information and sort it into predefined categories. It plays an important role in enhancing other NLP tasks like part-of-speech tagging
 and parsing. Examples of Common Entity Types:

Person Names: Albert Einstein
Organizations: GeeksforGeeks
Locations: Paris
Dates and Times: 5th May 2025
Quantities and Percentages: 50%, $100

See: https://www.nltk.org/api/nltk.chunk.ne_chunk.html

"""

#Sentence for NER :
sentence = "Mr. Smith made a deal on a beach of Switzerland near WHO."

#Tokenizing words :
tokenized_words = word_tokenize(sentence)

#PoS tagging :
for w in tokenized_words:
    tagged_words = nltk.pos_tag(tokenized_words)

#print (tagged_words)

#Named Entity Recognition :
N_E_R = nltk.ne_chunk(tagged_words,binary=False)
print(N_E_R)

#To visualize :
#N_E_R.draw()


#Sentence for NER :
sentence = "Mr. Smith made a deal on a beach of Switzerland near WHO."

#Tokenizing words :
tokenized_words = word_tokenize(sentence)

#PoS tagging :
for w in tokenized_words:
    tagged_words = nltk.pos_tag(tokenized_words)

#print (tagged_words)

#Named Entity Recognition :
N_E_R = nltk.ne_chunk(tagged_words,binary=True)

print(N_E_R)

#To visualize :
#N_E_R.draw()


"""
https://wordnet.princeton.edu/

What is WordNet?
Any opinions, findings, and conclusions or recommendations expressed in this material are those of the creators of WordNet and do not necessarily reflect the views 
of any funding agency or Princeton University.

When writing a paper or producing a software application, tool, or interface based on WordNet, it is necessary to properly cite the source. Citation figures are 
critical to WordNet funding.

About WordNet
WordNet® is a large lexical database of English. Nouns, verbs, adjectives and adverbs are grouped into sets of cognitive synonyms (synsets), each expressing a distinct
 concept. Synsets are interlinked by means of conceptual-semantic and lexical relations. The resulting network of meaningfully related words and concepts can be 
 navigated with the browser(Link is external). WordNet is also freely and publicly available for download. WordNet's structure makes it a useful tool for computational 
 linguistics and natural language processing.

WordNet superficially resembles a thesaurus, in that it groups words together based on their meanings. However, there are some important distinctions.
 First, WordNet interlinks not just word forms—strings of letters—but specific senses of words. As a result, words that are found in close proximity to one another 
 in the network are semantically disambiguated. Second, WordNet labels the semantic relations among words, whereas the groupings of words in a thesaurus does not follow 
 any explicit pattern other than meaning similarity."""

""""WordNet is the lexical database i.e. dictionary for the English language, specifically designed for natural language processing. 

Synset is a special kind of a simple interface that is present in NLTK to look up words in WordNet. Synset instances are the groupings of synonymous words that express the same concept. Some of the words have only one Synset and some have several. 
"""
#Import wordnet :
from nltk.corpus import wordnet

for words in wordnet.synsets("Fun"): 
    print(words)      
    
#Word meaning with definitions :
for words in wordnet.synsets("Fun"): 
    print(words.name())
    print(words.definition())
    print(words.examples())
    
    for lemma in words.lemmas(): 
        print(lemma)
    print("\n")
    
    
#How many differnt meanings :
for words in wordnet.synsets("Fun"): 
    for lemma in words.lemmas(): 
        print(lemma)
    print("\n")
    
    
word = wordnet.synsets("Play")[0]

#Checking name :
print(word.name())

#Checking definition :
print(word.definition())

#Checking examples:
print(word.examples())

word = wordnet.synsets("Play")[0]

#Find more abstract term :
print(word.hypernyms())

word = wordnet.synsets("Play")[0]

#Find more specific term :
word.hyponyms()

word = wordnet.synsets("Play")[0]

#Get only name :
print(word.lemmas()[0].name())

"""
a word or phrase that means exactly or nearly the same as another word or phrase in the same language, for example shut is a synonym of close.
"“shut” is a synonym of “close”"
"""
#Finding synonyms :

#Empty list to store synonyms :
synonyms = []

for words in wordnet.synsets('Fun'):
    for lemma in words.lemmas():
        synonyms.append(lemma.name())
        
print(synonyms)

"""noun
plural noun: antonyms
a word opposite in meaning to another (e.g. bad and good ).
"the antonym of ‘inclusion’ is ‘exclusion’ 
"""

#Finding antonyms :

#Empty list to store antonyms :
antonyms = []

for words in wordnet.synsets('Natural'):
    for lemma in words.lemmas():
        if lemma.antonyms():
            antonyms.append(lemma.antonyms()[0].name())
            
#Print antonyms :            
print(antonyms)


#Finding synonyms and antonyms :

#Empty lists to store synonyms/antonynms : 
synonyms = []
antonyms = []

for words in wordnet.synsets('New'):
    for lemma in words.lemmas():
        synonyms.append(lemma.name())
        if lemma.antonyms():
            antonyms.append(lemma.antonyms()[0].name())
            
#Print lists :
print(synonyms)
print("\n")
print(antonyms)


#https://www.geeksforgeeks.org/nlp-wupalmer-wordnet-similarity/
"""How does Wu & Palmer Similarity work? 
It calculates relatedness by considering the depths of the two synsets in the WordNet taxonomies, along with the depth of the LCS (Least Common Subsumer). 
"""
#Similarity in words :
word1 = wordnet.synsets("ship","n")[0]

word2 = wordnet.synsets("boat","n")[0] 

#Check similarity :
print(word1.wup_similarity(word2)) 

#Similarity in words :
word1 = wordnet.synsets("ship","n")[0]

word2 = wordnet.synsets("bike","n")[0] 

#Check similarity :
print(word1.wup_similarity(word2)) 


"""
https://medium.com/@eskandar.sahel/exploring-feature-extraction-techniques-for-natural-language-processing-46052ee6514

In natural language processing (NLP), feature extraction is a fundamental task that involves converting raw text data into a format that can be easily processed by machine learning algorithms. There are various techniques available for feature extraction in NLP, each with its own strengths and weaknesses. As a data scientist, it’s important to have a good understanding of the different feature extraction techniques available and their appropriate use cases.

In this article, I will explore several common techniques for feature extraction in NLP, including CountVectorizer, TF-IDF, word embeddings, bag of words, bag of n-grams, HashingVectorizer, Latent Dirichlet Allocation (LDA), Non-negative Matrix Factorization (NMF), Principal Component Analysis (PCA), t-SNE, and Part-of-Speach (POS) tagging.
"""

"""
https://www.geeksforgeeks.org/bag-of-words-bow-model-in-nlp/

Bag of words (BoW) model in NLP
In this article, we are going to discuss a Natural Language Processing technique of text modeling known as Bag of Words model. Whenever we apply any algorithm in NLP, it works on numbers. We cannot directly feed our text into that algorithm. Hence, Bag of Words model is used to preprocess the text by converting it into a bag of words, which keeps a count of the total occurrences of most frequently used words.

This model can be visualized using a table, which contains the count of words corresponding to the word itself.
"""

"""
https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html

CountVectorizer
class sklearn.feature_extraction.text.CountVectorizer(*, input='content', encoding='utf-8', decode_error='strict', strip_accents=None, lowercase=True, preprocessor=None, tokenizer=None, stop_words=None, token_pattern='(?u)\\b\\w\\w+\\b', ngram_range=(1, 1), analyzer='word', max_df=1.0, min_df=1, max_features=None, vocabulary=None, binary=False, dtype=<class 'numpy.int64'>)[source]
Convert a collection of text documents to a matrix of token counts.

This implementation produces a sparse representation of the counts using scipy.sparse.csr_matrix.

If you do not provide an a-priori dictionary and you do not use an analyzer that does some kind of feature selection then the number of features will be equal to the vocabulary size found by analyzing the data.

For an efficiency comparison of the different feature extractors, see FeatureHasher and DictVectorizer Comparison.

"""

#Import required libraries :
from sklearn.feature_extraction.text import CountVectorizer

#Text for analysis :
sentences = ["Jim and Pam travelled by the bus:",
             "The train was late",
             "The flight was full.Travelling by flight is expensive"]

#Create an object :
cv = CountVectorizer()

#Generating output for Bag of Words :
B_O_W = cv.fit_transform(sentences).toarray()

#Total words with their index in model :
print(cv.vocabulary_)
print("\n")

#Features :
print(cv.get_feature_names_out())
print("\n")

#Show the output :
print(B_O_W)


#https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html
"""
TfidfVectorizer
class sklearn.feature_extraction.text.TfidfVectorizer(*, input='content', encoding='utf-8', decode_error='strict', strip_accents=None, lowercase=True, preprocessor=None, tokenizer=None, analyzer='word', stop_words=None, token_pattern='(?u)\\b\\w\\w+\\b', ngram_range=(1, 1), max_df=1.0, min_df=1, max_features=None, vocabulary=None, binary=False, dtype=<class 'numpy.float64'>, norm='l2', use_idf=True, smooth_idf=True, sublinear_tf=False)[source]
Convert a collection of raw documents to a matrix of TF-IDF features.

Equivalent to CountVectorizer followed by TfidfTransformer.

For an example of usage, see Classification of text documents using sparse features.

For an efficiency comparison of the different feature extractors, see FeatureHasher and DictVectorizer Comparison.

For an example of document clustering and comparison with HashingVectorizer, see Clustering text documents using k-means.
"""
#Import required libraries :
from sklearn.feature_extraction.text import TfidfVectorizer

#Sentences for analysis :
sentences = ['This is the first document','This document is the second document']

#Create an object :
vectorizer = TfidfVectorizer(norm = None)

#Generating output for TF_IDF :
X = vectorizer.fit_transform(sentences).toarray()

#Total words with their index in model :
print(vectorizer.vocabulary_)
print("\n")

#Features :
print(vectorizer.get_feature_names_out())
print("\n")

#Show the output :
print(X)
