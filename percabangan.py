import streamlit as st

#Judul Aplikasi
st.title("NILAI MAHASISWA")

#Input dari pengguna
nilai = st.number_input("Masukan Nilai Anda : ", min_value=0, max_value=100)

#Percabangan Nilai
if nilai >= 60:
    st.success("Selamat! Anda dinyatakan LULUS!")
else:
    st.error("Maaf, Anda dinyatakan BELUM LULUS")

#Percabangan dengan chatbox
tampilkan_pesan = st.checkbox("Simpan Permanen")
if tampilkan_pesan:
    st.write("Nilai akan disimpan permanen")
else:
    st.write("Nilai belum disimpan permanen")

#Percabangan dengan button
if st.button("Simpan"):
   st.success("Sudah tersimpan permanen")
else:
    st.info("Belum tersimpan permanen")