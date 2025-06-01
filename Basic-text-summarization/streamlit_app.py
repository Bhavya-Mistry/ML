import streamlit as st
import nltk
import re
import heapq

# Download required resources
nltk.download('punkt')
nltk.download('stopwords')

# Summarization function
def summarize_text(article_text):
    article_text = article_text.lower()
    clean_text = re.sub(r'[^a-zA-Z]', ' ', article_text)
    clean_text = re.sub(r'\s+', ' ', clean_text)

    sentence_list = nltk.sent_tokenize(article_text)
    stopwords = nltk.corpus.stopwords.words('english')

    word_frequencies = {}
    for word in nltk.word_tokenize(clean_text):
        if word not in stopwords:
            word_frequencies[word] = word_frequencies.get(word, 0) + 1

    max_freq = max(word_frequencies.values())
    word_frequencies = {word: freq / max_freq for word, freq in word_frequencies.items()}

    sentence_scores = {}
    for sentence in sentence_list:
        if len(sentence.split()) < 30:
            for word in nltk.word_tokenize(sentence.lower()):
                if word in word_frequencies:
                    sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_frequencies[word]

    summary_sentences = heapq.nlargest(5, sentence_scores, key=sentence_scores.get)
    return " ".join(summary_sentences)

# Streamlit UI
st.title("📝 Basic Text Summarizer")
st.write("Paste any paragraph below to get a summary.")

text_input = st.text_area("Enter text to summarize", height=300)

if st.button("Summarize"):
    if text_input.strip() == "":
        st.warning("Please enter some text to summarize.")
    else:
        summary = summarize_text(text_input)
        st.subheader("📌 Summary:")
        st.write(summary)
        st.success("Summary generated successfully!")