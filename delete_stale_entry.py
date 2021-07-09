#!/usr/bin/python3.6
import datetime                                 #for getting data and time
starttime_time = datetime.datetime.now()

import os                                       #for moving into different directory and folder

print("...........................READ ME..............................")
print("First line of LINK_ID raw data MUST contain link ID")
print("FIRST line cannot be EMPTY or any other character EXCEPT LINK ID")
print("LAST line MUST be EMPTY, new line")

print("working directory is ", os.getcwd())
# print(os.listdir('.'))

#zz, hh are defined as ARRAY/LIST


###............###........OPEN FILE TO READ LINK DATA........###............###
raw_link_id = open('link.txt','r')
s = raw_link_id.readlines()
raw_link_id.close()
print ("\nTotal line count is                                   ", len(s)); print(type(s))
#v1=s[0]; print(type(v1))
#if v1.find("link.nstanca"):print("YES")
#v2=(s[len(s)-3])
#if v2.find("network_jrp"):print("YES")
#v3=(s[len(s)-2]);
#if v3.find("network_jrp"):print("YES")
#v4=(s[len(s)-1]);
#if v4=="\n":print("YES")

#if v1.find("link.nstance") and v2.find("network_jrp") and v3.find("network_jrp") and v4=="\n": print("DATA validation OK")

# ###............###........WRITE customer_listON 1D ARRAY........###............###

###............###........DECLEARE zz AS AN ARRAY........###............###
zz = []
duplicate = []
for a in range(0, len(s)):
    #print("value of a is",a)
    y = s[a]
    if a%4 == 0:link_ID = y; #print(a); #print(link_ID)
    elif a%4 == 1: SIDE_A = (y[47:-64]);#print(a); print("SIDE_A is",SIDE_A)
    elif a%4 == 2: SIDE_B = (y[47:-64]);#print(a); print("SIDE_B is",SIDE_B)
    else:
        if SIDE_A == SIDE_B: duplicate.append(link_ID); #print(duplicate)
#ABOVE line will add each duplicate link ID in to new LIST named as "duplicate"
#    print("value of a is",a)#print(len(s));print(type(y))

    zz.append(y)
output = ''.join(duplicate)
print(*duplicate, sep=' ')
#print(output); #print(type(output))
print("count of duplicate entry is",len(duplicate))
#    print(zz)

del zz
del duplicate



endtime_time = datetime.datetime.now()
print("Total processing time: {}".format(endtime_time - starttime_time))


