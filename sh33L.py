import requests,sys
W = '\033[1;37m' # White bold
N  = '\033[0m'  # white (Normal)
R = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
print W+R+"""
[+]
 |  ___  _   _  ___  ___  __   
 | / __)( )_( )(__ )(__ )(  )  
 | \__ \ ) _ (  (_ \ (_ \ )(__ 
 | (___/(_) (_)(___/(___/(____) v.2"""
print W+R+" |\n[+]"+W+" Tittle   : "+O+"WebShell Scanner\n"+W+R+"[+]"+W+" Coded By : "+O+"AnjasT3chSoft"
print W+R+"[+]"+W+" Github   :"+O+" https://github.com/anjastech"
print W+R+"[+]"+W+" Facebook :"+O+" https://web.facebook.com/anjelo.sonliberto"
print W+R+"[+]___________________________________________[+]"
print W+"\n[+]=="+R+" Menu :"
print W+B+"\n  1"+R+")"+W+" Default dengan fitur pencarian acak (Disarankan)"
print W+B+"  2"+R+")"+W+" Manual dengan webshell kamu sendiri"
print W+B+"  3"+R+")"+W+" Info"
print W+B+"  4"+R+")"+W+" Keluar."
menu=raw_input(W+'\n[+]=='+R+' Menu>>'+W+' ')
if "1" in menu:
	terget=raw_input(R+"[?]"+W+" Target UrL>> ")
	reps=terget+"/"
	if "http://" in terget:
		t=terget.replace('http://','')
		try:
			print W+B+"[*]"+W+" Target IP :"+G+"",requests.get('http://ip-api.com/json/%s'%(t)).json()["query"]
		except:
			print R+"[-] Koneksi Error"+W
			sys.exit()
	elif "https://" in terget:
		t=terget.replace('https://','')
		try:
			print W+B+"[*]"+W+" Target IP :"+G+"",requests.get('http://ip-api.com/json/%s'%(t)).json()["query"]
		except:
			print R+"[-] Koneksi Error!"+W
			sys.exit()
	else:
		print R+"[-] Gunakan: http://Situs.com"+W
		sys.exit()
	lst={"/wp-content/":"Wordpress"}
	for path,cms in lst.items():
		try:
			r=requests.get(reps+path)
		except:
			print R+"[!] Gunakan: http://Situs.com"+W
			sys.exit()
		if r.status_code == 200:
			print W+R+"[!]"+O+" Peringatan! :"+W+R+" Situs Ini menggunakan CMS",cms
			print W+B+"[*]"+W+" Bruteforcing Webshell Dengan "+R+"Wplist.txt ..."
			o=open('wordlist/wplist.txt').readlines()
			l=len(o)
			print W+B+"[*]"+W+R+" "+str(l)+" "+W+"Webshell Daftar Di Mulai!\n"
			word=open('wordlist/wplist.txt')
			result=open('result.txt','w')
			for k in range(l):
				list=word.readline().replace('\n','')
				uri=reps+list
				try:
					permintaan=requests.get(uri)
				except:
					print R+"[!] Gunakab: http://Situs.com"+W
					sys.exit()
				if permintaan.status_code == 200:
					print G+"[+] Found Shell"
					print R+"[!] "+W+"PATH :",uri
					result.write(uri+"\n")
				else:
					print R+"[-]"+W+" Tidak Di temukan, Periksa Koneksi internet anda! "+R+"=>"+W+"",list
			result.close()
			print "\n"+W+B+"[*]"+W+" Scan Selesai Dan berhasil."
			print W+B+"[*]"+W+" Hasil :"+R+W+"",str(len(open('result.txt').readlines()))
			print W+B+"[*]"+W+" Hasil di simpan ke :"+R+"result.txt"+W
			sys.exit()
		else:
			print W+B+"[*]"+W+" Bruteforcing Webshell Dengan "+R+"randomlist.txt ...\n"
			file=open("wordlist/randomlist.txt").readlines()
			c=len(file)
			print W+B+"[*]"+W+R+" "+str(c)+" "+W+"Random Daftar Di Muat!"
			fil=open('wordlist/randomlist.txt')
			filed=open('result.txt','w')
			for p in range(c):
				wordlist=fil.readline().replace('\n','')
				ur=reps+wordlist
				try:
					rrr=requests.get(ur)
				except:
					print R+"[!] Gunkan: http://Situs.com"+W
					sys.exit()
				if rrr.status_code == 200:
					print G+"[+] Shell Di Temukan"
					print R+"[!] "+W+"PATH :",ur
					filed.write(ur+"\n")
				else:
					print R+"[-]"+W+" Tidak Di temukan! "+R+"=>"+W+"",wordlist
			filed.close()
			print "\n"+W+B+"[*]"+W+" Scan Finished."
			print W+B+"[*]"+W+" Result :"+R+W+"",str(len(open('result.txt').readlines()))
			print W+B+"[*]"+W+" Result Saved To :"+R+"result.txt"+W
			sys.exit()

if "2" in menu:
	urtarget=raw_input(R+"[?]"+W+" Target UrL>> ")
	reps=urtarget+"/"
	urlist=raw_input(R+"[?]"+W+" WebShell Daftar>> ")
	if "http://" in urtarget:
		t=urtarget.replace('http://','')
		try:
			print W+B+"[*]"+W+" Target IP :"+G+"",requests.get('http://ip-api.com/json/%s'%(t)).json()["query"]
		except:
			print R+"[!] Koneksi Error!"+W
			sys.exit()
	elif "https://" in urtarget:
		t=urtarget.replace('https://','')
		try:
			print W+B+"[*]"+W+" Target IP :"+G+"",requests.get('http://ip-api.com/json/%s'%(t)).json()["query"]
		except:
			print R+"[-] Connection Error!"+W
			sys.exit()
	else:
		print R+"[-] Ussage: http://site.com"+W
		sys.exit()
	try:
		ur=open(urlist).readlines()
	except:
		print R+"[!] List Not Found!"
		sys.exit()
	urnum=len(ur)
	print W+B+"[*]"+W+R+" "+str(urnum)+" "+W+"List Loaded!"
	print W+B+"[*]"+W+" Bruteforcing Webshell With"+R+"",urlist+"\n"
	meme=open(urlist)
	filos=open('result.txt','w')
	for me in range(urnum):
		wl=meme.readline().replace('\n','')
		uri=reps+wl
		try:
			rr=requests.get(uri)
		except:
			print R+"[!] Ussage: http://site.com"+W
			sys.exit()
		if rr.status_code == 200:
			print G+"[+] Found Shell"
			print R+"[!] "+W+"PATH :",uri
			filos.write(uri+"\n")
		else:
			print R+"[-]"+W+" Not Found! "+R+"=>"+W+"",wl
	filos.close()
	print "\n"+W+B+"[*]"+W+" Scan Finished."
	print W+B+"[*]"+W+" Result :"+R+W+"",str(len(open('result.txt').readlines()))
	print W+B+"[*]"+W+" Result Saved To :"+R+"result.txt"+W
else:
	print R+"[-] Input Failed!"+W
	sys.exit()
