a=int(input("dati numarul liniei a matricei="))
P=[[int(input()) for i in range(y)] for y in range(a)]
print("Matricea=")
for i in range(len(P)):
    print(P[i])
s1=0
for i in range(0, len(P)):
    s1+=P[i][i]
s2=0
for i in range(0, len(P)):
    s2+=P[len(P)-i-1][i]
print("suma componentelor diagonalei secundare=", s2)
print("suma componentelor diagonalei principale=", s1)
s3=0
for i in P:
    for y in i:
        if P.index(i)<i.index(y):
            s3+=y
print(f"suma componentelor mai sus de diagonala principala=", s3)
s4=0
for i in P:
    for y in i:
        if P.index(i)>i.index(y):
            s4+=y
print(f"suma componentelor mai jos de diagonala principala=", s4)
s5=0
for i in P:
    for y in i:
        if P.index(i)+i.index(y)<y-1:
            s5+=y
print(f"suma componentelor mai sus de diagonala secundara=", s5)
s6=0
for i in P:
    for y in i:
        if P.index(i)+i.index(y)>y-1:
            s6+=y
print(f"suma componentelor mai jos de diagonala secundara=", s6)





