# WHILE LOOP
# Sedangkan perulangan while digunakan ketika jumlah perulangannya belum ditentukan (uncountable).
# Menjalankan baris kode di dalam blok kodenya secara terus menerus selama masih memenuhi ekspresi yang sudah ditentukan sebelumnya, yang berarti ia akan terus mengulang selama kondisi bernilai True. 

# KASUS PENGECEKAN BILANGAN PRIMA
def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor += 1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT

# KASUS MEMPERBAIKI INFINITE LOOP
def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  while n % 2 == 0 and n != 0:
    n = n / 2
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
    n += 1
  return False
  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False

# KASUS PEMBAGIAN
def sum_divisors(n):
  i = 1
  sum = 0
  # Return the sum of all divisors of n, not including n
  while i < n:
    if n % i == 0:
      sum += i
      i += 1
    else:
      i += 1
  return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114

# KASUS MENCETAK HASIL PERKALIAN YANG TIDAK LEBIH DARI 25

def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = multiplier * number 
		# What is the additional condition to exit out of the loop?
		if result > 25 :
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier += 1

multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5) 
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)	
# Should print: 8x1=8 8x2=16 8x3=24

# FOR LOOP
# Keduanya memiliki perbedaan pada segi penggunaan, dikatakan jika for lebih digunakan dalam perulangan yang sudah diketahui jumlah perulangannya (countable). 

# KASUS FAKTORIAL
def factorial(n):
    result = 1
    for x in range(1,n):
        result = result * x 
    return result

for n in range(0,10):
    print(n, factorial(n+1))

# KASUS PERULANGAN PERKALIAN 3 DARI X=1 SAMPAI X=10
for x in range(1,11):
  print(x**3)

# KASUS KELIPATAN 7 
for x in range(101):
    if x % 7 == 0:
        print(x)
   
# KASUS GAGAL/BERHASIL
def retry(operation, attempts):
  for n in range(attempts):
    if operation():
      print("Attempt " + str(n) + " succeeded")
      break
    else:
      print("Attempt " + str(n) + " failed")

retry(create_user, 3)
retry(stop_service, 5)

# FINAL GRADE 3
# MENAMPILKAN LOOPING 1 - 7

number = 1
while number in range (1,8):
	print(number, end=" ")
	number += 1

# KASUS MEMISAHKAN HURUF KE BAWAH DALAM 1 KATA 
def show_letters(word):
	for letters in word:
		print(letters)

show_letters("Hello")
# Should print one line per letter

# KASUS DIGIT
def digits(n):
	count = 0
	if n == 0:
	  return 1
	while (n > 0):
		count += 1
		n = n // 10
	return count
	
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1

# KASUS MATRIKS
def multiplication_table(start, stop):
	for x in range(start, stop + 1):
		for y in range(start, stop + 1):
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 3)
# Should print the multiplication table shown above

# KASUS COUNT DOWN/UP
def counter(start, stop):
	x = start
	if start > stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			x -= 1
			if x >= stop:
				return_string += ","
			
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			x += 1
			if x <= stop:
				return_string += ","
			
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"

# KASUS MENGEMBALIKAN STRING YANG BISA DIBAGI 2, LALU DICARI MAKSIMUMNYA
def even_numbers(maximum):
	return_string = ""
	for x in range (2, maximum+1, 2):
		return_string += str(x) + " "
	return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed

# KASUS PEMILIHAN SUARA
def votes(params):
	for vote in params:
	    print("Possible option:" + vote)