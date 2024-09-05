# Carregar o modelo
import pickle
MODEL_PATH = 'model.pkl'
with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)

# Fazer a previsão
def predict_credit_score(user_data):
    features = [user_data[field] for field in ['age', 'gender', 'dependents', 'education_level', 'annual_income', 'card_type', 'products_purchased_12m', 'interactions_12m', 'inactive_months_12m', 'credit_limit', 'transaction_value_12m', 'transaction_count_12m']]
    
    score = model.predict([features])[0]
    return score
