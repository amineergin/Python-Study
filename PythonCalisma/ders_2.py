import math
import os
import random
import re
import sys
import numpy as np


if __name__ == '__main__':
    
    #girilen değerin belirli aralıklarda ve çift olmasına göre ekrana farklı değerler yazdırmak.
    def if_else_fonksiyonu():
        n = int(input().strip())
        if(2<= n <=5 and n%2==0):
            print("Not Weird")
        elif(6<= n <=20 and n%2==0):
            print("Weird")
        elif(n> 20 and n%2==0):
            print("Not Weird")    
        else:
            print("Weird")  
    
    #Virgüllü sayının virgülden sonraki basamak sayısını belirlemek.
    #round içerisine bir sayı bir de değer alır, eğer hiçbir değer girilmezse sayıyı en yakın tam sayıya yuvarlar
    # eğer bir değer girilirse virgülden sonra girilen değer kadar basamak alır.
    def basamak_sayisini_belirt():     
        a = int(input())
        b = int(input())
        sayi1 = a/b
        # sayıyı en yakın tam sayıya yuvarlamak
        result1 = round(sayi1)
        sayi2 = a/b
        # virgülden sonra 5 basamak almak
        result2 = round(sayi2,5)
        print("a//b = ", result1)
        print("a/b = ",result2)
    
    # Girilen sayıya kadar olan bütün sayıların karesini alan fonksiyon
    def kare_al():        
        x = int(input())   
        if(1<= x <= 20):
            for i in range(x):
                result = i*i
                print(result)
    # Girilen değere kadar olan bütün sayıları yanyana yazdıran fonksiyon 
    def sayilari_birlestir():   
        x = int(input()) 
        if(1<= x <= 150):
            for i in range(x):
                i= i+1
                print(i,end="")
    
    def array_fonksiyonu():
        np.set_printoptions(legacy='1.13')
        
        array = np.array(input().split(), float)
        functions = [np.floor, np.ceil, np.rint]
        
        for fn in functions:
            print(fn(array))
            
    
    n = int(input())
    arr = np.array(int, input().split())
    sorted_array = arr.sort(reverse=True)
    print(sorted_array)
 
