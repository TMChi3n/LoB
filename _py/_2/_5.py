# cau 5
path = r'D:\K15DCPM02\Python\_py\_1.py'
print(f'Duong dan tap tin la {path}')
ViTriBD = path.rfind('\\')
print(ViTriBD)
TapTin = path[ViTriBD+1:]
print(f'Tap tin va phan mo rong la : {TapTin}')
ViTriKT = path.rfind('.') - len(path)
Ten = TapTin[:ViTriKT]
print(f'Ten tap tin : {Ten}')