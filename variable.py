import streamlit as st
from datetime import date

#Judul aplikasi
st.title("Biodata")

#Input string
nama = st.text_input("Masukan Nama Anda :")

#Pilihan dalam string
jenis_kelamin = st.selectbox(
    "Pilih jenis Kelamin Anda :",
    ("Laki-laki","Perempuan")
)

#Input string yang lebih panjang
alamat = st.text_area("Masukan Alamat Anda :", height=100)

#Input integer
umur = st.number_input("Masukan Umur Anda :", min_value=0, max_value=100, value=25)

#Input tanggal
tanggal_lahir = st.date_input("Pilih Tanggal Lahir Anda :", date(2000, 1, 1))

#Tombol untuk menampilkan hasil
if st.button("Tampilkan Data"):
    st.subheader("Data yang Dimasukkan :")
    st.write("Nama :",nama)
    st.write("Jenis Kelamin :",jenis_kelamin)
    st.write("Alamat :",alamat)
    st.write(f"Umur :{umur} tahun")
    st.write("Tanggal Lahir :", tanggal_lahir.strftime('%d-%m-%Y'))