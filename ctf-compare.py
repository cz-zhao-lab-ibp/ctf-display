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
fit1_lst = []
fit2_lst = []
fit1_lst_range1 = []
fit2_lst_range1 = []

for all_value in combined_lst:
    defocus_val.append(all_value[1])
    delta_def.append(all_value[4]-all_value[2])
    fit1_lst.append(all_value[2])
    fit2_lst.append(all_value[4])
    if abs(all_value[4]-all_value[2]) < 1:
        fit1_lst_range1.append(all_value[2])
        fit2_lst_range1.append(all_value[4])

def_range = len(defocus_val)
start_num = round(0.05*def_range)
stop_num = round(0.95*def_range)

ctf1_np=numpy.array(fit1_lst)
ctf1_np_range1=numpy.array(fit1_lst_range1)

ctf2_np=numpy.array(fit2_lst)
ctf2_np_range1=numpy.array(fit2_lst_range1)

mean_ctf1 = numpy.mean(ctf1_np)
mean_ctf2 = numpy.mean(ctf2_np)
delta_ctf = ctf2_np - ctf1_np

mean_ctf1_range1 = numpy.mean(ctf1_np_range1)
mean_ctf2_range1 = numpy.mean(ctf2_np_range1)
delta_ctf_range1 = ctf2_np_range1 - ctf1_np_range1

neg_ctf = sum([int(x<0) for x in delta_ctf])
neg_ctf_range1 = sum([int(y<0) for y in delta_ctf_range1])


print("Input file 1:")
print("Mean CTF: ", mean_ctf1)
print("Mean CTF (Extrema elimination): ", mean_ctf1_range1)

print("\nInput file 2:")
print("Mean CTF: ", mean_ctf2)
print("Mean CTF (extrema elimination): ", mean_ctf2_range1)

print("\nInput file 2 - file 1 differences")
print("Negative is better")
print("Delta mean CTF: ", mean_ctf2-mean_ctf1)
print("Delta mean CTF (extrema elimination): ",
      mean_ctf2_range1-mean_ctf1_range1)

print("\nFiles count:", len(ctf1_np))
print("Negative delta CTF: ", neg_ctf)
print("Negative delta CTF (extrema elimination): ", neg_ctf_range1)


plt.figure()

plt.scatter(defocus_val[start_num:stop_num],
            delta_def[start_num:stop_num], s=2)
# plt.plot([defocus_val[start_num], defocus_val[stop_num]],
#          [1, 1], linewidth=0.8, color='black')
# plt.plot([defocus_val[start_num], defocus_val[stop_num]],
#          [-1, -1], linewidth=0.8, color='black')

plt.xlabel("Defocus (A)")
plt.ylabel("Delta CTF fit (A)")
plt.ylim(-1,1)

plt.show()
