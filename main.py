from flask import Flask ,request, jsonify
import pickle
#from xgboost import XGBClassifier


import pandas as pd
import numpy as np

# try to take the data from the pickle file


model1 = pickle.load(open('model11.pkl','rb'))
heart = pd.DataFrame(model1)

# Input array
#new_input = [[0, 0, 28, 3, 1, 5, 5]] #0 ok
#new_input = [[1, 1, 41, 3, 0, 10, 6]] #0 ok
#new_input = [[0, 0, 25, 1, 1, 3, 7]] #0 ok
#new_input = [[1, 0, 32, 3, 1, 7, 8]] #1
#new_input = [[0, 1, 27, 3, 1, 6, 8]] #0 ok
#new_input = [[1, 1, 23, 2, 0, 10, 6]] #1
#new_input = [[1, 1, 33, 4, 1, 8, 3]] #1
#new_input = [[1, 1, 38, 4, 0, 11, 6]] #1
#new_input = [[1, 1, 27, 4, 0, 9, 2]] #1


# Labling the columns
#xgb = pd.DataFrame(new_input, columns=['HighBP', 'HighChol', 'BMI', 'GenHlth', 'Sex', 'Age', 'Income'])
## Prediction on the given input
#new_output = gbm.predict(dxgb)
## Output
##print(new_input, new_output)






app= Flask(__name__)

#model1 = pickle.load(open('model.pkl','rb'))



@app.route('/hr',methods=['POST'])
def heart():
    #aage = request.form.get('age')
    #genhlth=request.form.get('genhlth')
    #bmi = request.form.get('bmi')
    #income = request.form.get('income')
    #highbp = request.form.get('highbp')
    #highchol = request.form.get('highchol')
    #sex = request.form.get('sex')


    #new
    HighBP = request.form.get('HighBP')
    HighChol = request.form.get('HighChol')
    BMI = request.form.get('BMI')
    GenHlth = request.form.get('GenHlth')
    Sex = request.form.get('Sex')
    Age = request.form.get('Age')
    Income = request.form.get('Income')


    input_value= np.array([[HighBP, HighChol, BMI, GenHlth, Sex, Age, Income]])

    # Prediction on the given input
    new_output = heart.predict(input_value)
    # Output
    print(input_value, new_output)
    result = {'possibility of heart Disease':new_output }
    return jsonify(result)






    #result= {'My age':aage ,'genhealth':genhlth}


    #result = {'HighBP':HighBP,'HighChol':HighChol,'BMI':BMI,'GenHlth':GenHlth, 'Sex': Sex,'Age':Age,'Income':Income}

    #return jsonify(result)





if __name__ == '__main__':
    app.run(debug=True)
    #app.run('0.0.0.0')

