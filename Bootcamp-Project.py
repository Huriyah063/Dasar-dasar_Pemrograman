''' Latihan sederhana Python.
    Note: Perhatikan syntax/penulisan, terdapat typo pada codingan latihan di bawah.
    Latihan ini menggunakan Basic Syntax, Assignment Operator, Variable, dan Condition
    * Fungsi quit() digunakan untuk mengakhiri program.
'''

print("Selamat datang di Quiz Komputer!")

playing = input("Lanjut main? ")

# Buatkan kondisi yang hanya menerima kata 'Ya' untuk memulai Quiz dari variable playing di atas.
# Jika masukan variable playing bukan 'Ya', maka hentikan program.
if playing.lower() != "ya":
    quit()

print("Okay, Ayo kita mulai! :)")
score = 0

# Berikan kondisi dimana jika jawaban benar, maka akan mencetak teks 'Correct!'
answer = input("What does GPU stand for?\n")
if answer.lower() == "central processing unit":
    print('Correct!')
    # Isi baris di bawah untuk menambahkan nilai 1 pada variable score jika jawaban benar.
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Ganti bagian yang digaris bawahi dengan variable yang mencetak jawaban benar,
# dan total nilai dari jawaban yang benar.
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
