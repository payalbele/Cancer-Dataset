import pickle
import json
import config
import numpy as np

class CancerData():
    def __init__(self,new_cases_number,new_cases_rank,new_case_percent,new_cases_cum_risk,death_rank,death_percentage,Deaths_cum_risk,risk_of_prevalence_5yr,per100k_5yr_prevalence,cancer_type):
        self.new_cases_number = new_cases_number
        self.new_cases_rank = new_cases_rank
        self.new_case_percent =new_case_percent
        self.new_cases_cum_risk = new_cases_cum_risk
        self.death_rank = death_rank
        self.death_percentage=death_percentage
        self.Deaths_cum_risk=Deaths_cum_risk
        self.risk_of_prevalence_5yr=risk_of_prevalence_5yr
        self.per100k_5yr_prevalence=per100k_5yr_prevalence
        self.cancer_type='cancer_type_'+cancer_type

    def load_model(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
        # with open('Linear_Model.pkl','rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
        # with open('project_data.json','r') as f:    
            self.json_data = json.load(f)

    def get_Cancer_Deaths_Number(self):
        self.load_model()
        print("*"*30,self.json_data)
        cancer_type_index = self.json_data['columns'].index(self.cancer_type)

        test_array = np.zeros(len(self.json_data['columns']))
        test_array[0] = self.new_cases_number
        test_array[1] = self.new_cases_rank
        test_array[2] = self.new_case_percent
        test_array[3] = self.new_cases_cum_risk
        test_array[4] = self.death_rank
        test_array[5] = self.death_percentage
        test_array[6] = self.Deaths_cum_risk
        test_array[7] = self.risk_of_prevalence_5yr
        test_array[8] = self.per100k_5yr_prevalence
        test_array[cancer_type_index] = 1
        print("Test Array :",test_array)

        Deaths_Number = np.around(self.model.predict([test_array])[0],2)
        return Deaths_Number

if __name__ == "__main__":
    
    new_cases_number = 5421.00
    new_cases_rank= 26.00
    new_case_percent= 0.42
    new_cases_cum_risk= 0.06
    death_rank= 26.00
    death_percentage= 0.25
    Deaths_cum_risk= 0.04
    risk_of_prevalence_5yr= 10278.00
    per100k_5yr_prevalence= 0.78
    cancer_type= 'Lung'



    can_dat = CancerData(new_cases_number,new_cases_rank,new_case_percent,new_cases_cum_risk,death_rank,death_percentage,Deaths_cum_risk,risk_of_prevalence_5yr,per100k_5yr_prevalence)
    print(can_dat.get_Cancer_Deaths_Number())