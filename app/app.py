import streamlit as st
from constants import APP_TITLE, APP_SUBTITLE, LABELS
from utils import load_model, predict_argument, analyze_decision

st.set_page_config(
    page_title=APP_TITLE,
    page_icon='🧠',
    layout='centered'
)

model, vectorizer = load_model()

st.title(f'🧠{APP_TITLE}')
st.subheader(APP_SUBTITLE)

st.write(
    'Describe a personal decision and receive a structured analysis of its advantages, disadvantages, risks and key questions.'
)

st.divider()

user_text = st.text_area(
    'Enter your argument here:',
    placeholder='Example: The new job offers a higher salary and better career progression.')

if st.button('Analyze', type="primary"):
    if user_text.strip():
        prediction, probability = predict_argument(
            user_text, model, vectorizer
        )

        stance = LABELS[prediction]

        st.divider()
        st.subheader('NLP Classification')

        st.success(stance)
        st.write(f'Confidence: {probability:.2%}')
        st.progress(float(probability))

        with st.spinner('Analyzing your decision...'):
            analysis = analyze_decision(
                user_text, stance, probability
            )
        st.subheader('Decision Analysis')
        st.markdown(analysis)
    else:
        st.warning('Please enter an argument before clicking Analyze.')

st.divider()
st.caption(
    'DecisionLens AI helps organize information and does not provide professional, medical, legal or financial advice.'
)