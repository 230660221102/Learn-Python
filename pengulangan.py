import streamlit as st

st.title ("Daftar Mahasiswa")

mahasiswa = ["Asep", "Wawan", "Dadang", "Doni Wirtawan"]
st.subheader ("#FOR")
no = 1
for item in mahasiswa:
    st.write(f"{no}.{item}")
    no += 1

st.subheader("#WHILE")
no = 1
i = 0
while i <len (mahasiswa):
    st.write(f"{no}. {mahasiswa[i]}")
    no += 1
    i += 1


