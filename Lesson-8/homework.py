# 1 - masala
yosh = int(input("Yoshingizni kiriting: "))
if yosh >= 18:
    print("voyaga yetgan")
else:
    print("voyaga yetmagan")

# 2 - masala
baho = int(input("Bahoni kiriting: "))
if baho == 5:
    print("a'lo")
elif baho == 4:
    print("yaxshi")
elif baho == 3:
    print("qoniqarli")
elif baho == 2:
    print("qoniqarsiz")

# 3 - masala
oy = int(input("Oy raqamini kiriting: "))
if oy in [12, 1, 2]:
    print("Qish fasli")
elif oy in [3, 4, 5]:
    print("Bahor fasli")
elif oy in [6, 7, 8]:
    print("Yoz fasli")
elif oy in [9, 10, 11]:
    print("Kuz fasli")

# 4 - masala
harorat = float(input("Havoning haroratini kiriting: "))
if harorat > 30:
    print("havo issiq")
elif 20 <= harorat <= 30:
    print("havo iliq")
elif harorat < 15:
    print("havo sovuq")

# 5 - masala
kun = int(input("Hujjat amal qilish muddati (kun): "))
if kun > 5:
    print("hujjat amal qilish muddati tugadi")
else:
    print("hujjat amal qilish muddati hali tugamagan")

# 6 - masala
tolov_usuli = input("To'lov usulini kiriting (naqt yoki karta): ")
if tolov_usuli == "naqt":
    summa = float(input("Summani kiriting: "))
    print("Summa kiritildi:", summa)
elif tolov_usuli == "karta":
    parol = input("Parolni kiriting: ")
    print("Parol qabul qilindi")

# 7 - masala
baho = int(input("Bahoni kiriting: "))
if baho >= 90:
    print("A")
elif baho >= 80:
    print("B")
elif baho >= 70:
    print("C")
elif baho >= 60:
    print("D")
else:
    print("F")

# 8 - masala
yosh = int(input("Yoshingizni kiriting: "))
if yosh > 18:
    print("Kattalar")
else:
    print("Bolalar")

# 9 - masala
ob_havo = input("Ob-havo qanday? (yomg'ir/qor/yaxshi): ")
if ob_havo == "yomg'ir" or ob_havo == "qor":
    print("Ko'ylak kiyma")

# 10 - masala
tolov_turi = input("To'lov turini tanlang (naqd yoki kartochka): ")
if tolov_turi == "naqd":
    print("Siz naqd to'lovni tanladingiz")
elif tolov_turi == "kartochka":
    print("Siz kartochka orqali to'lovni tanladingiz")

baho = int(input("Bahoni kiriting: "))
if baho >= 70:
    print("Sertifikat olishingiz mumkin")

# 12 - masala
oy = int(input("Oy raqamini kiriting: "))
if oy in [12, 1, 2]:
    print("Qish fasli")
elif oy in [3, 4, 5]:
    print("Bahor fasli")
elif oy in [6, 7, 8]:
    print("Yoz fasli")
elif oy in [9, 10, 11]:
    print("Kuz fasli")

# 13 - masala
baho1 = int(input("1-bahoni kiriting: "))
baho2 = int(input("2-bahoni kiriting: "))
baho3 = int(input("3-bahoni kiriting: "))
ortalama = (baho1 + baho2 + baho3) / 3
if ortalama >= 4:
    print("Yaxshi")
elif ortalama >= 3:
    print("O'rtacha")
else:
    print("Yomon")

# 14 - masala
taom = input("Xohlagan taomingizni tanlang: ")
print("Tayyorlashga kirishamiz")

# 15 - masala
yosh = int(input("Avtomobilning yoshi: "))
masofa = int(input("Yurgan masofasi (km): "))
if yosh > 10:
    print("Ehtiyot qismlarni tekshiring")

# 16 - masala
yosh = int(input("Yoshingizni kiriting: "))
jins = input("Jinsingizni kiriting (erkak/ayol): ")
if jins == "erkak" and yosh < 18:
    print("Yosh bolaga o'yinchoq sovg'a qiling")
elif jins == "ayol" and yosh >= 18:
    print("Ayolga gul sovg'a qiling")
else:
    print("Mos sovg'a tanlash")

# 17 - masala
baho = int(input("Bahoni kiriting: "))
if baho > 100:
    print("Reytingni yangilang")

# 18 - masala
vaqt = int(input("Vaqtni kiriting (soat): "))
if 0 <= vaqt < 6 or 18 <= vaqt < 24:
    print("Xayrli tun")
else:
    print("Xayrli kun")

# 19 - masala
parol = input("Parolni kiriting: ")
if len(parol) < 8:
    print("Parolni kuchaytiring")

# 20 - masala
daromad = float(input("Oylik daromadingizni kiriting: "))
qarz = float(input("Qarzingizni kiriting: "))
if daromad > qarz:
    print("Kredit olish mumkin")

