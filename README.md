# 🧠 Customer Segmentation Dashboard

This project implements **customer segmentation using Gaussian Mixture Models (GMM)** and provides an **interactive Streamlit dashboard** to predict customer segments in real-time.

---

## 🚀 Features

* 📊 Customer segmentation using **GMM (Gaussian Mixture Model)**
* 🧮 Feature engineering (spending behavior, purchases, tenure, etc.)
* 📈 Model comparison (KMeans, Agglomerative, DBSCAN, GMM)
* 🧠 Final model selection based on performance
* 🌐 Interactive **Streamlit dashboard**
* 🎯 Real-time prediction of customer segment
* 📊 Confidence score for predictions
* 💡 Business insights for each segment

---

## 🧩 Customer Segments

The model identifies 4 key customer segments:

| Segment               | Description                                   |
| --------------------- | --------------------------------------------- |
| 💎 Premium Customers  | High income, high spending, highly responsive |
| 🛍️ Regular Customers | Frequent buyers, consistent revenue           |
| 💸 Budget Customers   | Low spending, price-sensitive                 |
| ⚠️ Inactive Customers | High browsing, low conversion                 |

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib, Seaborn
* Streamlit
* Joblib

---

## 📁 Project Structure

```
Customer-Segmentation/
│
├── app.py                  # Streamlit dashboard
├── predict.py              # Prediction logic
├── gmm_model.pkl           # Trained GMM model
├── scaler.pkl              # Feature scaler
├── features.pkl            # Feature order
├── Data_Mining_Project.ipynb  # Notebook (EDA + modeling)
├── marketing_campaign.csv  # Dataset
├── README.md
└── .gitignore
```

---

## ▶️ Run the App Locally

1. Clone the repository:

```bash
git clone https://github.com/Aman-Bhaiji/Customer-Segmentation.git
cd Customer-Segmentation
```

2. Create environment (recommended):

```bash
conda create -n Data_Mining_Project python=3.10
conda activate Data_Mining_Project
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

*(or manually install: numpy, pandas, scikit-learn, streamlit, joblib, matplotlib, seaborn)*

4. Run the dashboard:

```bash
streamlit run app.py
```

---

## 🧪 Sample Input

Use this to test the app:

**Premium Customer Example:**

* Age: 55
* Income: 100000
* Spending: 1500
* Purchases: High
* Web Visits: Low

---

## 📊 Model Insights

* GMM outperformed KMeans and Agglomerative clustering
* Data shows **overlapping cluster structure**
* DBSCAN was not suitable due to lack of density separation

---

## 📌 Key Learnings

* Importance of feature engineering in clustering
* Model validation using silhouette score
* Real-world data often requires probabilistic clustering (GMM)
* End-to-end ML pipeline: EDA → Modeling → Deployment

---

## 🚀 Future Improvements

* Add explainability ("Why this prediction?")
* Deploy dashboard online (Streamlit Cloud)
* Improve UI/UX
* Add real-time data input API

---

## 👨‍💻 Author

**Aman Bhaiji**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
