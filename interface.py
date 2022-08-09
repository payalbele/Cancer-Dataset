import json
from flask import Flask, jsonify, render_template, request,redirect, url_for
import config
from project_app.utils import CancerData

app = Flask(__name__)

################################################################################

@app.route('/') 
def hello_flask():
    print("Welcome to Flask")
    # return render_template("home.html")
    return 'Hello Python'

#################################################################################

@app.route('/predict')
def get_Cancer_Deaths_Number():
    
        data = request.form
        new_cases_number= eval(data['new_cases_number'])
        new_cases_rank= eval(data['new_cases_rank'])
        new_case_percent= eval(data['new_case_percent'])
        new_cases_cum_risk= eval(data['new_cases_cum_risk'])
        death_rank= eval(data['death_rank'])
        death_percentage= eval(data['death_percentage'])
        Deaths_cum_risk= eval(data['Deaths_cum_risk'])
        risk_of_prevalence_5yr= eval(data['risk_of_prevalence_5yr'])
        per100k_5yr_prevalence= eval(data['per100k_5yr_prevalence'])
        cancer_type= data['cancer_type']

        print("new_cases_number,new_cases_rank,new_case_percent,new_cases_cum_risk,death_rank,death_percentage,Deaths_cum_risk,risk_of_prevalence_5yr,per100k_5yr_prevalence",new_cases_number,new_cases_rank,new_case_percent,new_cases_cum_risk,death_rank,death_percentage,Deaths_cum_risk,risk_of_prevalence_5yr,per100k_5yr_prevalence,cancer_type)
        can_dat = CancerData(new_cases_number,new_cases_rank,new_case_percent,new_cases_cum_risk,death_rank,death_percentage,Deaths_cum_risk,risk_of_prevalence_5yr,per100k_5yr_prevalence,cancer_type)
        Deaths_Number = can_dat.get_Cancer_Deaths_Number()

        return jsonify({"Result"  : f"Predicted Deaths Number are : {Deaths_Number}"})
    
    
    
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=config.PORT_NUMBER)