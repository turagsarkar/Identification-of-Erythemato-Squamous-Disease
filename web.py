import numpy as np 
from flask import Flask, render_template, request
import sklearn
import pickle
app = Flask(__name__,template_folder='templates')
# load the model
model= pickle.load(open('Erythemato-Squamous-Disease.pkl', 'rb'))
#model = joblib.load('Erythemato-Squamous-Disease.sav')

@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    Erythema = int(request.form['Erythema'])
    scaling = int(request.form['scaling'])
    definite_borders =int(request.form['definite borders'])
    itching = int(request.form['itching'])
    koebner_phenomenon = int(request.form['koebner phenomenon'])
    polygonal_papules = int(request.form['polygonal papules'])
    follicular_papules = int(request.form['follicular papules'])
    oral_mucosal_involvement = int(request.form['oral mucosal involvement'])
    knee_and_elbow_involvement = int(request.form['knee and elbow involvement'])
    scalp_involvement = int(request.form['scalp involvement'])
    family_history = int(request.form['family history'])
    eosinophils_in_the_infiltrate = int(request.form['eosinophils in the infiltrate'])
    PNL_infiltrate = int(request.form['PNL infiltrate'])
    fibrosis_of_the_papillary_dermis = int(request.form['fibrosis of the papillary dermis'])
    exocytosis = int(request.form['exocytosis'])
    acanthosis = int(request.form['acanthosis'])
    hyperkeratosis = int(request.form['hyperkeratosis'])
    parakeratosis = int(request.form['parakeratosis'])
    clubbing_of_the_rete_ridges = int(request.form['clubbing of the rete ridges'])
    elongationofthereteridges = int(request.form['elongation of the rete ridges'])
    thinningofthesuprapapillaryepidermis = int(request.form['thinning of the suprapapillary epidermis'])
    spongiform_pustule = int(request.form['spongiform pustule'])
    munro_microabcess = int(request.form['munro microabcess'])
    focal_hypergranulosis = int(request.form['focal hypergranulosis'])
    disappearanceofthegranularlayer = int(request.form['disappearance of the granular layer'])
    spongiosis = int(request.form['spongiosis'])
    follicularhornplug = int(request.form['follicular horn plug'])
    inflammatorymonoluclearinfiltrate = int(request.form['inflammatory monoluclear infiltrate'])
    Agelinear = int(request.form['Age (linear)'])

    result = model.predict([[Erythema,scaling,definite_borders,itching,koebner_phenomenon,polygonal_papules,follicular_papules,oral_mucosal_involvement,knee_and_elbow_involvement,
                             scalp_involvement,family_history,eosinophils_in_the_infiltrate,PNL_infiltrate,fibrosis_of_the_papillary_dermis,exocytosis,acanthosis,
                             hyperkeratosis,parakeratosis,clubbing_of_the_rete_ridges,elongationofthereteridges,thinningofthesuprapapillaryepidermis,spongiform_pustule,munro_microabcess,
                             focal_hypergranulosis,disappearanceofthegranularlayer,spongiosis,follicularhornplug,inflammatorymonoluclearinfiltrate, Agelinear]])[0]
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)