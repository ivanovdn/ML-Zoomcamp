Problem - Predict the risk of diabetes using 16 tabular features.
Dataset was taken from kaggle: https://www.kaggle.com/andrewmvd/early-diabetes-classification.
This dataset contains 520 observations with 16 characteristics.

On cross-validation was choosen GradientBoostingClassifier (in notebook).

In train.py model trains on all data and serializes in capstone_model.pkl file.
Then you can build docker to test it with test.py with url = '0.0.0.0:9696/predict' 
or use test.py which request POST on AWS Elastic Beantalk 
(link: http://diabet-predict-env.eba-xjdiypmw.us-east-1.elasticbeanstalk.com/predict).