import random
import json
import time

with open('creator_id.txt', 'r') as file:
    isi_file = file.read()
    print(isi_file)

time.sleep(2)
for i in range (30):
    print("")
    
isi = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
panjang = 16

while True:
    try : 
        isi_menu = [
            "1. Generate Password",
            "2. Search Password",
            "3. Exit"
        ]
        for i in isi_menu:
            print(i)
        main_menu = (int(input("[INPUT] : ")))
        if main_menu == 1:
            id_gmail = input("Masukkan ID : ")
            for i in range (30):    
                print("")
                
            randomlist = random.sample(isi, panjang)
            randomlist = ''.join(randomlist)


            with open("PLC_PSWD.json", "r") as file:
                data = json.load(file)  

            data[id_gmail] = randomlist

    
            with open("PLC_PSWD.json", "w") as file:
                json.dump(data, file, indent=4)
                
                
            print("ID : ", id_gmail)
            print("PASSWORD : ", randomlist)   
            
            try : 
                print ("Countinue ? Y/n")
                countinue = input("[INPUT] : ")
                if countinue == "Y" or countinue == "y" or countinue == "":
                    for i in range (30):
                        print("")
                    continue
                else:
                    continue
            except ValueError:
                print("EROR : FALSE INPUT")
                
            
                
        elif main_menu == 2:
            
            id_gmail = input("Masukkan ID : ")
            for i in range (30):
                print("")
                
            try:
                with open("PLC_PSWD.json", "r") as file:
                    isi_file_PSWD = json.load(file)  

                if id_gmail in isi_file_PSWD:
                    for i in range (30):
                        print("")
                    print(f"ID : {id_gmail} | PASSWORD : {isi_file_PSWD[id_gmail]}")
                    
                    try:
                        print ("Countinue ? Y/n")
                        countinue = input("[INPUT] : ")
                        if countinue == "Y" or countinue == "y" or countinue == "":
                            for i in range (30):
                                print("")
                            continue
                        else:
                            break
                    except ValueError:
                        print("❌ INPUT SALAH")
                        print("❌ Silahkan coba lagi")
                        
                else:
                    
                    for i in range (30):
                        print("")
                    print("❌ EROR : ID NOT FOUND")
                    time.sleep(3)
                    

            except (FileNotFoundError, json.JSONDecodeError):
                print("❌ File password tidak ditemukan atau rusak!")
        
            try:  
                isi_menu = [
                    "1. Back to Main Menu",
                    "2. Exit"
                ]
                for i in isi_menu:
                    print(i)
                
                last_menu = (int(input("[INPUT] : ")))
                if last_menu == 1:
                    continue
                
                elif last_menu == 2:
                    break
                
                else:
                    print("❌ INPUT SALAH")
                    print("❌ Silahkan coba lagi")
            except ValueError:
                print("❌ INPUT SALAH")
                
        elif main_menu == 3:
            print("❌ PROGRAM BERAKHIR")
            break
        
        else:
            print("❌ INPUT SALAH")
            print("❌ Silahkan coba lagi")
            break    
    except ValueError:
        print("EROR : FALSE INPUT")
        print("PLEASE INPUT THE CORRECT NUMBER")
        time.sleep(2)
        for i in range (30):
            print("")

        