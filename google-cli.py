from googlesearch import search
from colorama import init,Fore,Back
import os


#color 
red = Fore.RED
green = Fore.GREEN
d = Fore.RESET
cyan = Fore.CYAN

def cm(com):
   os.system(com)
cm("clear")

#banner edit yin ma a loe 
banner = f'''{cyan}
██████╗  █████╗ ███╗   ██╗██████╗  █████╗ ██████╗ 
██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔══██╗
██████╔╝███████║██╔██╗ ██║██║  ██║███████║██████╔╝
██╔═══╝ ██╔══██║██║╚██╗██║██║  ██║██╔══██║██╔══██╗
██║     ██║  ██║██║ ╚████║██████╔╝██║  ██║██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝

{d}
'''
#banner edit yin lee pal ya mel m a loe sout pal
print(banner)
q = input(f"{green}𝔾𝕠𝕠𝕘𝕝𝕖 𝕊𝕖𝕒𝕣𝕔𝕙{red} ~# ")
for i in search(query=q,num=20,stop=10):
   print(f"{red}=̶=̶=̶{d}"*20)
   print(f"{green}𝕊𝕚𝕥𝕖 :: {cyan}"+ i + '\n')
