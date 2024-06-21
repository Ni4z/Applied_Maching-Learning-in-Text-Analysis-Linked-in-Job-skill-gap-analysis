# run beforehand in the terminal
# pip install spacy
# pip install streamlit
# pip install https://huggingface.co/Doener48/de_pipeline/resolve/main/de_pipeline-any-py3-none-any.whl

import streamlit as st
import spacy
from spacy import displacy


nlp = spacy.load('de_pipeline')  # todo use our model

filename = 'ds4b.txt'

st.write('Switch to default texts:')
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button('AML4TA'):
        filename = 'aml4ta.txt'
with col2:
    if st.button('DS4B'):
        filename = 'ds4b.txt'
with col3:
    if st.button('DL4CV'):
        filename = 'dl4cv.txt'


st.header("Text to analyze:")

with open(filename, 'r', encoding='utf8') as f:
    jobtxt = f.read()

input_text = st.text_area("", jobtxt)
doc = nlp(input_text)
colors = {'HARD': "#85C1E9", "SOFT": "#ff6961"}
options = {"ents": ['HARD', 'SOFT'], "colors": colors}
ent_html = displacy.render(doc, style="ent", jupyter=False, options=options)

st.header("Annotated input:")
st.markdown(ent_html, unsafe_allow_html=True)


# run this by streamlit run streamlit-main.py
