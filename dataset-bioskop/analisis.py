import numpy as np
import pandas as pd

#Tampilkan statistik deskriptif data
df = pd.read_csv('dataset_film_bioskop.csv')
print(df.head())

#Statistik deskriptif
print(df.describe())

#Tampikan jumlah data yang kosong & isi dengan nilai median
print(df.isnull().sum())
df['Rating_IMDb'] = df['Rating_IMDb'].fillna(df['Rating_IMDb'].median())
df['Durasi_Menit'] = df['Durasi_Menit'].fillna(df['Durasi_Menit'].median())
df['Pendapatan_Global_Juta_USD'] = df['Pendapatan_Global_Juta_USD'].fillna(df['Pendapatan_Global_Juta_USD'].median())
df['Jumlah_Ulasan_IMDb'] = df['Jumlah_Ulasan_IMDb'].fillna(df['Jumlah_Ulasan_IMDb'].median())

#Genre unik tanpa duplikasi
print(df['Genre'].unique())

#Film yang rilis setelah 1 Januari 2024
df['Tanggal_Rilis'] = pd.to_datetime(df['Tanggal_Rilis'])
hasil = df[df['Tanggal_Rilis'] > '2024-01-01']
print(hasil)

#Tampilkan data film secara acak
print(df.sample(10))

#Statistik rating menggunakan numpy
print("Rating tertinggi: ", np.max(df['Rating_IMDb']))
print("Rating terendah: ", np.min(df['Rating_IMDb']))
print("Rata-rata rating: ", np.mean(df['Rating_IMDb']))
print("Median rating: ", np.median(df['Rating_IMDb']))
