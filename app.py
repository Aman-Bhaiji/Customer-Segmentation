import streamlit as st
from predict import predict_customer
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Customer Segmentation", layout="centered")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
input, textarea {
    border: 2px solid #1f77b4 !important;
    border-radius: 6px !important;
}

input:focus, textarea:focus {
    border: 2px solid #1f77b4 !important;
    box-shadow: 0 0 5px #1f77b4 !important;
}

.big-font {
    font-size: 26px !important;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<p class="big-font">🧠 Customer Segmentation Dashboard</p>', unsafe_allow_html=True)
st.write("Enter customer details to predict their segment")

# ---------------- RESULT PLACEHOLDER ----------------
result_placeholder = st.empty()

# ---------------- FORM ----------------
with st.form("customer_form", clear_on_submit=True):

    st.subheader("Customer Information")

    age = st.text_input("Age", placeholder="Enter age")
    income = st.text_input("Income", placeholder="Enter income")
    recency = st.text_input("Recency", placeholder="Days since last purchase")

    web_purchases = st.text_input("Web Purchases")
    catalog_purchases = st.text_input("Catalog Purchases")
    store_purchases = st.text_input("Store Purchases")

    web_visits = st.text_input("Web Visits per Month")
    tenure = st.text_input("Customer Tenure (Years)")
    children = st.text_input("Total Children")

    spending = st.text_input("Total Spending")

    submit = st.form_submit_button("🔍 Predict Segment")

# ---------------- PREDICTION ----------------
if submit:

    # Show loader immediately
    with st.spinner("🔄 Processing your input..."):

        # ---------------- INPUT VALIDATION ----------------
        try:
            age_val = int(age)
            income_val = float(income)
            recency_val = int(recency)

            web_purchases_val = int(web_purchases)
            catalog_purchases_val = int(catalog_purchases)
            store_purchases_val = int(store_purchases)

            web_visits_val = int(web_visits)
            tenure_val = float(tenure)
            children_val = int(children)

            spending_val = float(spending)

        except:
            st.error("⚠️ Please enter valid numeric values in all fields.")
            st.stop()

        # Simulate processing (increase visibility)
        time.sleep(1.5)

        total_purchases = web_purchases_val + catalog_purchases_val + store_purchases_val

        if total_purchases == 0:
            spending_per_purchase = 0
        else:
            spending_per_purchase = spending_val / total_purchases

        data = {
            "Age": age_val,
            "Income": income_val,
            "Recency": recency_val,
            "Total_Spending": spending_val,
            "Total_Purchases": total_purchases,
            "Spending_per_Purchase": spending_per_purchase,
            "NumWebPurchases": web_purchases_val,
            "NumCatalogPurchases": catalog_purchases_val,
            "NumStorePurchases": store_purchases_val,
            "NumWebVisitsMonth": web_visits_val,
            "Customer_Tenure_Years": tenure_val,
            "Total_Children": children_val
        }

        cluster, segment, confidence = predict_customer(data)

    # ---------------- RESULT DISPLAY ----------------
    result_placeholder.success(f"🎯 Predicted Segment: {segment}")
    result_placeholder.progress(float(confidence))
    result_placeholder.write(f"Confidence: {confidence:.2f}")

    # ---------------- INSIGHTS ----------------
    if segment == "Premium Customers":
        st.info("💎 High-value customer. Target with premium offers and VIP programs.")
    elif segment == "Regular Customers":
        st.info("🛍️ Frequent buyer. Focus on retention and cross-selling.")
    elif segment == "Budget Customers":
        st.info("💸 Price-sensitive customer. Offer discounts and deals.")
    elif segment == "Inactive Customers":
        st.info("⚠️ Low engagement. Use re-targeting and conversion campaigns.")

    st.toast(f"Prediction complete: {segment}")