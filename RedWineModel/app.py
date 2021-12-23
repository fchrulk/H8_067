import flask
import numpy as np
import pickle
import random

model = pickle.load(open('model/model_random_forest_gini.pkl', 'rb'))

app = flask.Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return(flask.render_template('home.html'))

@app.route('/predict',methods=['POST'])
def get_wine_quality():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in flask.request.form.values()]
    final_features = [np.array(int_features)]

    prediction = model.predict(final_features)

    output = {0: 'Bad', 1: 'Good'}

    if prediction[0] == 0:
        score = random.randrange(0, 6)
    else:
        score = random.randrange(6, 10)

    txt = output[prediction[0]]
    full_text = 'The wine quality is {}'.format(txt)
    score_text = 'Wine Score = {}/10'.format(score)

    return flask.render_template('predicted.html', 
                                 result_output=full_text,
                                 score_text=score_text)

@app.route('/wine_stats')
def wine_stats():
    return(flask.render_template('Wine Statistics.html'))

if __name__ == '__main__':
    app.run(debug=True)