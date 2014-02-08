# -*- coding: utf-8 -*-
#création tableaux+ variables

#formation des tableaux
tab=[];
temptab=[];
def createTab(nombreCase):
    for i in range(nombreCase):
        tab.append([]);
        temptab.append([]);
        for j in range(nombreCase):
            tab[i].append([]);
            temptab[i].append([]);
            for k in range(nombreCase):
                tab[i][j].append(0);
                temptab[i][j].append(0);

def live(i,j,k):
    tab[i][j][k] = 1

def die(i,j,k):
    tab[i][j][k] = 0

def generation(nombreCase):
    for i in range(nombreCase):
        for j in range(nombreCase):
            for k in range(nombreCase):
                sum = 0
                for tempi in range(i-1,i+2):
                    if tempi>=0 and tempi<nombreCase:
                        for tempj in range (j-1,j+2):
                            if tempj>=0 and tempj<nombreCase:
                                for tempk in range (k-1,k+2):
                                    if tempk>=0 and tempk <nombreCase:
                                        sum = sum + tab[tempi][tempj][tempk];
                sum = sum - tab[i][j][k];
                if sum == 3 or (sum==2 and tab[i][j][k]):
                    temptab[i][j][k]=1;
                else:
                    temptab[i][j][k]=0;
    for i in range(nombreCase):
        for j in range(nombreCase):
            for k in range(nombreCase):
                tab[i][j][k]=temptab[i][j][k];
