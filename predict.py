import joblib
import numpy as np

# Load everything
gmm = joblib.load("gmm_model.pkl")
scaler = joblib.load("scaler.pkl")
features = joblib.load("features.pkl")

cluster_names = {
    0: "Budget Customers",
    1: "Premium Customers",
    2: "Inactive Customers",
    3: "Regular Customers"
}

def predict_customer(data_dict):
    import numpy as np
    
    # Convert input to array
    X = np.array([data_dict[f] for f in features]).reshape(1, -1)
    
    # Scale
    X_scaled = scaler.transform(X)
    
    # Predict cluster
    cluster = gmm.predict(X_scaled)[0]
    
    # Get probabilities
    probs = gmm.predict_proba(X_scaled)[0]
    
    # Confidence = highest probability
    confidence = max(probs)
    
    return cluster, cluster_names[cluster], confidence