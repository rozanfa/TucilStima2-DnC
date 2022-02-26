import numpy as np
from utility import findDistance, splitDs


class MyConvexHull:
    def __init__(self, ds):
         # Ubah numpy list menjadi python list
        self.ds = ds.tolist()

        # Inisialisasi hasil
        self.chpoints = []
        self.topSimplices = []
        self.botSimplices = []

        # Cari convex hull
        self.findConvexHull()

        # Buat atribut points sebagai numpy array dari dataset
        self.points = np.array(self.ds)

        # Buat atribut simplices sebagai gabungan dari simplices bawah dan atas
        self.simplices = self.topSimplices + self.botSimplices

    
    # Mencari convex hull dari dataset ds.
    def findConvexHull(self):

        # Jika dataset hanya berisi 2 titik, langsung return
        if len(self.ds) <= 2:
            self.addToBotSimplices(p1, p2)
            return

        # Urutkan titik berdasarkan absis yang menaik
        sortedDs = sorted(self.ds, key=lambda x: x[0])
        p1 = sortedDs[0] # Titik minimum
        p2 = sortedDs[-1] # Titik maksimum

        # Masukkan ke dalam list hasil
        self.chpoints.append(p1) 
        self.chpoints.append(p2) 

        # Masukkan ke dalam simplices
        self.addToTopSimplices(p1, p2)
        self.addToBotSimplices(p1, p2)

        # Keluarkan p1 dan p2 dari sortedDs
        sortedDs.pop(0)
        sortedDs.pop(-1)

        # Pisahkan titik yang berada di atas dan di bawah gatis p1-p2
        dsAbove, dsBelow = splitDs(p1, p2, sortedDs)

        # Cek titik yang membentuk convex hull di atas dan bawah garis p1-p2
        self.findConvexHullPoint(p1, p2, dsAbove, True)
        self.findConvexHullPoint(p1, p2, dsBelow, False)


    # Mencari titik-titik yang membentuk convex hull secara rekursif
    # dengan menggunakan algoritma divide and conqueror
    def findConvexHullPoint(self, p1, p2, ds, isAbove):
        
        # Basis rekursi
        # Rekursi berhenti jika dataset ds sudah kosong atau ada titik yang bernilai null
        if ds == [] or p1 is None or p2 is None:
            return []

        farthestDistance = -1   # Inisisasi jarak titik terjauh
        farthestPoint = None    # Inisiasi titik terjauh
        
        # Cari titik terjauh di datastore ds
        for point in ds:
            distance = findDistance(p1, p2, point)
            if distance > farthestDistance:
                farthestDistance = distance
                farthestPoint = point

        # Masukkan titik terjauh ke dalam list hasil
        #print(farthestPoint)
        self.chpoints.append(farthestPoint)

        # Masukkan ke dalam simplices
        if isAbove:
            self.addToTopSimplices(p1, farthestPoint)
            self.addToTopSimplices(farthestPoint, p2)
        else :
            self.addToBotSimplices(p1, farthestPoint)
            self.addToBotSimplices(farthestPoint, p2)

        # Hapus titik terjauh dari dataset
        ds.remove(farthestPoint)

        # Pisahkan titik titik berdasarkan lokasinya terhadap garis p1-p2
        ds1Above, ds1Below = splitDs(p1, farthestPoint, ds) 
        ds2Above, ds2Below = splitDs(p2, farthestPoint, ds)

        if isAbove:
            # Jika is above bernilai true, cek titik bagian atas saja
            self.findConvexHullPoint(p1, farthestPoint, ds1Above, True) 
            self.findConvexHullPoint(farthestPoint, p2, ds2Above, True)
        else:
            # Jika is above bernilai false, cek titik bagian bawah saja
            self.findConvexHullPoint(p1, farthestPoint, ds1Below, False) 
            self.findConvexHullPoint(farthestPoint, p2, ds2Below, False)


    # Menghubungkan dua titik ke dalam simplices bawah
    def addToTopSimplices(self, p1, p2):

        # Cari index kedua titik
        i1 = self.ds.index(p1)
        i2 = self.ds.index(p2)

        simplicesSize = len(self.topSimplices)
        i = 0

        # Cek apakah titik p1 dan/atau p2 sudah ada
        # Jika ada, hapus terlebih dahulu
        while i < simplicesSize:
            if self.topSimplices[i][0] == i1:
                self.topSimplices.pop(i)
                simplicesSize -= 1
                continue
            if self.topSimplices[i][1] == i2:
                self.topSimplices.pop(i)
                simplicesSize -= 1
                continue
            i += 1

        # Masukkan index dari p1 dan p2 ke dalam simplices
        self.topSimplices.append([i1, i2])


    # Menghubungkan dua titik ke dalam simplices atas
    def addToBotSimplices(self, p1, p2):

        # Cari index kedua titik
        i1 = self.ds.index(p1)
        i2 = self.ds.index(p2)
        
        simplicesSize = len(self.botSimplices)
        i = 0

        # Cek apakah titik p1 dan/atau p2 sudah ada
        # Jika ada, hapus terlebih dahulu
        while i < simplicesSize:
            if self.botSimplices[i][0] == i1:
                self.botSimplices.pop(i)
                simplicesSize -= 1
                continue
            if self.botSimplices[i][1] == i2:
                self.botSimplices.pop(i)
                simplicesSize -= 1
                continue
            i += 1

        # Masukkan index dari p1 dan p2 ke dalam simplices
        self.botSimplices.append([i1, i2])