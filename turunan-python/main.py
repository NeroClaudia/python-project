import math

while True:
    try:
        print("1. Input x^n: ")
        print("2. Input sin(kx): ")
        print("3. Input e^kx: ")
        print("4. Input ln(x): ")
        print("5. Exit")

        pilihan = int(input("Input pilihan (1-5): "))

        if pilihan == 5:
            print("Program selesai")
            break

        elif pilihan not in [1, 2, 3, 4]:
            raise KeyError
        
        x0 = float(input("Input nilai x0: "))

        if pilihan == 1:
            n = float(input("Input nilai n: "))
            hasil = n * (x0 ** (n - 1))
            print(f"f'(x) = n * x^(n-1) = {n} * {x0}^({n}-1) = {hasil}")

        elif pilihan == 2:
            k = float(input("Input nilai k: "))
            x0_rad = math.radians(k * x0)
            hasil = k * (math.cos(x0_rad))
            print(f"f'(x) = k * cos(kx) = {k} * cos({k}*{x0}°) = {hasil:.4f}")

        elif pilihan == 3:
            k = float(input("Input nilai e: "))
            hasil = k * (math.exp(k * x0))
            print(f"f'(x) = k * e^(kx) = {k} * e^({k}*{x0}) = {hasil}")

        elif pilihan == 4:
            if x0 <= 0:
                print("Fungsi ln(x) hanya terdefinisi untuk x > 0!")
            else:
                hasil = 1 / x0
                print(f"f'(x) = 1/x = 1/{x0} = {hasil}")

    except ValueError:
        print("Input yang diberikan bukan tipe data numerik yang dapat diproses")
    
    except KeyError:
        print("Pilihan menu tidak tersedia")
    
    except Exception as e:
        print(f"Terdapat error tak terduga {e}")