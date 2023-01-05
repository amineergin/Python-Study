# yakın kampüs - python dersleri #3 Veri tipleri ve Sayı tipleri (integer,float)
# its a dictionary
dict_a = {
        'isim':'amine',
        'yas':21,
        'okul':True,
        'ayakkabinumarasi':36.5
    }

print("dictionary: ", dict_a)
print("next=>>>")
print("dict isim: ", dict_a['isim'])

# its a set
set_a = {1,3.5,True,'Amine'}
print("next=>>>")
print("set: ", set_a)

# its a tuple
tuple_a = (1,'Amine',False,5.5)
print("next=>>>")
print("tuple: ", tuple_a)

# its a list
list_a = [1,5,1,True,False,"Amine","amine",5.5]
print("next=>>>")
print("list: ", list_a)

if(list_a[5] == list_a[6]):
    print("merhaba dünya") 
    # so they are different
