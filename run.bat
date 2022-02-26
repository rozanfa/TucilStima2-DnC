@echo off
echo Daftar datasets:
echo 1. Iris
echo 2. Wine
echo 3. Breast Cancer
set /p ds="Pilih dataset yang ingin digunakan (default = 1): "
set /p x="Masukkan kolom untuk sumbu-x (default = 0): "
set /p y="Masukkan kolom untuk sumbu-y (default = 1): "
py src\main.py %ds% %x% %y%