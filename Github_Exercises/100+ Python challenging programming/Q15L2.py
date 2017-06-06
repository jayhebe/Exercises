# num = int(input())
# print(str(num + num * 11 + num * 111 + num * 1111))

a = input()
n1 = int("%s" % a)
n2 = int("%s%s" % (a, a))
n3 = int("%s%s%s" % (a, a, a))
n4 = int("%s%s%s%s" % (a, a, a, a))

print(n1 + n2 + n3 + n4)