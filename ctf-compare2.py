#!/usr/bin/env python

import numpy
import sys
import re
import matplotlib as mpl
import matplotlib.pyplot as plt

input_file1 = numpy.load(str(sys.argv[1]))
input_file2 = numpy.load(str(sys.argv[2]))

file1_lst = []
file2_lst = []

for i in input_file1:
    file1_lst.append((re.findall(r'/(.+?)\'', str(i[1])), i[19], i[24]))

for j in input_file2:
    file2_lst.append((re.findall(r'/(.+?)\'', str(j[1])), j[19], j[24]))

file1_lst.sort()
file2_lst.sort()

combined_lst_temp = []
for m in file1_lst:
    for n in file2_lst:
        if m[0] == n[0]:
            combined_lst_temp.append((m[0], m[1], m[2], n[1], n[2]))
combined_lst = sorted(combined_lst_temp, key=lambda x: x[1])

defocus_val = []
delta_def = []
for all_value in combined_lst:
    defocus_val.append(all_value[1])
    delta_def.append(abs(all_value[4]-all_value[2]))

def_range = len(defocus_val)
start_num = round(0.05*def_range)
stop_num = round(0.95*def_range)
mid_num1 = round(0.2*def_range)
mid_num2 = round(0.8*def_range)

plt.figure()

plt.subplot(121)
plt.scatter(defocus_val[start_num:mid_num1],
            delta_def[start_num:mid_num1], s=2)
plt.xlabel("Defocus (A)")
plt.ylabel("Delta Defocus (A)")

plt.subplot(122)
plt.scatter(defocus_val[mid_num2:stop_num], delta_def[mid_num2:stop_num], s=2)
plt.xlabel("Defocus (A)")
plt.ylabel("Delta Defocus (A)")

plt.show()
