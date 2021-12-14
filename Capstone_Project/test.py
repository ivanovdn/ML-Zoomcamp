import requests

host = 'diabet-predict-env.eba-xjdiypmw.us-east-1.elasticbeanstalk.com'
url = f'http://{host}/predict'


data = {"age":40,
 "gender":1,
 "polyuria":0,
 "polydipsia":1,
 "sudden_weight_loss":0,
 "weakness":1,
 "polyphagia":0,
 "genital_thrush":0,
 "visual_blurring":0,
 "itching":1,
 "irritability":0,
 "delayed_healing":1,
 "partial_paresis":0,
 "muscle_stiffness":1,
 "alopecia":1,
 "obesity":1}

print(requests.post(url, json=data).json())