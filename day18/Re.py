import re
#
# a = re.findall('w..l','hello world')
#
# print(a)

# a = re.findall('h.*o$','refdsfdsfdsfdshello')
# print(a)

# a = re.findall('a.?li','fjdkslfsfoieworujioewuralioioiiouifodsouifdsjklfuieow')
# print(a)

# a = re.findall('[1-9,a-z,A-Z]*','fdsfrejwiofjdsklfjkdslfioewabcdefgsjfkldjfksduio')
# print(a)
# a = re.findall('[^tf]*',"fdsfiewuorjfkldsjifuoeiwjfkoewtewtabctdfjkdslfjiojoewj")
# print(a)

#
# ip_list = ['192.168.10.1','192.168.10.2','192.168.10.3','10.10.10.1','192.168.11.1']
#
# input_ip = input("Enter IP: ")
# a = re.findall('\d{1,3}',input_ip)
# for i in ip_list:
#     b = re.findall('\d{1,3}',i)
#     # print(len(set(b).difference(a)))
#     if len(a) == 4:
#         if len(set(a).difference(b)) == 0:
#             print(i)
#     elif len(a) == 3:
#         if len(set(b).difference(a)) == 1 and len(set(a).difference(b)) == 0:
#             print(i)
#     elif len(a) == 2:
#         if len(set(b).difference(a)) <= 2 and len(set(a).difference(b)) <= 1:
#             print(i)
#     elif len(a) == 1:
#         if a[0] == b[0]:
#             print(i)
#     elif len(a) == 0:
#         print(i)

# a = re.findall(r'Julia\b','Julia is a name of JuliaJia')
# print(a)

# a = re.findall(r'(ac)|3','acacdD:\de')
# print(a)
#
# ret = re.search('(?P<id>\d{3})/(?P<name>\w{3})','weew345/ttt123/ooo')
# print(ret.group())
# print(ret.group("id"))
# print(ret.group("name"))

# ret = re.split('[k,s]','weruirksweruioewr')
# print(ret)
# ret = re.compile('\.com')
# a = "www.google.com"
# print(ret.findall(a))

# calc_input = input("Enter: ")
# calc_input = "((1+3)*4)+2*(4-2*(3-1))"
list1 = ['*','/']
list2 = ['+','-']
result2 = 0
def basic_calc(a,b):
    if len(a) == 2:
        c = float(a[0])
        d = float(a[1])
        if b == '+':
            return c + d
        elif b == '-':
            return c - d
        elif b == '*':
            return c * d
        elif b == '/':
            return c / d
    elif len(a) == 3 and a[0] == '':
        c = float(a[1])
        d = float(a[2])
        if b == '+':
            return c + d
        elif b == '-':
            return c - d
        elif b == '*':
            return c * d
        elif b == '/':
            return c / d
    elif len(a) == 3 and a[2] == '':
        c = float(a[0])
        d = float(a[1])
        if b == '+':
            return c + d
        elif b == '-':
            return c - d
        elif b == '*':
            return c * d
        elif b == '/':
            return c / d




def filter1(a):
    result = 0
    if a != '':
        c = a[len(a) - 1]
        if c in list2:
            ret3 = re.split('[+\-]', a)
            ret4 = re.findall('[+\-]', a)
            # ret5 = re.findall('[^\d]', ret3[0])
            result = basic_calc(ret3, ret4[0])[0]
            return result,c


        elif c in list1:
            ret3 = re.split('[*/]', a)
            ret4 = re.split('[+\-*/]', ret3[0])
            ret5 = re.findall('[^\d]', ret3[0])[0]
            # print(ret5)
            result = float(ret4[0])
            num2 = float(ret4[1])
            return result,num2,ret4[1],c,ret5



calc_input = "1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14)-(-4*3)/(16-3*2))"
ret_init = re.sub(' ','',calc_input)
ret1 = re.sub('(\(\(+)','B',ret_init)
ret2 = re.split('B',ret1)
ret3 = re.sub('\(','A',ret2[1])
ret4 = re.split('A',ret3)
c = []
num = []
if ret2[0][len(ret2[0]) - 1] in list1:
    result1,num1,num2,c2,c1 = filter1(ret2[0])
    num.append(num1)
    num.append(num2)
    c.append(c1)
    c.append(c2)
else:
    result1,c1 = filter1(ret2[0])
    c.append(c1)

for i in ret4:
    num3 = 0
    if ')' in i:
        i_index = ret4.index(i)
        old = re.sub('\)\)+',')',i)
        new = re.split('\)',old)
        ret5 = re.split('[^\d]',new[0])
        ret6 = re.findall('[+\-*/]',new[0])
        print(ret6)
        if ret5[0] == '':
            a = ret5[1]
            ret5[1] = '-%s' % a
            # num4 += basic_calc(ret5,ret6[1])
            # num.append(num4)
            c4 = new[1]
            c.append(c4)
        else:
            pass
    else:
        ret5 = re.split('[^\d]',i)
        ret6 = re.findall('[^\d]',i)
        if ret6[1] in list2:
            num3 += basic_calc(ret5,ret6[0])
            c3 = ret6[len(ret6) - 1]
            # num.append(num3)
            # print(ret6)
            # c.append(c3)
        elif ret6[1] in list1:
            num


# print(ret4)