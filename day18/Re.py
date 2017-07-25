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


ip_list = ['192.168.10.1','192.168.10.2','192.168.10.3','10.10.10.1','192.168.11.1']

input_ip = input("Enter IP: ")
a = re.findall('\d{1,3}',input_ip)
for i in ip_list:
    b = re.findall('\d{1,3}',i)
    # print(len(set(b).difference(a)))
    if len(a) == 4:
        if len(set(a).difference(b)) == 0:
            print(i)
    elif len(a) == 3:
        if len(set(b).difference(a)) == 1 and len(set(a).difference(b)) == 0:
            print(i)
    elif len(a) == 2:
        if len(set(b).difference(a)) <= 2 and len(set(a).difference(b)) <= 1:
            print(i)
    elif len(a) == 1:
        if a[0] == b[0]:
            print(i)
    elif len(a) == 0:
        print(i)
