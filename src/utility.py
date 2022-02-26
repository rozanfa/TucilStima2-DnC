import math

# Mencari jarak antara garis p1-p2 dengan titik point
def findDistance(p1, p2, point):
    # Gunakan rumus ax + by + c = 0 untuk mengecek jarak titik terhadap garis
    a = p1[1] - p2[1]
    b = p2[0] - p1[0]
    c = p1[0]*p2[1] - p2[0]*p1[1]
    return abs(a*point[0] + b*point[1] + c)/math.sqrt(a*a + b*b)


# Membagi titik-titk yang ada di dataset ds berdasarkan lokasinya terhadap garis p1-p2
def splitDs(p1, p2, ds):
    if p2[0] == p1[0]:
        return [], []

    # Inisiasi dataset titik atas dan bawah
    dsAbove = []
    dsBelow = []

    # Hitung gradien m dan konstanta c agar dapat membentuk persamaan garis y = mx + c
    m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    c = - m * p1[0] + p1[1] 

    # Tentukan posisi setiap titik
    for point in ds:
        # Jika y > mx + c, letakkan di dataset titik atas
        if point[1] > m * point[0] + c:
            dsAbove.append(point)
        # Jika y < mx + c, letakkan di dataset titik bawah
        elif point[1] < m * point[0] + c:
            dsBelow.append(point)
    
    return dsAbove, dsBelow

