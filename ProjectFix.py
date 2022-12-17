import pandas as pd, os, csv
from functools import reduce

with open("dataMhs.csv", "r") as f:
    reader = csv.DictReader(f)
    alldata = list(reader)
    data = alldata[:1000]

#LOGIKA
#IP/IPK
def filteringIPBesar():
    filtering = pd.DataFrame(filter((lambda x : True if int(float(x["ips"])) >= 3.0 else False), data))
    NilaiIp = filtering[:]["ips"]
    return print(NilaiIp)
def filteringIPKBesar():
    filtering = pd.DataFrame(filter((lambda x : True if int(float(x["ipk"])) >= 3.0 else False), data))
    NilaiIp = filtering[:]["ipk"]
    return print(NilaiIp)
def filteringIPKecil():
    filtering = pd.DataFrame(filter((lambda x : True if int(float(x["ips"])) < 3.0 else False), data))
    NilaiIp = filtering[:]["ips"]
    return print(NilaiIp)
def filteringIPKKecil():
    filtering = pd.DataFrame(filter((lambda x : True if int(float(x["ipk"])) < 3.0 else False), data))
    NilaiIp = filtering[:]["ipk"]
    return print(NilaiIp)

#2019/2020
def filteringThAkademik2019():
    filtering = pd.DataFrame(filter((lambda x : x["tahun_akademik"] == "2019/2020-Ganjil"), data))
    NilaiIp = filtering
    return print(NilaiIp)
def filteringThAkademik2020():
    filtering = pd.DataFrame(filter((lambda x : x["tahun_akademik"] == "2020/2021-Genap"), data))
    NilaiIp = filtering
    return print(NilaiIp)

#SGanjil/SGenap
def filteringSganjil():
    filtering = pd.DataFrame(filter((lambda x : int(x["semester_mahasiswa"]) % 2 == 1), data))
    NilaiIp = filtering
    return print(NilaiIp)
def filteringSgenap():
    filtering = pd.DataFrame(filter((lambda x : int(x["semester_mahasiswa"]) % 2 == 0), data))
    NilaiIp = filtering
    return print(NilaiIp)

#Matkul
def filteringMTA1():
    filtering = pd.DataFrame(filter((lambda x : x["nama_mk"] == "Tugas Akhir 1 (Proposal)"), data))
    NilaiIp = filtering
    return print(NilaiIp)
def filteringMTA2():
    filtering = pd.DataFrame(filter((lambda x : x["nama_mk"] == "Tugas Akhir 2 "), data))
    NilaiIp = filtering
    return print(NilaiIp)
def filteringMPWeb():
    filtering = pd.DataFrame(filter((lambda x : x["nama_mk"] == "Pemrograman Web*"), data))
    NilaiIp = filtering
    return print(NilaiIp)
def filteringMKP():
    filtering = pd.DataFrame(filter((lambda x : x["nama_mk"] == "Kerja  Praktik  "), data))
    NilaiIp = filtering
    return print(NilaiIp)
def filteringMPL():
    filtering = pd.DataFrame(filter((lambda x : x["nama_mk"] == "Kriptografi (PL)"), data))
    NilaiIp = filtering
    return print(NilaiIp)
def filteringMMN():
    filtering = pd.DataFrame(filter((lambda x : x["nama_mk"] == "Metode Numerik*"), data))
    NilaiIp = filtering
    return print(NilaiIp)
def filteringMPBO():
    filtering = pd.DataFrame(filter((lambda x : x["nama_mk"] == "Pemrograman  Berorientasi Objek*"), data))
    NilaiIp = filtering
    return print(NilaiIp)
def filteringMSPK():
    filtering = pd.DataFrame(filter((lambda x : x["nama_mk"] == "Sistem Pendukung Keputusan"), data))
    NilaiIp = filtering
    return print(NilaiIp)

#NIM
def filteringNimGanjil():
    filtering = pd.DataFrame(filter((lambda x : int(x["nim"][10]) % 2 == 1), data))
    NilaiIp = filtering
    return print(NilaiIp)
def filteringNimGenap():
    filtering = pd.DataFrame(filter((lambda x : int(x["nim"][10]) % 2 == 0), data))
    NilaiIp = filtering
    return print(NilaiIp)

# filteringNimGenap()
# filteringMTA2()

def clear():
    os.system("cls")

def main():
    clear()
    print()
    print("======================================")
    print("      REPOSITORY DATA MAHASISWA       ")
    print("             INFORMATIKA              ")
    print("======================================")
    print("| 1. Tampilkan Seluruh Data          |")
    print("| 2. Tampilkan Nama Mahasiswa        |")
    print("| 3. Tampilkan NIM Mahasiswa         |")
    print("| 4. Tampilkan Tahun Akademik        |")
    print("| 5. Tampilkan Semester Mahasiswa    |")
    print("| 6. Tampilkan Mata Kuliah           |")
    print("| 7. Tampilkan Nilai IP Mahasiswa    |")
    print("| 0. Keluar Program                  |")
    print("======================================") 
    print()

    def SeluruhData():
        frame = pd.DataFrame(data)
        print(frame)
        print()
        print("Seluruh data telah ditampilkan")
        input()
        main()
    def NamaMahasiswa():
        def NamaMahasiswa():
            mapping = pd.DataFrame(map(lambda x : x["nama"], data))
            return print(mapping)
        return NamaMahasiswa()
    def NIMMahasiswa():
        clear()
        def MenuNIM():
            clear()
            print("======================================")
            print("          Silahkan Pilih NIM          ")
            print("            [Ganjil/Genap]            ")
            print("======================================")
            print("| 1. Tampilkan Seluruh Data          |")
            print("| 2. Tampilkan NIM Ganjil            |")
            print("| 3. Tampilkan NIM Genap             |")
            print("| 0. Keluar Program                  |")
            print("======================================")
            def Ndata():
                clear()
                frame = pd.DataFrame(data)
                print(frame)
                input()
                MenuNIM()
            def NIMGanjil():
                clear()
                filteringNimGanjil()
                input()
                MenuNIM()
            def NIMGenap():
                clear()
                filteringNimGenap()
                input()
                MenuNIM()
            inputNIM = int(input("Masukan Pilihan :"))
            return Ndata() if inputNIM==1 else NIMGanjil() if inputNIM==2 else NIMGenap() if inputNIM==3 else main() if inputNIM==0 else print("pilihan tidak ada")
        return MenuNIM()
    def TahunAMahasiswa():
        clear()
        def MenuTahun():
            clear()
            print("======================================")
            print("       Silahkan Tahum Akademik        ")
            print("        [2019-2020/2020-2021]         ")
            print("======================================")
            print("| 1. Tampilkan Seluruh Data          |")
            print("| 2. Tampilkan Tahun 2019-2020       |")
            print("| 3. Tampilkan Tahun 2020-2021       |")
            print("| 0. Keluar Program                  |")
            print("======================================")
            def Sdata():
                clear()
                frame = pd.DataFrame(data)
                print(frame)
                input()
                MenuTahun()
            def TTahun2019():
                clear()
                filteringThAkademik2019()
                input()
                MenuTahun()
            def TTahun2020():
                clear()
                filteringThAkademik2020()
                input()
                MenuTahun()
            inputT = int(input("Masukan Pilihan :"))
            return Sdata() if inputT ==1 else TTahun2019() if inputT==2 else TTahun2020() if inputT==3 else main() if inputT==0 else print("Pilihan tidak ada")
        return MenuTahun()
    def SemesterMahasiswa():
        clear()
        def MenuSem():
            clear()
            print("======================================")
            print("        Silahkan Pilih Semester       ")
            print("             [Ganjil/Genap]           ")
            print("======================================")
            print("| 1. Tampilkan Seluruh Data          |")
            print("| 2. Tampilkan Semester Ganjil       |")
            print("| 3. Tampilkan Semester Genap        |")
            print("| 0. Keluar Program                  |")
            print("======================================")
            def DataS():
                frame = pd.DataFrame(data)
                print(frame)
            def SGanjil():
                filteringSganjil()
                input()
                MenuSem()
            def SGenap():
                filteringSgenap()
                input()
                MenuSem()
            inputSem = int(input("Masukan Pilihan :"))
            return DataS() if inputSem==1 else SGanjil() if inputSem==2 else SGenap() if inputSem==3 else main() if inputSem==0 else print("tidak ada pilihan")
        return MenuSem()
    def Matkul():
        clear()
        def menuMatkul():
            clear()
            print("======================================")
            print("         Silahkan Pilih Matkul        ")
            print("======================================")
            print("| 1. Seluruh Data Matkul             |")
            print("| 2. Tugas Akhir 1                   |")
            print("| 3. Tugas Akhir 2                   |")
            print("| 4. Pemrograman WEB                 |")
            print("| 5. Kerja Praktik                   |")
            print("| 6. Kriptografi                     |")
            print("| 7. Metode Numerik                  |")
            print("| 8. Pemro Berbasis Objek            |")
            print("| 9. Sistem Pendukung Keputusan      |")
            print("| 0. Keluar Program                  |")
            print("======================================") 
            def SSData():
                frame = pd.DataFrame(data)
                print(frame)
            def TA1():
                filteringMTA1()
            def TA2():
                filteringMTA2()
            def PWEB():
                filteringMPWeb()
            def KP():
                filteringMKP()
            def kripto():
                filteringMPL()
            def MN():
                filteringMMN()
            def PBO():
                filteringMPBO()
            def Spk():
                filteringMSPK()
            inputM = int(input("Masukan Pilihan :"))
            return SSData() if inputM==1 else TA1() if inputM==2 else TA2() if inputM==3 else PWEB() if inputM==4 else KP() if inputM==5 else kripto() if inputM==6 else MN() if inputM==7 else PBO() if inputM==8 else Spk() if inputM==9 else main() if inputM==0 else print("pilihan tidak ada")
        return menuMatkul()
    def NilaiIPMahasiswa():
        clear()
        def menuNilai():
            clear()
            print("======================================")
            print("       DATA NILAI IP MAHASISWA        ")
            print("======================================")
            print("| 1. Tampilkan Seluruh Nilai Data    |")
            print("| 2. Tampilkan Nilai IP Terbesar     |")
            print("| 3. Tampilkan Nilai IP Terkecil     |")
            print("| 4. Tampilkan Rata-Rata Nilai IP    |")
            print("| 0. Keluar Program                  |")
            print("======================================")
            def SNilaiIP():
                clear()
                frame = pd.DataFrame(data)
                print(frame)
                input()
                menuNilai()
            def SNilaiTB():
                clear()
                def menuNilaiIPIPKB():
                    print("======================================")
                    print("       Silahkan PIlih [IP/IPK]        ")
                    print("======================================")
                    print("| 1. Tampilkan IP                    |")
                    print("| 2. Tampilkan IPK                   |")
                    print("| 0. Keluar Program                  |")
                    print("======================================")
                    def TampilkanIPBesar():
                        filteringIPBesar()
                        input()
                        menuNilai()
                    def TampilkanIPKBesar():
                        filteringIPKBesar()
                        input()
                        menuNilai()
                    inputPil = int(input("Masukan pilihan :"))
                    return TampilkanIPBesar() if inputPil==1 else TampilkanIPKBesar() if inputPil==2 else menuNilai() if inputPil==0 else print("pilihan tidak ada")
                return menuNilaiIPIPKB()
            def SNilaiTK():
                clear()
                def menuNilaiIPIPKK():
                    print("======================================")
                    print("       Silahkan PIlih [IP/IPK]        ")
                    print("======================================")
                    print("| 1. Tampilkan IP                    |")
                    print("| 2. Tampilkan IPK                   |")
                    print("| 0. Keluar Program                  |")
                    print("======================================")
                    def TampilkanIPKecil():
                        filteringIPKecil()
                        input()
                        menuNilai()
                    def TampilkanIPKKecil():
                        filteringIPKKecil()
                        input()
                        menuNilai()
                    inputPil = int(input("Masukan pilihan :"))
                    return TampilkanIPKecil() if inputPil==1 else TampilkanIPKKecil() if inputPil==2 else menuNilai() if inputPil==0 else print("pilihan tidak ada")
                return menuNilaiIPIPKK()
            def RataRataIP():
                pass
            inputPill = int(input("Masukan Pilihan :"))
            return SNilaiIP() if inputPill==1 else SNilaiTB() if inputPill==2 else SNilaiTK() if inputPill==3 else RataRataIP() if inputPill==4 else main()
        return menuNilai()
    def dataTidakada():
        pass
    inputPilihan = int(input("Masukan Pilihan :"))
    return SeluruhData() if inputPilihan==1 else NamaMahasiswa() if inputPilihan==2 else NIMMahasiswa() if inputPilihan==3 else TahunAMahasiswa() if inputPilihan==4 else SemesterMahasiswa() if inputPilihan==5 else Matkul() if inputPilihan==6 else NilaiIPMahasiswa() if inputPilihan==7 else dataTidakada()

main()