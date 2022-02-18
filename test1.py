# data = [
#     {'Nomor Telepon':6216343463,
#     'Nama':'HYPERMART GAJAH MADA',
#     'Alamat':'JL GAJAHMADA NO 19-26',
#     'Kota':'JAKARTA PUSAT',    
#     'Category':'DEPARTMENT STORE'},
#     {'Nomor Telepon':6287825086209,
#     'Nama':'DAPOER PANDAN WANGI',
#     'Alamat':'JL PATUHA NO 38',
#     'Kota':'BANDUNG',    
#     'Category':'RESTAURANT'},
#     {'Nomor Telepon':622486001900,
#     'Nama':'SILOAM HOSPITAL',
#     'Alamat':'JL KOMPOL MAKSUM NO 296',
#     'Kota':'SEMARANG',
#     'Category':'HOSPITAL'},
#     {'Nomor Telepon':12345678,
#     'Nama':'LEVI ACKERMAN',
#     'Alamat':'MIZUBE NO SATO AOYAMA 4106',
#     'Kota':'HITA',
#     'Category':'PRIVATE'},
#     ]
# def daftar_nomor ():
#     print('{:<4}|{:<14}|{:<25}|{:<30}|{:<14}|{:<16}'.format('No','Nomor Telepon','Nama','Alamat','Kota','Category'))
#     for i in range(len(data)):
#      print('{:<4}|{:<14}|{:<25}|{:<30}|{:<14}|{:<16}'.format(i+1,data[i]['Nomor Telepon'],data[i]['Nama'],data[i]['Alamat'],data[i]['Kota'],data[i]['Category']))


# def MenuTambah():
#     a = [d['Nomor Telepon'] for d in data if 'Nomor Telepon' in d]
#     nomor_telepon = int(input('masukkan Nomor Telepon :'))
#     if  nomor_telepon in a:
#         print('******DATA SUDAH TERDAFTAR******')
#     elif nomor_telepon not in a:
#         Nama = input('masukkan Nama:')
#         Alamat = input('masukkan Alamat:')
#         Kota = input('masukkan Kota:')
#         Category = input('masukkan Category:')
#         while True:
#             Yes_no = input('apakah anda ingin menyimpan (Y/N):').capitalize()
#             if Yes_no == 'Y':
#                 data.append({'Nomor Telepon': nomor_telepon,'Nama': Nama,'Alamat': Alamat,'Kota':Kota,'Category':Category})
#                 print('******DATA TELAH DISIMPAN******')                
#                 return MenuKedua()
#             elif Yes_no == 'N':                
#                 return MenuKedua()

# def MenuUbah():
#     a = [d['Nomor Telepon'] for d in data if 'Nomor Telepon' in d]
#     nomor_telepon = int(input('masukkan Nomor Telepon :'))
#     if  nomor_telepon not in a:
#         print('******DATA TIDAK TERDAFTAR******')
#     elif nomor_telepon in a:
#         b = next(nomor for nomor in data if nomor["Nomor Telepon"] == nomor_telepon)
#         print('\n{:<14}|{:<25}|{:<30}|{:<14}|{:<16}'.format(*b.values()))
#         while True:
#             Yes_no = input('\napakah anda ingin mengubah data (Y/N):').capitalize()
#             if Yes_no == 'Y':
#                 key = input("pilih salah satu dari kolom Nama,Alamat,Kota,Category yang akan diupdate:").capitalize()
#                 val = input('input {} baru:'.format(key))
#                 while True:
#                     Yes_no = input('apakah anda ingin menyimpan (Y/N):').capitalize()
#                     if Yes_no == 'Y':
#                         b[key]=val
#                         print('******DATA TELAH DISIMPAN******')                                                                           
#                         return MenuKetiga()
#                     elif Yes_no == 'N':
#                         print('******DATA TIDAK DISIMPAN******')                
#                         return MenuKetiga()                  
#             elif Yes_no == 'N':                
#                 return MenuKetiga()
            

# def MenuPertama():
#     while (True):
#         inputMenu = input('''
# +++++++++++++DAFTAR NOMOR KONTAK+++++++++++++

# 1. menampilkan daftar 
# 2. mencari daftar berdasarkan nomor telepon
# 3. kembali ke menu utama

# Masukkan angka dari list diatas :''')
#         if inputMenu=='1':
#             daftar_nomor ()
#         elif inputMenu=='2':
#             print('Masukkan Nomor Telepon:')
#             nomorTelepon = int(input())
#             print(next((nomor for nomor in data if nomor["Nomor Telepon"] == nomorTelepon), '\n******DATA TIDAK TERDAFTAR******'))                                                                                    
#         elif inputMenu=='3':
#             return menuUtama()            

# def MenuKedua():
#     while (True):
#         inputMenu = input('''
# +++++++++++++DAFTAR NOMOR KONTAK+++++++++++++

# 1. Tambah daftar Telepon
# 2. kembali ke menu utama

# Masukkan angka dari list diatas :''')
#         if inputMenu =='1':
#             MenuTambah()
#         elif inputMenu =='2':
#             return menuUtama()

# def MenuKetiga():
#     while (True):
#         inputMenu = input('''
# +++++++++++++DAFTAR NOMOR KONTAK+++++++++++++

# 1. Ubah data daftar Telepon
# 2. kembali ke menu utama

# Masukkan angka dari list diatas :''')
#         if inputMenu =='1':
#             MenuUbah()
#         elif inputMenu =='2':
#             return menuUtama()

# def MenuKeempat():
#     while (True):
#         inputMenu = input('''
# +++++++++++++DAFTAR NOMOR KONTAK+++++++++++++

# 1. Hapus data daftar Telepon
# 2. kembali ke menu utama

# Masukkan angka dari list diatas :''')
#         if inputMenu =='1':
#             a = [d['Nomor Telepon'] for d in data if 'Nomor Telepon' in d]
#             nomor_telepon = int(input('masukkan Nomor Telepon :'))
#             if  nomor_telepon not in a:
#                 print('\nData Tidak Terdaftar')
#             elif nomor_telepon in a:                                  
#                 index = a.index(nomor_telepon)
#                 while True:
#                     Yes_no = input('apakah anda ingin menghapus data (Y/N):').capitalize()
#                     if Yes_no == 'Y':
#                         del data[index]
#                         print('******DATA DIHAPUS******')
#                         daftar_nomor()
#                         return MenuKeempat()  
#                     elif Yes_no == 'N':
#                         print('******DATA TIDAK DIHAPUS******')               
#                         return MenuKeempat()                  
#         elif inputMenu =='2':
#             return menuUtama()

# def menuUtama ():
#     while (True):
#         inputMenuUtama = input('''
# +++++++++++++DAFTAR NOMOR KONTAK+++++++++++++

# 1. menampilkan daftar Nomor Telepon
# 2. menambah daftar Nomor Telepon
# 3. Update daftar Nomor Telepon
# 4. Menghapus Daftar Nomor Telepon
# 5. Exit

# Masukkan angka dari list diatas :''')
#         if inputMenuUtama=='1':
#             MenuPertama()
#         elif inputMenuUtama=='2':
#             MenuKedua()
#         # elif inputMenuUtama=='2':
#         # elif inputMenuUtama=='2':
#         elif inputMenuUtama=='5':
#             print('Terimakasih menggunakan layanan kami, Sampai Jumpa')
#             break
#         else:
#             print('\n******SILAHKAN MASUKKAN ANGKA YANG BENAR******')

# MenuUtama()



