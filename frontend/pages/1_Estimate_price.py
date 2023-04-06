import streamlit as st
import pandas as pd
import os
import joblib

model = joblib.load(os.path.abspath("../model/model.obj"))


def load_data():
    data_file = os.path.abspath("../data/preprocessed.csv")
    data = pd.read_csv(data_file, index_col=0)

    return data


data = load_data()
st.write("# Estimate Laptop Price")
features = {
    "Processor": st.selectbox("Select Processor", data.Processor.unique()),
    "RAM": st.selectbox("Select RAM Size", data.RAM.unique()),
    "OS": st.selectbox("Select OS", data.OS.unique()),
    "Storage": st.selectbox("Storage", data.Storage.unique()),
    "OS_arch": st.selectbox("OS Architecure", data.OS_arch.unique()),
    "RAM_Type": st.selectbox("Select RAM Type", data.RAM_Type.unique()),
    "Processor_brand": st.selectbox(
        "Select Brand of Processor", data.Processor_brand.unique()
    ),
}


def predict():
    test = [list(features.values())]
    pred = int(model.predict(test))

    st.success(f"Estimated Price for the chosen configuration: Rs {pred}")


st.button("Estimate", on_click=predict)