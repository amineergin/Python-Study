import math
#Artık yıl tespit eden fonksiyon
def is_leap(years):
    leap = False
    ust = math.pow(10,5)
    if(years >= 1900 and years <= ust):  
        if(years%400 == 0):
                leap = True
                return leap
        elif(years%4 == 0 and years%100 !=0):
                leap = True
                return leap
        else:
            return leap    
        
#Kullanıcıya selam veren fonksiyon
def print_full_name(first, last):
    # Write your code here
     print("Hello " + first + " " + last + "! You just delved into python.")

#Girilen stringin verilen pozisyondaki değerini verilen karakterle değiştirmek
def mutate_string(string, position, character):
    list_of_string = list(string)
    list_of_string[position] = character
    # string = ''.join(list_of_string)  
    #or
    string = string[:position] + character + string[position+1:]
    return string

#Girilen değer içerisinde istenen değerin kaç kez var olduğunu bulan fonksiyon
def count_substring(string, sub_string):
    result = 0
    girilen_deger = list(string)
    for i in girilen_deger:
        if(i == sub_string):
            result += 1
    return result  
         
a = "AmineHatunErgin"
b = "in"
count_substring(a, b)