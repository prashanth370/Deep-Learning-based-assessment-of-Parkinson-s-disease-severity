from flask import *
import os
from werkzeug.utils import secure_filename
import label_image

def load_image(image):
    text = label_image.main(image)
    return text

app = Flask(__name__)

@app.route('/')
@app.route('/first')
def first():
    return render_template('first.html')

 
  
    
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/chart')
def chart():
    return render_template('chart.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        file_path = secure_filename(f.filename)
        f.save(file_path)
        # Make prediction
        result = load_image(file_path)
        result = result.title()
        d = {"brownspot":" → You are Normal. Keep Calm and Make Healthy Life",
	'Normal':" → You are Normal. Keep Calm and Make Healthy Life",
        "Severe":" → Neurodegenerative diseases are incurable and debilitating conditions that result in progressive degeneration and / or death of nerve cells. This causes problems with movement (called ataxias), mental functioning (called dementias) and affect a person's ability to move, speak and breathe[1]. Neurodegenerative disorders impact many families - these disorders are not easy for the individual nor their loved ones.",
        "Stage1":" → The most common neurodegenerative disorders are amyloidoses, tauopathies, α-synucleinopathies, and TDP-43 proteinopathies. The protein abnormalities in these disorders have abnormal conformational properties.",
        "Stage2":" → Neurodegenerative diseases are often presented as a distinct entity, however there is often overlap as you may have noted in the above descriptions, eg for AD and Lewy body pathologies. None of the neurodegenerative disorders have perfect diagnostic accuracy, and neuropathology will continue to be the gold standard for the foreseeable future."}
        result = result+d[result]
        #result2 = result+d[result]
        #result = [result]
        #result3 = d[result]        
        print(result)
        #print(result3)
        os.remove(file_path)
        return result
        #return result3
    return None

if __name__ == '__main__':
    app.run()