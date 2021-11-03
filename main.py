import joblib
from flask import Flask , render_template, request

app = Flask(__name__)

#Load Model

model1 = joblib.load('lr_model.pkl')

#output1 = model1.predict([[6.58,3802,7834,0.6290]])
#print(output1)

@app.route('/')
def page():
    return render_template('base.html')


@app.route('/predict', methods=['POST'])

def predict():
    tax = request.form.get('pt')
    inc = request.form.get('ai')
    hgh = request.form.get('ph')
    pop = request.form.get('pdl')
    output = model1.predict([[float(tax),int(inc),int(hgh),float(pop)]])
    output1 = round(output[0], 3)
    print(output1)

    return render_template('base_1.html', pred_text = f"Estimated Petrol Consumption {output1}")

app.run(debug=True)


