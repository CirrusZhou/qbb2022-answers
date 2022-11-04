#!/usr/bin/env python

import sys

import numpy
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import math

#python load_data2.py dCTCF_full.40000.matrix dCTCF_ontarget_6400_iced.matrix 40000_bins.bed output_file

def main():
    # in1_fname should be ddCTCF
    # in2_fname should be dCTCF
    # bin_fname should be bed file with bin locations
    
    in1_fname, in2_fname, bin_fname, out_fname = sys.argv[1:5]
    data1 = numpy.loadtxt(in1_fname, dtype=numpy.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    #print(data1[0][0]>=54878)
    data2 = numpy.loadtxt(in2_fname, dtype=numpy.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    #print(data2)
    frags = numpy.loadtxt(bin_fname, dtype=numpy.dtype([
        ('chr', 'S5'), ('start', int), ('end', int), ('bin', int)]))

    chrom = b'chr15'
    start = 10400000
    end = 13400000
    start_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                         (frags['start'] <= start) &
                                         (frags['end'] > start))[0][0]]
    end_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                       (frags['start'] <= end) &
                                       (frags['end'] > end))[0][0]] + 1

                                       
    #Filter out data with one or both interaction ends falling outside the desired bin range
    filter_data1_ls=[]
    score1=[]
    for i in data1:
        if i[0] >= start_bin and i[1] <= end_bin:
            #print (i[0])
            #log transform the scores
            i[2]=math.log(i[2])
            #collect all the scores
            score1.append(i[2])
            filter_data1_ls.append(i)

    for m in range(len(filter_data1_ls)):
        #print(filter_data1_ls[m])
        filter_data1_ls[m][2]=filter_data1_ls[m][2]-min(score1)
    #print(len(filter_data1_ls))
    #print(score1)
    
    #filter_data1=numpy.array(filter_data1_ls)

    #create matrix1
    matrix1 = numpy.zeros((72,72))
    print(numpy.shape(matrix1))
    for i in filter_data1_ls:
        x=i[0]-start_bin
        y=i[1]-start_bin
        #print(x,y)
        matrix1[x,y]=i[2]
        matrix1[y,x]=i[2]
        
    #create smoothed matrices before subtracting:


    insulator = []
    for i in range(len(matrix1)):
        if i >=5:
            insulator.append(numpy.mean(matrix1[(i-5):i,i:(i+5)]))

    #plt.plot(insulator)
    #plt.show()
            

    fig, ax = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, figsize=(5,6.25))
    ax[0].imshow(matrix1,vmax=9,cmap='magma')
    ax[0].axis('off')
    plt.margins(x=0)
    ax[1].plot(insulator)
    plt.savefig ( 'insulator.png')

'''
    #plot reference: https://www.geeksforgeeks.org/matplotlib-pyplot-imshow-in-python/
    fig, axes = plt.subplots(nrows=1,ncols=3)
    c=axes[0].imshow(matrix1,vmax=9,cmap='magma')
    d=axes[1].imshow(matrix2,vmax=9,cmap='magma')
    position = fig.add_axes([0.01,0.3,0.03,0.4])
    plt.colorbar(c,cax=position)

    norm=colors.CenteredNorm(vcenter=0,halfrange=0.5)
    e=axes[2].imshow(norm(matrix3),cmap='seismic')

    #define the position for color box. left, down, how wide, how tall
    position2 = fig.add_axes([0.93,0.3,0.03,0.4])
    plt.colorbar(e,cax=position2)


    plt.show()
    plt.savefig ( '3panel.png')
    
    
'''


if __name__ == "__main__":
    main()