%%writefile app.py
import streamlit as st
import joblib

# load model
model = joblib.load("customer_segmentation.pkl")

st.set_page_config(page_title="Customer Behaviour Analysis", layout="centered")

st.title("🛍️ Customer Behaviour Analysis System")
st.write("K-Means Clustering Based Customer Segmentation")

st.markdown("### Enter Customer Details")

income = st.number_input("Annual Income (k$)", min_value=0.0, max_value=200.0, step=1.0)
score = st.number_input("Spending Score (1-100)", min_value=0.0, max_value=100.0, step=1.0)

if st.button("Predict Customer Type"):

    result = model.predict([[income, score]])
    cluster = int(result[0])

    if cluster == 0:
        msg = "Average Customers (Normal buyers)"
    elif cluster == 1:
        msg = "Rich but Careful Customers"
    elif cluster == 2:
        msg = "Low Income Low Spending Customers"
    elif cluster == 3:
        msg = "Impulsive Buyers"
      else:
        msg = "Premium Customers (Target Audience)"

    st.success(f"Cluster {cluster} : {msg}")

p1 = int(input("Enter Annual Income: "))
p2 = int(input("Enter Spending Score: "))

result = model.predict([[p1, p2]])
print("Customer belongs to cluster:", result[0])

Enter Annual Income: 33
Enter Spending Score: 44
Customer belongs to cluster: 1
