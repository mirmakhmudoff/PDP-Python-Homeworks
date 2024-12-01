yil = int(input("Yilni kiriting: "))

kabissa = yil % 4 == 0 and yil % 100 != 0 or yil % 400 == 0

print(f"{yil} kabissa yilmi? {kabissa}")