def cari_huruf_tengah():
    huruf_pertama = input("Masukkan huruf pertama: ").upper()
    huruf_terakhir = input("Masukkan huruf terakhir: ").upper()
    abjad = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indeks_awal = abjad.index(huruf_pertama)
    indeks_akhir = abjad.index(huruf_terakhir)
    if indeks_awal < indeks_akhir:
        huruf_tengah = abjad[indeks_awal+1:indeks_akhir]
    else:
        huruf_tengah = abjad[indeks_akhir+1:indeks_awal][::-1]
    if len(huruf_tengah) % 2 == 0:
        tengah1 = int(len(huruf_tengah) / 2)
        tengah2 = tengah1 - 1
        return huruf_tengah[tengah2:tengah1+1]
    else:
        return huruf_tengah[len(huruf_tengah)//2]

print(cari_huruf_tengah())
