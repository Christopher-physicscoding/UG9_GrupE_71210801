nama = str (input(" nama : "))
tempat_tanggal_lahir = input ("tempat tanggal lahir : ")
nama_depan = nama.split()[0]
nama_belakang = nama.split()[-1]
nama_tengah = nama.split()[-2]
print( "haloo! "+" ".join([nama_belakang, nama_depan ]))
print(" anda lahir di",tempat_tanggal_lahir)

nama = str (input(" nama : "))
tempat_tanggal_lahir = input ("tempat tanggal lahir : ")
nama_depan = nama.split()[0]
nama_tengah = nama.split()[-2]
nama_belakang = nama.split()[-1]
print( "haloo! "+" ".join([nama_belakang, nama_depan,nama_tengah]))
print(" anda lahir di",tempat_tanggal_lahir) 
       
