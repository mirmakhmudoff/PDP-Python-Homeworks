narx1 = float(input("Birinchi mahsulotning narxini kiriting: "))
narx2 = float(input("Ikkinchi mahsulotning narxini kiriting: "))

if narx1 < narx2:
    print("Birinchi mahsulot arzonroq.")
elif narx1 > narx2:
    print("Ikkinchi mahsulot arzonroq.")
else:
    print("Ikkala mahsulotning narxi teng.")