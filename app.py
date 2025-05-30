import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st.set_page_config(page_title="Dropout Prediction Dashboard", layout="wide")

st.title("Dropout Prediction Dashboard - Jaya Jaya Institut")

# Load data
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv"
    df = pd.read_csv(url, sep=';')
    df.columns = df.columns.str.strip()  # Strip whitespace
    return df

df = load_data()

# Display data
if st.checkbox("Tampilkan Data"):
    st.write(df.head())

# Preprocessing
df_clean = df.copy()
le = LabelEncoder()
for col in df_clean.select_dtypes(include='object').columns:
    df_clean[col] = le.fit_transform(df_clean[col].astype(str))

# Drop kolom tidak relevan
drop_columns = [
    "GDP", "Inflation_rate", "Unemployment_rate",
    "Mothers_occupation", "Fathers_occupation",
    "Educational_special_needs", "Displaced",
    "Tuition_fees_up_to_date", "Scholarship_holder", "Nacionality"
]
drop_columns_existing = [col for col in drop_columns if col in df_clean.columns]
df_clean = df_clean.drop(columns=drop_columns_existing)

# Train-test split
X = df_clean.drop("Status", axis=1)
y = df_clean["Status"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)

# Sidebar prediction
st.sidebar.header("Prediksi Dropout")
user_input = {}
for col in X.columns:
    if df[col].dtype == 'object':
        user_input[col] = st.sidebar.selectbox(col, df[col].unique())
    else:
        user_input[col] = st.sidebar.number_input(col, float(df[col].min()), float(df[col].max()), float(df[col].mean()))

user_df = pd.DataFrame([user_input])
for col in user_df.select_dtypes(include='object').columns:
    user_df[col] = le.fit_transform(user_df[col].astype(str))
user_df = user_df[X.columns]

# Prediksi
pred = rf.predict(user_df)[0]
pred_label = le.inverse_transform([pred])[0] if hasattr(le, 'inverse_transform') else pred
st.sidebar.markdown(f"### Prediksi: **{pred_label}**")

# Grafik distribusi target
st.subheader("Distribusi Target (Status)")
fig, ax = plt.subplots()
sns.countplot(x="Status", data=df, ax=ax)
st.pyplot(fig)
