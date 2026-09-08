batas_nilai = (65, 100)

nilai_masuk = []
lulus = []
remedi = []

while True:
    nilai = input("Masukkan nilai (ketik 'selesai' untuk berhenti): ")

    if nilai == "selesai":
        break

    nilai = int(nilai)

    if nilai >= 0 and nilai <= batas_nilai[1]:
        nilai_masuk.append(nilai)

        if nilai >= batas_nilai[0]:
            lulus.append(nilai)
        else:
            remedi.append(nilai)
    else:
        print("Nilai harus 0-100!")

print("\nNilai masuk:", nilai_masuk)
hapus = input("Masukkan nilai yang ingin dihapus (ketik 'tidak' jika tidak ada): ")

if hapus != "tidak":
    hapus = int(hapus)

    if hapus in nilai_masuk:
        nilai_masuk.remove(hapus)

        if hapus in lulus:
            lulus.remove(hapus)

        if hapus in remedi:
            remedi.remove(hapus)

        print("Nilai berhasil dihapus.")
    else:
        print("Nilai tidak ditemukan.")

print("\nHasil Akhir")
print("Batas nilai :", batas_nilai)
print("Nilai masuk :", nilai_masuk)
print("Lulus       :", lulus)
print("Remedi      :", remedi)