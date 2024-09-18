def konversi_nilai(nilai):
    """Mengonversi nilai dari rentang 1-100 ke rentang 0-1."""
    return nilai / 100

def main():
    while True:
        print("\nAplikasi Pengambilan Keputusan Penerimaan Karyawan Baru")
        
        # Input nilai dari pengguna (1-100)
        nilai_attitude = float(input("Masukkan nilai attitude (1-100): "))
        nilai_akademik = float(input("Masukkan nilai akademik (1-100): "))
        nilai_penampilan = float(input("Masukkan nilai penampilan (1-100): "))
        nilai_inisiatif = float(input("Masukkan nilai inisiatif (1-100): "))
        
        # Konversi nilai ke rentang 0-1
        attitude = konversi_nilai(nilai_attitude)
        akademik = konversi_nilai(nilai_akademik)
        penampilan = konversi_nilai(nilai_penampilan)
        inisiatif = konversi_nilai(nilai_inisiatif)
        
        # Hitung kontribusi setiap kriteria
        kontribusi_attitude = attitude * 0.2
        kontribusi_akademik = akademik * 0.4
        kontribusi_penampilan = penampilan * 0.1
        kontribusi_inisiatif = inisiatif * 0.3
        
        # Hitung total score
        total_score = (kontribusi_attitude + kontribusi_akademik +
                       kontribusi_penampilan + kontribusi_inisiatif)
        
        # Tentukan kategori hasil
        if total_score < 0.4:
            hasil = "Kurang Baik"
        elif total_score < 0.6:
            hasil = "Cukup"
        elif total_score < 0.8:
            hasil = "Baik"
        else:
            hasil = "Sangat Baik"
        
        # Tampilkan hasil
        print(f"\n--- Hasil Perhitungan ---")
        print(f"Kontribusi Attitude: {kontribusi_attitude:.2f}")
        print(f"Kontribusi Akademik: {kontribusi_akademik:.2f}")
        print(f"Kontribusi Penampilan: {kontribusi_penampilan:.2f}")
        print(f"Kontribusi Inisiatif: {kontribusi_inisiatif:.2f}")
        print(f"Total Score: {total_score:.2f}, Kategori: {hasil}")
        
        # Tanya pengguna apakah ingin menghitung lagi
        lanjut = input("\nApakah Anda ingin menghitung lagi? (ya/tidak): ").strip().lower()
        if lanjut != 'ya':
            print("Terima kasih! Program selesai.")
            break

if __name__ == "__main__":
    main()
