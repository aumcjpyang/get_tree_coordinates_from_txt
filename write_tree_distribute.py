# -*- coding: utf-8 -*-
import re

def info_col(file_name) :
    """returning of longitude, latitude, longitude & latitude,
        tree type, quantity, they are stored as str in lists repectively"""
    
    cdn = re.compile(r"<Point><coordinates>(\d+\.\d+),(\d+\.\d+)</coordinates></Point>")
    tqt = re.compile(r"<name>(\D+)</name>")
    qtt = re.compile(r"<value>(\d+)</value>")
    coord_x = []
    coord_y = []
    coord_xy = []
    tree_type = []
    quant = []
    
    f = open(file_name, 'r', encoding="utf-8")
    for line in f :
        t1 = re.search(cdn, line)
        t2 = re.search(tqt, line)
        t3 = re.search(qtt, line)
        if t1 :
            print("longitude = ",t1.group(1),"\nlatitude = ",t1.group(2))
            coord_x.append(t1.group(1))
            coord_y.append(t1.group(2))
            coord_xy.append([t1.group(1),t1.group(2)])
        elif t2 :
            print("type = ",t2.group(1))
            tree_type.append(t2.group(1))
        elif t3 :
            print("quant = ",t3.group(1),end="\n--------\n")
            quant.append(t3.group(1))
    f.close()
    re.purge()
    return coord_x, coord_y, coord_xy, tree_type, quant

def creat_tree_excel(cd_x, cd_y, tt, qt, file_name) :
    if len(cd_x) == len(tt) :
        if len(cd_x) == len(qt) :
            new_e = open(file_name, 'w', encoding='utf-8')
            for i in range(len(cd_x)) :
                new_e.write(tt[i]+','+cd_x[i]+','+cd_y[i]+','+qt[i]+'\n')
            new_e.close()
        else :
            print('len(cd_x) != len(qt)')
    else :
        print('len(cd_x)!= len(tt)')

if "__main__" == __name__ :
    x,y,xy,tree_t,tree_q = info_col('tree_7.txt')
    creat_tree_excel(x, y, tree_t, tree_q, 'tree_atri_of_7.txt')
