import numpy as np
infile=open('schieramento.txt','r')
Nord = False
Sud= False
Est= False
Ovest= False
tab=[]

for i in infile:
    i=i.rstrip()
    lista=[]
    for c in i:
        lista.append(int(c))
    tab.append(lista)

schieramento=[]

for j in tab:
    if sum(j) != 0:
        schieramento.append(j)

max_liste=[]
for i in schieramento:
    m=max(i)
    max_liste.append(m)
file=max(max_liste)

if 1 not in schieramento[-1]:
    Nord = True

if 1 not in schieramento[0]:
    Sud = True

if not Nord and not Sud:
    sch=[]
    for j in schieramento:
        l=[]
        for k in j:
            if k != 0:
                l.append(k)
        sch.append(l)
    massimo=sch[0]
    for j in range(1, len(sch)-1):
        if len(sch[j]) < len(massimo):
            massimo=massimo
        else:
            massimo=sch[j]
    if massimo[0] > massimo[-1]:
        Est = True
    else :
        Ovest = True
if Nord or Sud :
    #fare trasposta e poi eliminare gli zero
    schieramento_nord_sud = np.transpose(schieramento)
    sch_n_s=[]

    for j in schieramento_nord_sud:
        if sum(j) != 0:
            sch_n_s.append(j)
    sch_s_n = np.transpose(sch_n_s)
    buchi = []
    for j in sch_s_n:
        l = []
        for k in j:
            if k != 0:
                l.append(k)
        buchi.append(l)
    minimo = buchi[0]
    for j in range(1, len(buchi)):
        if len(buchi[j]) < len(minimo):
            minimo=buchi[j]
        else:
            minimo=minimo
    if Sud:
        fila_buchi=minimo[0]
    if Nord:
        fila_buchi=minimo[-1]
    larghezza = len(sch_n_s)

if Est or Ovest:
    sch_o_e=[]
    schieramento_ovest_est=np.transpose(schieramento)
    for j in schieramento_ovest_est:
        if sum(j) != 0:
            sch_o_e.append(j)
    buchi = []
    for j in sch_o_e:
        l = []
        for k in j:
            if k != 0:
                l.append(k)
        buchi.append(l)
    minimo = buchi[0]
    for j in range(1, len(buchi)-1):
        if len(buchi[j]) < len(minimo):
            minimo=buchi[j]
        else:
            minimo=minimo
    if Est:
        fila_buchi=minimo[0]
    if Ovest:
        fila_buchi=minimo[-1]
    larghezza= len(schieramento)

print('larghezza: ', larghezza)
print('numero di file: ', file)

if Nord :
    print ('direzione cardinale = nord')
if Sud :
    print ('direzione cardinale = sud')
if Est :
    print ('direzione cardinale = est')
if Ovest :
    print ('direzione cardinale = ovest')
print('fila con più buchi: ', fila_buchi)
