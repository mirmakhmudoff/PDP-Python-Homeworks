car = float(input("Avtomobilning narxini kiriting: "))
tolangan = float(input("To'langan qismini kiriting: "))
oy = int(input("Necha oyga bo'lib to'lashni xohlaysiz? (oylar soni): "))
yillik_foiz = float(input("Yillik foiz miqdorini kiriting (masalan, 10 foiz uchun 10): "))

if tolangan >= car * 0.5:
    qolgan_sum = car - tolangan
    monthly_payment = qolgan_sum / oy

    increased_qolgan_sum = qolgan_sum * (1 + yillik_foiz / 100)
    monthly_payment_with_interest = increased_qolgan_sum / oy

    print(f"Qolgan qismini {oy} oyga bo'lib to'lash uchun oylik to'lov miqdori: {monthly_payment:.2f} so'm")
    print(f"Yillik {yillik_foiz}% oshirish bilan oylik to'lov miqdori: {monthly_payment_with_interest:.2f} so'm")
else:
    print("To'lov umumiy narxning kamida 50% bo'lishi kerak!")
