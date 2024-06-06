import os
import string

# 1a
def file_line_len(fpath):    
    file=open(fpath, encoding='utf-8')
    texta_rindas=file.readlines()
    file.close()

    return len(texta_rindas)
    
pp='nod_12\\veidenbaums.txt'

print(f"1a - Rindu skaits datnē: {file_line_len(pp)}")

# 1b
def get_poem_lines(fpath):
    file=open(fpath, encoding='utf-8')
    texta_rindas=file.readlines()
    file.close()

    poemas_rindas=[]
    for rinda in texta_rindas:
        if rinda !="\n":
            if rinda[-4:] != "***\n":
                poemas_rindas.append(rinda)

    return poemas_rindas

print(f"1b - Dzejas rindu skaits datnē: {get_poem_lines(pp)}")

# 1c

def save_lines(destpath, lines):
    outputf=destpath

    write_lines=[]

    for line in lines:
        write_lines.append(line)

    with open(outputf, mode="w", encoding='utf-8') as file:
        file.writelines(write_lines)

kur="nod_12\\lines.txt"

save_lines(kur, "testa rinda 2")

# 1d
save_lines("nod_12\\veidenbaums_poems.txt", get_poem_lines(pp))

# 1e
def clean_punkts(srcpath,destpath):

    with open(srcpath, encoding='utf-8') as file:
        text_lines = file. readlines()

    clean_lines=[]
    for line in text_lines:
        clean_line=""
        for ch in line:
            if ch not in string.punctuation:
                clean_line+=ch
        clean_lines.append(clean_line)

    save_lines(destpath, clean_lines)

clean_punkts("nod_12\\veidenbaums_poems.txt","nod_12\\veidenbaums_no_punkts.txt")



