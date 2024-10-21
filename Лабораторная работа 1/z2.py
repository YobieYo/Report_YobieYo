# TODO Найдите количество книг, которое можно разместить на дискете
ksran=100
kstrok=50
ksim=25
odin=4
kniga=ksran*kstrok*ksim*odin
all=1.44*1024**2
vsego=int(all/kniga)
print("Количество книг, помещающихся на дискету:", vsego)
