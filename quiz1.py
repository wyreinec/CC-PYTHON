# --------EKSPRESI DAN VARIABEL-------- 

# KASUS SPLIT BILL
# 2 orang lagi makan malem
# tagihan = 47.25 dollar 
# tip = 15%
# hitung tip, total yang harus dibayar, setiap orang perlu bayar berapa

bill = 47.28
tip = bill * 0.15
total = bill + tip
share = total / 2 
print("Each person needs to pay: " + str(share))

# KASUS PEMBAGIAN
# bagaimana caranya agar hasil pembilang dan penyebut = 1?
numerator = 10
denominator = 10
result = numerator / denominator
print(result)

#KASUS MENGGABUNGKAN VARIABEL
word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "Python"
word6 = "so"
word7 = "far?"

print(word1 + " " + word2 + " " + word3 + " " + word4 + " " + word5 + " " + word6 + " " + word7)

# KASUS Menampilkan 2 + 2 = 4 tapi harus string
print("2 + 2 = " + str(2 + 2))

# -------- FUNCTION-------- 

#KASUS KONVERSI
# 1) Complete the function to return the result of the conversion
def convert_distance(miles): #mendefinisikan fungsi
	return miles * 1.6  # approximately 1.6 km in 1 mile

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(2*my_trip_km))

#KASUS MEMBANDINGKAN 2 ANGKA LALU DIURUTKAN MENAIK
# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)

#KASUS LUCKY NUMBER SESUAI DENGAN BANYAKNYA HURUF DALAM 1 NAMA
def lucky_number(name):
  number = len(name) * 9
  message = "Hello " + name + ". Your lucky number is " + str(number)
  return message
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))

# --------KONDISIONAL-------- 

# KASUS MENAMPILKAN NAMA
def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))

# KASUS PENYIMPANAN FILE
# Sistem dengan ukuran 4096 byte, menggunakan penyimpanan 4096 * 2 = 8192 byte. Berapa jumlah total byte yang diperlukan untuk menyimpan file dengan ukuran tertentu?
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return ((block_size * full_blocks) + block_size)
    return block_size * full_blocks

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192

# KASUS PENERJEMAHAN WARNA
def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown

# KASUS LULUS ATAU TIDAK
# Lulus = >= 60 dan <= 95
# Gagal = <60
# Nilai Tertinggi = 100

def exam_grade(score):
	if score == 100:
		grade = "Top Score"
	elif 95 >= score >= 60 :
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail

# KASUS MEMBALIKKAN NAMA
def format_name(first_name, last_name):
	# code goes here
	if first_name == '' and last_name == '':
		return ""
	elif last_name == " ":
		return "Name: " + first_name
	elif first_name == " ":
		return "Name: " + last_name
	else:
		return "Name: " + last_name + "," + first_name
	return string

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string

# KASUS MEMBANDINGKAN KATA TERPANJANG
def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2) >= len(word3) :
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))

# KASUS PEMBAGIAN
def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to 
# keep just the fractional part of the quotient
	return (numerator / denominator) % 1 if denominator else 0

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0