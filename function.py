import streamlit as st

#Fungsi penjumlahan
def tambah(a, b):
    return a + b

#Fungsi pengurangan
def kurang(a, b):
    return a - b

st.title ("PROGRAM PERHITUNGAN")

x = st.number_input("Masukan Angka Pertama :")
y = st.number_input("Masukan Angka Kedua :")
col1, col2 = st.columns(2)

with col1:
    if st.button("Penjumlahan"):
        hasil = tambah (x, y)
        st.success(f"{x}+{y} = {hasil}")

with col2:
    if st.button("Pengurangan"):
        hasil = kurang (x, y)
        st.success(f"{x}-{y} = {hasil}")