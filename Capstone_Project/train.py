import pandas as pd
import pickle
import warnings
warnings.filterwarnings('ignore')
from sklearn.ensemble import GradientBoostingClassifier


df = pd.read_csv('diabets_data.csv')

X = df.drop('class', 1).values
y = df['class'].values

# Train on full data
gbc = GradientBoostingClassifier(random_state=17, n_estimators=100, max_depth=4)
gbc.fit(X, y)

model_name = 'capstone_model.pkl'
with open(model_name, 'wb') as f:
    pickle.dump(gbc, f)