
m_tbl=[]

for i in range (1, 11):
    row=[]
    for j in range (1,11):
        row.append(i*j)
    m_tbl.append(row)

for row in m_tbl:
    print(row)


print(*m_tbl, sep='\n') # ērta divdimensiju saraksta izdruka, cikls ir klasika

print(m_tbl[2][5]) # piekļuve elementam

print(m_tbl[2][1:5]) # var arī sagriezt uttt...




