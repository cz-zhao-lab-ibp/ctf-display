#!/usr/bin/env python

import numpy
import sys
import matplotlib as mpl
import matplotlib.pyplot as plt


input_file = numpy.load(str(sys.argv[1]))
all_defocus = []
all_ctf = []
paired_value = []

for i in input_file:
    all_defocus.append(i[19])
    all_ctf.append(i[24])

for j, k in zip(all_defocus, all_ctf):
    paired_value.append((j, k))

sorted_paired_value = sorted(paired_value)

len_input = len(input_file)
start_num = round(0.05*len_input)
stop_num = round(0.95*len_input)
mid_num1 = round(0.2*len_input)
mid_num2 = round(0.8*len_input)

sorted_defocus = []
sorted_ctf = []
for l in sorted_paired_value:
    sorted_defocus.append(l[0])
    sorted_ctf.append(l[1])

low_avg_defocus = numpy.mean(sorted_defocus[start_num:mid_num1])
high_avg_defocus = numpy.mean(sorted_defocus[mid_num2:stop_num])

low_avg_ctf = numpy.mean(sorted_ctf[start_num:mid_num1])
high_avg_ctf = numpy.mean(sorted_ctf[mid_num2:stop_num])


plt.figure()

plt.subplot(121)
plt.scatter(sorted_defocus[start_num:mid_num1],
            sorted_ctf[start_num:mid_num1], s=2)
plt.title('Low Defocus:'+str(round(sorted_defocus[start_num]))+' to '+str(
    round(sorted_defocus[mid_num1])), fontsize='medium')
plt.text(numpy.min(sorted_defocus[start_num:mid_num1]), numpy.max(
    sorted_ctf[start_num:mid_num1]), 'Average CTF fit: '+str(low_avg_ctf))

plt.subplot(122)
plt.scatter(sorted_defocus[mid_num2:stop_num],
            sorted_ctf[mid_num2:stop_num], s=2)
plt.title('High Defocus:'+str(round(sorted_defocus[mid_num2]))+' to '+str(
    round(sorted_defocus[stop_num])), fontsize='medium')
plt.text(numpy.min(sorted_defocus[mid_num2:stop_num]), numpy.max(
    sorted_ctf[mid_num2:stop_num]), 'Average CTF fit: '+str(high_avg_ctf))

plt.show()
