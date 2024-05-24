import math

def add(x, y):
    """Fungsi untuk melakukan penjumlahan"""
    return x + y

def subtract(x, y):
    """Fungsi untuk melakukan pengurangan"""
    return x - y

def multiply(x, y):
    """Fungsi untuk melakukan perkalian"""
    return x * y

def divide(x, y):
    """Fungsi untuk melakukan pembagian"""
    if y == 0:
        return "Error: Pembagian dengan nol tidak diperbolehkan."
    return x / y

def power(x, y):
    """Fungsi untuk melakukan perpangkatan"""
    return x ** y

def square_root(x):
    """Fungsi untuk melakukan perhitungan akar kuadrat"""
    if x < 0:
        return "Error: Akar kuadrat dari bilangan negatif tidak diperbolehkan."
    return math.sqrt(x)

def main():
    """Fungsi utama untuk menjalankan program kalkulator"""
    print("Program Kalkulator Sederhana")
    
    while True:
        print("\nPilih operasi yang ingin Anda lakukan:")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Perpangkatan")
        print("6. Akar Kuadrat")
        print("7. Keluar")
        
        choice = input("Masukkan pilihan (1/2/3/4/5/6/7): ").strip()
        
        if choice == '7':
            print("Terima kasih telah menggunakan kalkulator ini. Selamat tinggal!")
            break

        if choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Masukkan bilangan pertama: "))
                num2 = float(input("Masukkan bilangan kedua: "))
            except ValueError:
                print("Error: Masukkan nilai numerik yang valid.")
                continue
        
        if choice == '6':
            try:
                num = float(input("Masukkan bilangan: "))
            except ValueError:
                print("Error: Masukkan nilai numerik yang valid.")
                continue

        if choice == '1':
            print(f"Hasil: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Hasil: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Hasil: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"Hasil: {num1} / {num2} = {result}")
        elif choice == '5':
            print(f"Hasil: {num1} ^ {num2} = {power(num1, num2)}")
        elif choice == '6':
            result = square_root(num)
            print(f"Hasil: √{num} = {result}")
        else:
            print("Error: Pilihan tidak valid.")

        retry = input("Apakah Anda ingin melakukan operasi lain? (y/n): ").strip().lower()
        if retry != 'y':
            print("Terima kasih telah menggunakan kalkulator ini. Selamat tinggal!")
            break

if __name__ == "__main__":
    main()
