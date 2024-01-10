import pickle
import streamlit as st
from streamlit_option_menu import option_menu
model = pickle.load(open('/content/drive/MyDrive/Web/Erythemato-Squamous-Disease.pkl', 'rb'))

with st.sidebar:

    selected = option_menu('Disease Prediction System',

                          ['Erythemato-Squamous-Disease'],
                          icons=['clipboard2-pulse-fill'],
                          default_index=0)

if (selected == 'Erythemato-Squamous-Disease'):

    # page title
    st.title('Erythemato-Squamous-Disease')

    Erythema = st.text_input('Erythema')
    scaling = st.text_input('scaling')
    definite_borders =st.text_input('definite borders')
    itching = st.text_input('itching')
    koebner_phenomenon = st.text_input('koebner phenomenon')
    polygonal_papules = st.text_input('polygonal papules')
    follicular_papules = st.text_input('follicular papules')
    oral_mucosal_involvement = st.text_input('oral mucosal involvement')
    knee_and_elbow_involvement = st.text_input('knee and elbow involvement')
    scalp_involvement = st.text_input('scalp involvement')
    family_history = st.text_input('family history')
    eosinophils_in_the_infiltrate = st.text_input('eosinophils in the infiltrate')
    PNL_infiltrate = st.text_input('PNL infiltrate')
    fibrosis_of_the_papillary_dermis = st.text_input('fibrosis of the papillary dermis')
    exocytosis = st.text_input('exocytosis')
    acanthosis = st.text_input('acanthosis')
    hyperkeratosis = st.text_input('hyperkeratosis')
    parakeratosis = st.text_input('parakeratosis')
    clubbing_of_the_rete_ridges = st.text_input('clubbing of the rete ridges')
    elongationofthereteridges = st.text_input('elongation of the rete ridges')
    thinningofthesuprapapillaryepidermis = st.text_input('thinning of the suprapapillary epidermis')
    spongiform_pustule = st.text_input('spongiform pustule')
    munro_microabcess = st.text_input('munro microabcess')
    focal_hypergranulosis = st.text_input('focal hypergranulosis')
    disappearanceofthegranularlayer = st.text_input('disappearance of the granular layer')
    spongiosis = st.text_input('spongiosis')
    follicularhornplug = st.text_input('follicular horn plug')
    inflammatorymonoluclearinfiltrate = st.text_input('inflammatory monoluclear infiltrate')
    Agelinear = st.text_input('Age (linear)')

    diagnosis = ''
    if st.button('Test Result'):
      prediction = model.predict([[Erythema,scaling,definite_borders,itching,koebner_phenomenon,polygonal_papules,follicular_papules,oral_mucosal_involvement,knee_and_elbow_involvement,
                             scalp_involvement,family_history,eosinophils_in_the_infiltrate,PNL_infiltrate,fibrosis_of_the_papillary_dermis,exocytosis,acanthosis,
                             hyperkeratosis,parakeratosis,clubbing_of_the_rete_ridges,elongationofthereteridges,thinningofthesuprapapillaryepidermis,spongiform_pustule,munro_microabcess,
                             focal_hypergranulosis,disappearanceofthegranularlayer,spongiosis,follicularhornplug,inflammatorymonoluclearinfiltrate, Agelinear]])

      if (prediction[0] == 1):
        diagnosis = 'psoriasis'
      if (prediction[0] == 2):
        diagnosis = 'seboreic dermatitis'
      if (prediction[0] == 3):
        diagnosis = 'lichen planus'
      if (prediction[0] == 4):
        diagnosis = ' pityriasis rosea '
      if (prediction[0] == 5):
        diagnosis = 'cronic dermatitis '
      else:
        diagnosis = 'pityriasis rubra pilaris'

      st.success(diagnosis)