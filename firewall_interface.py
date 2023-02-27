
import uvicorn
from pydantic import BaseModel
import numpy as np
import pickle
from fastapi import FastAPI
#app object
app = FastAPI()

from pydantic import BaseModel

class data_breache(BaseModel):
    Source_Port :float
    Destination_Port:float
    NAT_Source_Port:float
    Bytes:float
    Bytes_Sent:float
    Bytes_Received:float
    Packets:float
    Elapsed_Time:float
    pkts_sent:float
    pkts_received:float

pickle1_in = open("firewall_model.pkl","rb")
classifier = pickle.load(pickle1_in)

pickle2_in = open("firewall_model_isolation.pkl","rb")
iso_classifier = pickle.load(pickle2_in)

@app.get('/')
def index():
    return {'message':'Hello, world'}

@app.get('/{name}')
def index1(name:str):
    return {'message':f'Hello, world {name}'}



@app.post('/predict')
def predict_breach(data:data_breache):
    #print('heloo')
    data = data.dict()
    #print("hello")
    Source_Port=data['Source_Port']
    Destination_Port=data['Destination_Port']
    NAT_Source_Port=data['NAT_Source_Port']
    Bytes=data['Bytes']
    Bytes_Sent=data['Bytes_Sent']
    Bytes_Received=data['Bytes_Received']
    Packets=data['Packets']
    Elapsed_Time=data['Elapsed_Time']
    pkts_sent=data['pkts_sent']
    pkts_received=data['pkts_received']
    prediction = classifier.predict([[Source_Port,Destination_Port,NAT_Source_Port,Bytes,Bytes_Sent,Bytes_Received,Packets,Elapsed_Time,pkts_sent,pkts_received]])
    if (prediction[0]==0):
        prediction = "alow"
    elif (prediction[0]==1):
        prediction = "drop"
    elif (prediction[0]==2):
        prediction = "deny"
    else:
        prediction = "reset-both"
    
    return {
        'prediction':prediction
        }

@app.post('/predict_dtree')
def predict_breach(data:data_breache):
    #print('heloo')
    data = data.dict()
    #print("hello")
    Source_Port=data['Source_Port']
    Destination_Port=data['Destination_Port']
    NAT_Source_Port=data['NAT_Source_Port']
    Bytes=data['Bytes']
    Bytes_Sent=data['Bytes_Sent']
    Bytes_Received=data['Bytes_Received']
    Packets=data['Packets']
    Elapsed_Time=data['Elapsed_Time']
    pkts_sent=data['pkts_sent']
    pkts_received=data['pkts_received']
    prediction = classifier.predict([[Source_Port,Destination_Port,NAT_Source_Port,Bytes,Bytes_Sent,Bytes_Received,Packets,Elapsed_Time,pkts_sent,pkts_received]])
    if (prediction[0]==0):
        prediction = "alow"
    elif (prediction[0]==1):
        prediction = "drop"
    elif (prediction[0]==2):
        prediction = "deny"
    else:
        prediction = "reset-both"
    
    return {
        'prediction':prediction
        }

@app.post('/predict_iso')
def predict_breach(data:data_breache):
    #print('heloo')
    data = data.dict()
    #print("hello")
    Source_Port=data['Source_Port']
    Destination_Port=data['Destination_Port']
    NAT_Source_Port=data['NAT_Source_Port']
    Bytes=data['Bytes']
    Bytes_Sent=data['Bytes_Sent']
    Bytes_Received=data['Bytes_Received']
    Packets=data['Packets']
    Elapsed_Time=data['Elapsed_Time']
    pkts_sent=data['pkts_sent']
    pkts_received=data['pkts_received']
    prediction = iso_classifier.predict([[Source_Port,Destination_Port,NAT_Source_Port,Bytes,Bytes_Sent,Bytes_Received,Packets,Elapsed_Time,pkts_sent,pkts_received]])
    if (prediction[0]==0):
        prediction = "alow"
    elif (prediction[0]==1):
        prediction = "drop"
    elif (prediction[0]==2):
        prediction = "deny"
    else:
        prediction = "reset-both"
    
    return {
        'prediction':prediction
        }



