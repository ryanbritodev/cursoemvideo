print(""" _   _   __                               
| \ | |_/_/_ _ __ ___   ___ _ __ ___  ___ 
|  \| | | | | '_ ` _ \ / _ \ '__/ _ \/ __|
| |\  | |_| | | | | | |  __/ | | (_) \__ |
|_|_\_|\__,_|_| |_| |_|\___|_|  \___/|___/
 /_/ _ __ ___  _ __   __ _ _ __ ___  ___  
|_ _| '_ ` _ \| '_ \ / _` | '__/ _ \/ __| 
 | || | | | | | |_) | (_| | | |  __/\__ \ 
|___|_| |_| |_| .__/ \__,_|_|  \___||___/ 
              |_|                         """)

soma = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        print(i)
        soma += i
print("\nSOMATÓRIO DOS NÚMEROS: {}".format(soma))
