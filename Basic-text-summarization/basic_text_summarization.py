article_text = "Just what is agility in the context of software engineering work? Ivar Jacobson [Jac02a] provides a useful discussion: Agility  has become today’s buzzword when describing a modern software process. Everyone is agile. An agile team is a nimble team able to appropriately respond to changes. Change is what software development is very much about. Changes in the software being built, changes to the team members, changes because of new technology, changes of all kinds that may have an impact on the product they build or the project that creates the product. Support for changes should be built-in everything we do in software, something we embrace because it is the heart and soul of software. An agile team recognizes that software is developed by individuals working in teams and that the skills of these people, their ability to collaborate is at the core for the success of the project.In Jacobson’s view, the pervasiveness of change is the primary driver for agility. Software engineers must be quick on their feet if they are to accommodate the rapid changes that Jacobson describes.  But agility is more than an effective response to change. It also encompasses the philosophy espoused in the manifesto noted at the beginning of this chapter. It encourages team structures and attitudes that make communication (among team members, between technologists and business people, between software engineers and their managers) more facile. It emphasizes rapid delivery of operational software and deemphasizes the importance of intermediate work products (not always a good thing); it adopts the customer as a part of the development team and works to eliminate the “us and them” attitude that continues to pervade many software projects; it recognizes that planning in an uncertain world has its limits and that a project plan must be ﬂ exible.  Agility can be applied to any software process. However, to accomplish this, it is essential that the process be designed in a way that allows the project team to adapt tasks and to streamline them, conduct planning in a way that understands the ﬂ uidity of an agile development approach, eliminate all but the most essential work products and keep them lean, and emphasize an incremental delivery strategy that gets working software to the customer as rapidly as feasible for the product type and operational environment."

"""# Import Libraries"""

import re
import nltk
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')

"""# Data Processing"""

article_text = article_text.lower()

clean_text = re.sub('[^a-zA-Z]', ' ', article_text)
clean_text = re.sub(r'\s+',' ', clean_text)
article_text

sentence_list = nltk.sent_tokenize(article_text)
sentence_list

stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}
for word in nltk.word_tokenize(clean_text):
  if word not in stopwords:
    if word not in word_frequencies:
      word_frequencies[word] = 1
    else:
      word_frequencies[word] += 1

maximum_frequency = max(word_frequencies.values())

for word in word_frequencies:
  word_frequencies[word] = word_frequencies[word] / maximum_frequency

"""# Calculate sentence scores"""

sentence_scores = {}

for sentence in sentence_list:
  for word in nltk.word_tokenize(sentence):
    if word in word_frequencies and len(sentence.split(' ')) < 30:
      if sentence not in sentence_scores:
        sentence_scores[sentence] = word_frequencies[word]
      else:
        sentence_scores[sentence] += word_frequencies[word]

word_frequencies

sentence_scores

import heapq
summary = heapq.nlargest(5, sentence_scores, key=sentence_scores.get)

print(" ".join(summary))