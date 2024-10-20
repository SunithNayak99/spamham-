import streamlit as st 
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

tidf=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))

st.title("Email/SMS clasiifier by nitte")


input_sms= st.text_area("Enter the message")
if st.button("Predict"):
    

    # preprossing

    ps=PorterStemmer()


    def transfer_text(text): 
        text=text.lower()

        text=nltk.word_tokenize(text)

        y=[]
        for i in text: 
            y.append(ps.stem(i))
        text=y[:]
        y.clear()

        y=[]
        for i in text: 
            if i.isalnum(): 
                y.append(i)
        text=y[:]
        y.clear()

        y=[]
        for i in text: 
            if i not in stopwords.words('english') and i not in string.punctuation: 
                y.append(i)
        text=y[:]
        y.clear()
        return ' '.join(text)

    transfer_sms=transfer_text(input_sms)

    # 2vectorizer
    vector_input=tidf.transform([transfer_sms])
    # 3predict
    result=model.predict(vector_input)[0]
    # 4disply
    if result==1:
        st.header("Spam Message")
    else:
        st.header("Message is not Spam")




