import pandas as pd
import numpy as np

def predict(model, X, threshold = 0.3):
    """
    desc:   given an x dataframe, make a prediction using our model
    
    args:
        model (Sklearn.pipeline Pipeline) : Trained model we are going to evaluate
        X (pd.DataFrame): X values passed to model.
        
    returns:
        y (int) : 1 or 0, 1 for True (user is at elevated risk of stroke), 0 false (user is not at elevated risk of stroke)
    """
    
    #get the prediction probabilites
    probability = model.predict_proba(X)[:,-1][0]

    #round the values based on our custom threshold
    stroke = 1 if probability >= threshold else 0.0

    return stroke



def build_df(gender,age,hypertension,heart_disease,diabetes,marital_status,work,env,height,weight,smoking):
    """
    desc:   takes in user input from frontend forms and converts it to our X dataframe
    
    args:
        gender (string) : users gender 
        age (float) : users age 
        hypertension (string) : if user has hypertension 
        heart_disease (string) : if user has heart disease
        diabetes (string) : if user has diabetes
        marital_status (string) : if user has been previously married
        work (string) : where the user works
        env (string) : where the user lives
        height (float) : users height in metres
        weight (float) : users weight in kg
        smoking (string) : users smoking status
    returns:
        X (pd.DataFrame): X values to be passed to model.
    """
    
    #create empty dataframe

    X = pd.DataFrame(columns = ['gender', 'age', 'hypertension', 'heart_disease', 'ever_married',
       'work_type', 'Residence_type', 'avg_glucose_level', 'bmi',
       'smoking_status', 'stroke'])
