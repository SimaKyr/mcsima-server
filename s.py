import os.path
import urllib.request
from urllib.request import Request, urlopen
import subprocess
import sys
import base64

def decB64(i):
    base64_string = i
    base64_bytes = base64_string.encode("ascii")

    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    return sample_string
configFile = "YmVkcm9jazoKICBhZGRyZXNzOiAwLjAuMC4wCiAgcG9ydDogMTkxMzIKICBjbG9uZS1yZW1vdGUtcG9ydDogZmFsc2UKICBtb3RkMTogIlBST1NUTyBTSU1BS1lSIgogIG1vdGQyOiAiU0lNQUtZUiBUWVQiCiAgc2VydmVyLW5hbWU6ICJUWVQgTkVUIFNJTUFLWVJBIgpyZW1vdGU6CiAgYWRkcmVzczogYXV0bwogIHBvcnQ6IDI1NTY1CiAgYXV0aC10eXBlOiBvZmZsaW5lCmNvbW1hbmQtc3VnZ2VzdGlvbnM6IHRydWUKcGFzc3Rocm91Z2gtbW90ZDogdHJ1ZQpwYXNzdGhyb3VnaC1wcm90b2NvbC1uYW1lOiBmYWxzZQpwYXNzdGhyb3VnaC1wbGF5ZXItY291bnRzOiB0cnVlCmxlZ2FjeS1waW5nLXBhc3N0aHJvdWdoOiBmYWxzZQpwaW5nLXBhc3N0aHJvdWdoLWludGVydmFsOiAzCm1heC1wbGF5ZXJzOiAyCmRlYnVnLW1vZGU6IGZhbHNlCmdlbmVyYWwtdGhyZWFkLXBvb2w6IDMyCmFsbG93LXRoaXJkLXBhcnR5LWNhcGVzOiB0cnVlCmFsbG93LXRoaXJkLXBhcnR5LWVhcnM6IGZhbHNlCnNob3ctY29vbGRvd246IHRydWUKY2FjaGUtY2h1bmtzOiB0cnVlCmNhY2hlLWltYWdlczogMAphYm92ZS1iZWRyb2NrLW5ldGhlci1idWlsZGluZzogZmFsc2UKZm9yY2UtcmVzb3VyY2UtcGFja3M6IHRydWUKeGJveC1hY2hpZXZlbWVudHMtZW5hYmxlZDogdHJ1ZQptZXRyaWNzOgogIGVuYWJsZWQ6IGZhbHNlCiAgdXVpZDogODVmOTYzNzAtY2U0ZC00OGRiLWI2OGUtZTNlMjZjZGU0ODhmCnNjb3JlYm9hcmQtcGFja2V0LXRocmVzaG9sZDogMjAKZW5hYmxlLXByb3h5LWNvbm5lY3Rpb25zOiBmYWxzZQp1c2UtYWRhcHRlcnM6IHRydWUKCmNvbmZpZy12ZXJzaW9uOiA0Cg=="
dbg = False
debugWindows = False

print("Программа по подключению к серверу Майнкрафт")
print("Создал:   SimaKyr.")
print("\n")

stPgFile = 'installed_yn'

if(len(sys.argv) == 2):
    if(sys.argv[1] == "h"):
        print("Привет! Что требуем:")
        print("1 - Сброс параметров")
        print("2 - Режим отладки")
        print("3 - Режим максимальной отладки")
        print("\n")
        i = str(input("Введите число:"))
        if(i == "1"):
            if(os.path.exists(stPgFile)):
              os.remove(stPgFile)
            print("Сбросено! Продолжаем обычное выполнение...")
        if(i == '2'):
            dbg = True
            print("Вкючили режим отладки! Продолжаем обычное выполнение...")
        if(i == '3'):
            dbg = True
            debugWindows = True
            print("Вкючили полный режим отладки! Продолжаем обычное выполнение...")
urlGC = 'http://ci.nukkitx.com/job/GeyserMC/job/Geyser/job/master/lastSuccessfulBuild/artifact/bootstrap/standalone/target/Geyser.jar'

stPg = False

logo = "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW#+=WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@+++=WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW+++++=WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*+++++*=WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW=++++****=WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW#++++*****:=WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@++++****+:::=WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*+++****+:::::=WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*+++****+:::::::=WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW=+++****+++::::::+WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW#+++****+++++::::#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@+++****+++++++:*@WW*#WWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*+:+***++++++++#@@#+:+#WWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWW@=+::***+++++++*@@@*++:++@WWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWW@#+::+**+++++++#@@=++++:+++@WWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWW@:::+**++++++*@@@*+++++:++++@WWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWW@+:::**++++++#@@=+++++++:+++++WWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWW*:::+*+++++*@@#***++++++::++++*WWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWW=::::*+++++#@@@@**+++++++::+++++*WWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWW#::::+++++*@@@@@@@@*++++++:::+++++*WWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWW@:::::*+++#@@@@@@@@@@@*++++::::+++++=WWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWW+::::+***@@@@@@@@@@@@@W@*++:::+++++++=WWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWW*:::::**#WW@@@@@@@@@@WWWWWW=:::++++++++#WWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWW=:::::+=WWWWWWWW@@@WWWWWWWWWWW=:+++++++++#WWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWW@::::::@WWWWWWWWWWWWWWWW@@@@@@##@=+++++++++@WWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWW:::::::::::::::::::::::::+++=@WWWWW#*****+++@WWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWW+::::::::::::::::+++++++*#WWWWWWWWWWWW#****+++@WWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWW=::::::::++********+*=@WWWWWWWWWWWWWWWWWW#***+:+WWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWW#++***************#WWWWWWWWWWWWWWWWWWWWWWWWW#==*:+WWWWWWWWWWWWW\nWWWWWWWWWWWWWWWW=************=@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW#==+*WWWWWWWWWWWW\nWWWWWWWWWWWWWWW=*********#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW#=**WWWWWWWWWWW\nWWWWWWWWWWWWWW#*****=@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW#==WWWWWWWWWW\nWWWWWWWWWWWWW@**#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW##WWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\n"
def split_host_port(string):
    if not string.rsplit(':', 1)[-1].isdigit():
        return (string, None)

    string = string.rsplit(':', 1)

    host = string[0]  # 1st index is always host
    port = str(string[1])

    return (host, port)
def main():
    print(logo)
    print("Приветствую вас!")
    if(dbg):
        print("Проверяем установлена ли данная программа...")
    print("Введите адрес сервера MINECRAFT: JAVA EDITION.")
    print("Он должен выглядить так *.tcp.ngrok.io:*****")
    ip = str(input("Адрес сервера:"))
    if(dbg):
        print("Запись новых параметров...")
    cfg = decB64(configFile)
    cfg = cfg.replace("auto", split_host_port(ip)[0]).replace("25565", split_host_port(ip)[1])

    f = open("config.yml", "w", encoding='utf-8')
    f.write(cfg)
    f.close()
    print("Запуск...")
    subprocess.call("java -jar geysermc.jar")
if(os.path.exists(stPgFile)):
    if(dbg):
        print("Программа уже установлена! Отлично!")
    stPg = True
    main()
else:
    if(dbg):
        print("Программа не установлена )-: Начинаем установку...")

    print("Начием скачивать установщик JAVA...")
    with urllib.request.urlopen('http://raw.githubusercontent.com/MasterDevX/java/master/installjava') as f:
        html = f.read().decode('utf-8')
        f = open("installjava", "w", encoding='utf-8')
        f.write(html)
        f.close()

        st = os.stat('installjava')
        os.chmod('installjava', st.st_mode | stat.S_IEXEC)

        print("JAVA установщик скачан. Устанавливаем JAVA...")
        if(not debugWindows):
            subprocess.call("./installjava")
        print("Скачиваем сервер GeyserMC...")

        req = Request(urlGC, headers={'User-Agent': 'Mozilla/5.0'})

        f = open("geysermc.jar", "wb")
        f.write(urlopen(req).read())
        f.close()

        print("Установка успешно завершена!")
        f = open(stPgFile, "a")
        f.write("Привет! Этот файл не удалять \(-:")
        f.close()
        print("Для повторного запуска используй")
        print("py s.py")
        print("Перезапуск...")
        main()
