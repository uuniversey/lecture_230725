



# 세트 관련 메서드

# my_set1 = {1,2,3}
# my_set2 = {1,2,3}

# my_set1.discard(10) # {1,3}
# print(my_set1) 

# my_set2.remove(10) # error
# print(my_set2)


# my_set = {1,2,3}
# element = my_set.pop()

# print(element) # 1
# print(my_set) # {2, 3}

# a = [
#     {
#         'name' : '삼계탕',
#         'price' : 20000
#     },
#     {
#         'name' : '육전',
#         'price' : 15000
#     }
# ]

# b ={
#     '삼계탕' : 20000,
#     '육전' : 15000,
# }

# print(a,b)
# my_set = {1,'2',3,'9',100,'4',87,'39',10,'52'}

# print(my_set.pop())
# print(my_set.pop())
# print(my_set.pop())
# print(my_set.pop())
# print(my_set.pop())
# print(my_set.pop())
# print(my_set.pop())
# print(my_set.pop())
# print(my_set.pop())
# print(my_set.pop())




# 딕셔너리 관련 메서드


# person = {
#     'name' : 'Alice',
#     'age' : 25
#     }

# other_person = {
#     'name' : 'Jane',
#     'gender' : 'Female'
#     }

# print(my_dict['name'])
# print(my_dict.get['name'])

# print(my_dict['age'])
# print(my_dict.get('age'))
# print(my_dict.get('age', 'Unknown'))



# print(person.keys())
# for key in person.keys():
#     print(key)

# print(person.values())
# for value in person.values():
#     print(value)

# print(person.items())
# for key in person.items():
#     print(key)


# print(person.pop('age'))
# print(person.pop('country', 'country 키는 없지롱'))


# print(person.setdefault('country', 'KOREA'))
# print(person.setdefault('age', '50'))
# print(person.get('age'))
# print(person)


# person.update(other_person)
# person.update(age = 99)
# person.update(lee = 'wj')
# print(person)



'''
혈액형 인원수 세기
결과 => {'A':3, 'B':3, 'O':3, 'AB':3}

blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB','O','A','B','O','B','AB']

1. []

new_dict = {}
for blood_type in blood_types:
    # 기존에 키가 이미 존재하는 경우
    if blood_type in new_dict:
        #기존의 키 값을 +1 증가
        new_dict[blood_type] += 1
    
     # 키가 존재하지 않는 경우 (처음 설정되는 경우)
    else:
        new_dict[blood_type] = 1

print(new_dict)



2. .get()

new_dict1 = {}
for blood_type in blood_types:
    new_dict1[blood_type] = new_dict1.get(blood_type, 0) + 1
    
print(new_dict1)



3. .setdefault()

new_dict2 = {}
for blood_type in blood_types:
    new_dict2.setdefault(blood_type, 0)
    new_dict2[blood_type] += 1
    
print(new_dict2)
'''



# copy

# a = [1,2,3]

# c = a.copy()
# c[0] = 100

# print(a,c)



# # 얕은 복사의 한계
# a = [1, 2, [1, 2]]

# b = a[:]
# b[2][0] = 999 
# print(a,b) # [1, 2, [999, 2]] [1, 2, [999, 2]]
# c = a.copy()
# c[2][0] = 999 
# print(a,c) # [1, 2, [999, 2]] [1, 2, [999, 2]]



# 깊은 복사

# import copy

# original_list = [1, 2, [1,2]]
# deep_copied_list = copy.deepcopy(original_list)

# deep_copied_list[2][0] = 999

# print(original_list, deep_copied_list) # [1, 2, [1, 2]] [1, 2, [999, 2]]


# 별 찍기 -9

# case = int(input())

# for i in range(case):
#     print(' ' * i + '*' * (2*case-(2*(i))-1))

# for i in range(case-1):
#     print(' ' * (case-2-i) + '*' * (2*i + 3))



# 별 찍기 -10

star_list = ['***', '* *', '   ']
x = int(input())
def star(x):
    if x == 3:
            print(star_list[0])
            print(star_list[1])
            print(star_list[0])


    elif x == 9:
        print(star_list[0] * 3)
        print(star_list[1] * 3)
        print(star_list[0] * 3)
        print(star_list[0] + star_list[-1] + star_list[0])
        print(star_list[1] + star_list[-1] + star_list[1])
        print(star_list[0] + star_list[-1] + star_list[0])
        print(star_list[0] * 3)
        print(star_list[1] * 3)
        print(star_list[0] * 3)

    elif x == 27:
        print(star_list[0] * 9)
        print(star_list[1] * 9)
        print(star_list[0] * 9)
        print((star_list[0] + star_list[-1] + star_list[0]) * 3)
        print((star_list[1] + star_list[-1] + star_list[1]) * 3)
        print((star_list[0] + star_list[-1] + star_list[0]) * 3)
        print(star_list[0] * 9)
        print(star_list[1] * 9)
        print(star_list[0] * 9)
        print((star_list[0]) * 3 + (star_list[-1]) * 3 + (star_list[0])* 3)
        print((star_list[1]) * 3 + (star_list[-1]) * 3 + (star_list[1])* 3)
        print((star_list[0]) * 3 + (star_list[-1]) * 3 + (star_list[0])* 3)
        print((star_list[0] + star_list[-1] + star_list[0] + (star_list[-1]* 3) + star_list[0] + star_list[-1] + star_list[0] ))
        print((star_list[1] + star_list[-1] + star_list[1] + (star_list[-1]* 3) + star_list[1] + star_list[-1] + star_list[1] ))
        print((star_list[0] + star_list[-1] + star_list[0] + (star_list[-1]* 3) + star_list[0] + star_list[-1] + star_list[0] ))
        print((star_list[0]) * 3 + (star_list[-1]) * 3 + (star_list[0])* 3)
        print((star_list[1]) * 3 + (star_list[-1]) * 3 + (star_list[1])* 3)
        print((star_list[0]) * 3 + (star_list[-1]) * 3 + (star_list[0])* 3)
        print(star_list[0] * 9)
        print(star_list[1] * 9)
        print(star_list[0] * 9)
        print((star_list[0] + star_list[-1] + star_list[0]) * 3)
        print((star_list[1] + star_list[-1] + star_list[1]) * 3)
        print((star_list[0] + star_list[-1] + star_list[0]) * 3)
        print(star_list[0] * 9)
        print(star_list[1] * 9)
        print(star_list[0] * 9)

    return star_list.pop() 

print (star(x))





# 별 찍기 -11




