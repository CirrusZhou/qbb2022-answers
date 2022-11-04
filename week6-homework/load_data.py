#!/usr/bin/env python

import sys

import numpy
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import math

#python load_data.py ddCTCF_ontarget_6400_iced.matrix dCTCF_ontarget_6400_iced.matrix dCTCF_ontarget_6400_abs.bed output_file
#python load_data.py ddCTCF_ontarget_6400_iced.matrix dCTCF_ontarget_6400_iced.matrix dCTCF_ontarget_6400_abs.bed output_file

def main():
    # in1_fname should be ddCTCF
    # in2_fname should be dCTCF
    # bin_fname should be bed file with bin locations
    
    in1_fname, in2_fname, bin_fname, out_fname = sys.argv[1:5]
    data1 = numpy.loadtxt(in1_fname, dtype=numpy.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    #print(data1)
    data2 = numpy.loadtxt(in2_fname, dtype=numpy.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    #print(data2)
    frags = numpy.loadtxt(bin_fname, dtype=numpy.dtype([
        ('chr', 'S5'), ('start', int), ('end', int), ('bin', int)]))

    chrom = b'chr15'
    start = 11170245
    end = 12070245
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
        if i[0] >= start_bin & i[1] <= end_bin:
            #log transform the scores
            i[2]=math.log(i[2])
            #collect all the scores
            score1.append(i[2])
            filter_data1_ls.append(i)
    #shift data by subtracting the minimum value so the new minimum value is zero
    for m in range(len(filter_data1_ls)):
        #print(filter_data1_ls[m])
        filter_data1_ls[m][2]=filter_data1_ls[m][2]-min(score1)
        #print(filter_data1_ls[m])
    
    #filter_data1=numpy.array(filter_data1_ls)

    #create matrix1
    matrix1 = numpy.zeros((end_bin-start_bin+1,end_bin-start_bin+1))
    for i in filter_data1_ls:
        x=i[0]-start_bin
        y=i[1]-start_bin
        matrix1[x,y]=i[2]
        matrix1[y,x]=i[2]
        
    #print (matrix1)

    
    
    
    filter_data2_ls=[]
    score2=[]
    for i in data2:
        if i[0] >= start_bin & i[1] <= end_bin:
            i[2]=math.log(i[2])
            score2.append(i[2])
            filter_data2_ls.append(i)
    #print(filter_data2_ls)
    for m in range(len(filter_data2_ls)):
        #print(filter_data2_ls[m])
        filter_data2_ls[m][2]=filter_data2_ls[m][2]-min(score2)
        #print(filter_data2_ls[m])
    #print(filter_data2_ls[:3])
    #create matrix2
    matrix2 = numpy.zeros((end_bin-start_bin+1,end_bin-start_bin+1))
    for i in filter_data2_ls:
        x=i[0]-start_bin
        y=i[1]-start_bin
        matrix2[x,y]=i[2]
        matrix2[y,x]=i[2]


    #create smoothed matrices before subtracting:
    def smooth_matrix(mat):
        N = mat.shape[0]
        invalid = numpy.where(mat[1:-1, 1:-1] == 0)
        nmat = numpy.zeros((N - 2, N - 2), float)
        for i in range(3):
            for j in range(3):
                nmat += mat[i:(N - 2 + i), j:(N - 2 + j)]
        nmat /= 9
        nmat[invalid] = 0
        return nmat

    matrix1=smooth_matrix(matrix1)
    matrix2=smooth_matrix(matrix2)
    #print(matrix1)



    #create difference matrix    
    matrix3 = numpy.zeros((end_bin-start_bin+1,end_bin-start_bin+1))
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            matrix3[i,j] = matrix1[i,j]-matrix2[i,j]

    #remove the distace dependent signal
    def remove_dd_bg(mat):
        N = mat.shape[0]
        mat2 = numpy.copy(mat)
        for i in range(N):
            bg = numpy.mean(mat[numpy.arange(i, N), numpy.arange(N - i)])
            mat2[numpy.arange(i, N), numpy.arange(N - i)] -= bg
            if i > 0:
                mat2[numpy.arange(N - i), numpy.arange(i, N)] -= bg
        return mat2

    matrix3=remove_dd_bg(matrix3)
    #matrix3=smooth_matrix(matrix3)

    #plot reference: https://www.geeksforgeeks.org/matplotlib-pyplot-imshow-in-python/
    fig, axes = plt.subplots(nrows=1,ncols=3)
    c=axes[0].imshow(-matrix1, cmap='magma', vmax=0)
    d=axes[1].imshow(-matrix2, cmap='magma', vmax=0)
    position = fig.add_axes([0.01,0.3,0.03,0.4])
    plt.colorbar(c,cax=position)

    norm=colors.CenteredNorm(vcenter=0,halfrange=0.5)
    e=axes[2].imshow(norm(matrix3),cmap='seismic')

    #define the position for color box. left, down, how wide, how tall
    position2 = fig.add_axes([0.93,0.3,0.03,0.4])
    plt.colorbar(e,cax=position2)


    #plt.show()
    plt.savefig ( '3panel.png')
    
    



if __name__ == "__main__":
    main()