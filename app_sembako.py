from os import system
from time import sleep

def print_menu():
	system("cls")
	print("""
	Kasir Sembako Sederhana
	[1]. Lihat Semua Produk
	[2]. Tambah Produk Baru
	[3]. Cari Produk
	[4]. Hapus Produk
	[5]. Update Produk
	[Q]. Keluar
		""")

def print_header(msg):
	system("cls")
	print(msg)

def not_empty(container):
	if len(container) != 0:
		return True
	else:
		return False

def verify_ans(char):
	if char.upper() == "Y":
		return True
	else:
		return False

def print_data(contact=None, telp=True, hobi=True, all_data=False):
	if contact != None and all_data == False:
		print(f"NAMA : {contact}")
		print(f"TELP : {contacts[contact]['telp']}")
		print(f"HOBI : {contacts[contact]['hobi']}")
	elif hobi == False and all_data == False:
		print(f"NAMA : {contact}")
		print(f"TELP : {contacts[contact]['telp']}")
	elif all_data == True:
		for every_contact in contacts:
			nama = every_contact # nama = keynya
			telp = contacts[every_contact]["telp"]
			hobi = contacts[every_contacts]["hobi"]
			print(f"NAMA : {nama} - TELP : {telp} - HOBI : {hobi}")

def view_contacts():
	print_header("DAFTAR KONTAK TERSIMPAN")
	if not_empty(contacts):
		print_data(all_data=True)
	else:
		print("MAAF BELUM ADA KONTAK TERSIMPAN")
	input("Tekan ENTER untuk kembali ke MENU")

def add_contact():
	print_header("MENAMBAHAN KONTAK BARU")
	nama = input("NAMA \t: ")
	telp = input("TELP \t: ")
	hobi = input("HOBI \t: ")
	respon = input(f"Apakah yakin ingin menyimpan kontak : {nama} ? (Y/N")
	if verify_ans(respon):
		contacts[nama] = {
		"telp" : telp,
		"hobi" : hobi
		}
		print("Data Kontak Tersimpan")
	else:
		print("Data Batal Tersimpan")
	input("Tekan ENTER untuk kembali ke MENU")

def searching(contact):
	if contact in contacts:
		return True
	else:
		return False

def find_contact():
	print_header("MENCARI KONTAK")
	nama = input("Nama Kontak Yang Dicari : ")
	exists = searching(nama)
	if exixts:
		print("Data Ditemukan")
		print_data(contact)
	else:
		print("Data Tidak Ada")
	input("Tekan ENTER untuk kemali ke MENU")

def delete_contact():
	print_header("Menghapus kontak")
	nama = input("Nama Kontak yang akan dihapus : ")
	if exists:
		print_data(contact=nama)
		respon = input(f"yakin ingin menghapus {nama} ? (Y/N) ")
		if verify_ans(respon):
			del contacts[nama]
			print("Data Kontak Telah Dihapus")
		else:
			prinT("Data Kontak Batal Dihapus")
	else:
		print("Data Tidak Ada")
	input("Tekan ENTER untuk Kembali ke MENU ")



def check_user_input(char):
	char = char.upper()
	if char  == "Q":
		print("BYE!!!")
		return True 
	elif char == "1":
		view_contacts()
	elif char == "2":
		add_contact()
	elif char == "3":
		find_contact()
	elif char == "4":
		delete_contact()
	elif char == "5":
		pass

contacts = {
	"anas" : {
		"telp" : "213652",
		"hobi" : "rebahan"
	},
	"aming" : {
		"telp" : "1251554",
		"hobi" : "kupu kupu"
	}
}
#flag/sign/tanda menyimpan sebuah kondisi
stop = False

while not stop:
	print_menu()
	user_input =  input("Pilihan : ").upper()
	stop = check_user_input(user_input)
