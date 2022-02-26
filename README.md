# Convex Hull Finder
# Tugas Kecil 2 - IF221 Strategi Algoritma

## Deskripsi
Program ini berfungsi untuk mencari convex hull, yaitu himpunan convex terkecil (convex polygon) yang mengandung seluruh titik yang menjadi bagiannya. Program ini menggunakan algoritma divide and conquer. Setelah menemukan seluruh convex hull yang dicari, program akan mengeluarkan output gambar seluruh convex hull beserta titik-titik lainnya dengan warna yang acak.

## Requirement Program
Python 3 dengan library numpy, pandas, matplotlib, sklearn, random, dan sys
(Untuk menginstall library, gunakan command `pip install <nama-library>`)

## Cara Menggunakan Program
Terdapat dua file yang dapat digunakan, yaitu file main.py dan main.ipynb

### A. main.ipynb
Buka file main.ipynb di dalam folder src menggunakan VSCode ataupun aplikasi serupa, kemudian jalankan "kotak" pertama dan "kotak" kedua. Dataset yang digunakan bisa diganti pada code di baris kelima "kotak" pertama.

### B. main.py

#### Cara 1 : Menggunakan run.bat (khusus sistem operasi Windows)
Buka file run.bat kemudian berikan masukan yang diminta file

#### Cara 2 : Menggunakan command terminal
Buka terminal di folder src, kemudian ketikkan
```
py main.py <arg1> <arg2> <arg3>
```
Dengan :
- arg1 : integer antara 1 sampai 3 yang menentukan dataset yang akan digunakan
    1 : dataset iris (default)
    2 : dataset wine
    3 : dataset breast cancer
- arg2 : integer yang menyatakan kolom yang akan digunakan sebagai sumbu-x dari grafik
- arg3 : integer yang menyatakan kolom yang akan digunakan sebagai sumbu-y dari grafik

Jika tidak diberikan argumen, maka program akan berjalan dengan dataset default

## Author
Rozan Fadhil Al Hafidz
13520039
