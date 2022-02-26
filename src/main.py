import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
import random
import sys

# Cek apakah terdapat argumen
if len(sys.argv) >= 2:
    if int(sys.argv[1]) == 1:
        print("Menggunakan dataset iris")
        data =datasets.load_iris()
    elif int(sys.argv[1]) == 2:
        print("Menggunakan dataset wine")
        data =datasets.load_wine()
    elif int(sys.argv[1]) == 3:
        print("Menggunakan dataset breast cancer")
        data = datasets.load_breast_cancer()
    else :
        print("Menggunakan dataset default : iris")
        data = datasets.load_iris()
    if len(sys.argv) >= 3:
        x = int(sys.argv[2])
        print(f"Menggunakan kolom ke-{x} sebagai sumbu x")
        if len(sys.argv) >= 4:
            y = int(sys.argv[3])
            print(f"Menggunakan kolom ke-{y} sebagai sumbu y")
        else :
            y = 1
            print("Menggunakan kolom ke-1 sebagai sumbu y (default)")
    else :
        x = 0
        print("Menggunakan kolom ke-0 sebagai sumbu x (default)")
        y = 1
        print("Menggunakan kolom ke-1 sebagai sumbu y (default)")

else :
    print("Menggunakan dataset default : iris")
    data = datasets.load_iris()
    x = 0
    print("Menggunakan kolom ke-0 sebagai sumbu x (default)")
    y = 1
    print("Menggunakan kolom ke-1 sebagai sumbu y (default)")
print()

#create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)

#visualisasi hasil ConvexHull
try :
    import matplotlib.pyplot as plt
    from myConvexHull import MyConvexHull
    plt.figure(figsize = (10, 6))
    plt.title(data.feature_names[x] + ' vs ' + data.feature_names[y])
    plt.xlabel(data.feature_names[x])
    plt.ylabel(data.feature_names[y])
    for i in range(len(data.target_names)):
        bucket = df[df['Target'] == i]
        bucket = bucket.iloc[:,[x,y]].values

        hull = MyConvexHull(bucket) 
        #bagian di atas diganti dengan hasil implementasi ConvexHull Divide & Conquer

        color = '#' + str(hex(random.randint(48,160))[2::]) + str(hex(random.randint(48,160))[2::]) + str(hex(random.randint(48,160))[2::])
        plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i], color=color)
        for simplex in hull.simplices:
            plt.plot(bucket[simplex, 0], bucket[simplex, 1], color)
    plt.legend()
    plt.show()
except :
    print("Kolom dari dataset yang diberikan bukan merupakan bilangan")
    print("Tidak dapat membentuk convex hull")