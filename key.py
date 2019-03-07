import os, sys

print ("--------------------B.S.T--------------------")
print ("\033[1;32mMasukan ID & Password nya bangsat")
print ("Kalo Gak Tau Chat Saya !")
print ("Mr.N4w4Nu6 Yang Tampan")
print ("Contact Me : 083145204326")
print ("--------------------CIA--------------------")
ID = 'Mr.N4w4Nu6'      
password = 'BL4CKSH4D0W TE4M'
def kembali():
	kembali = sys.executable
	os.execl(kembali, kembali, *sys.argv)


def main():
	id = raw_input("ID: ")
	if id == ID:
		pwd = raw_input("password : ")
		if pwd == password:

			print "\n\033[1;34mHello Welcome To Tools CIA",

			sys.exit()

		else:
			print "\n\033[1;36mIsi Dengan Benar Bangsat !!!\033[00m"
		print "Silakan Login Lagi!"
		print "Masukan Password Dengan Benar"
		print "Dimohon Login Lagi Yang Benar Goblok\n"

		kembali()

	else:
		print "\n\033[1;36mIsi Dengan Benar Anjing !!!\033[00m"
		print "Silakan Login Lagi!"
		print "Masukan ID dengan benar"
		print "Dimohon Login Lagi Yang Benar Goblok\n"

		kembali()

try:
	main()
except KeyboardInterrupt:
	os.system('clear')
	kembali()