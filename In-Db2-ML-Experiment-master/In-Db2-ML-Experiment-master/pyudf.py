import nzae 
from joblib import load
from sklearn import tree
from sklearn import preprocessing

class predict_fraud(nzae.Ae):
    def _setup(self):
        self.model = load('/data2/home/apu/saved_model.joblib')
        #self.scaler = load('/data2/home/apu/saved_scaler.joblib')

    def predict(self,data):
        result = self.model.predict([data])
        return int(result[0])

    # def prepare_data(self,row):
    #    scaled_amount = self.scaler.transform(row[28])
    #    feature_row = row[0:27] + [scaled_amount]
    #    return [feature_row]
    
    def _getFunctionResult(self,row):
       # features = self.prepare_data(row)
        fraud = self.predict(row)
        return fraud

predict_fraud.run()
