def near_sym(x, y, s):
    for a, b, id in s:
        if (a-x)**2+(b-y)**2 < 4:
            return id
    return -1


def number(x, d):
    if d[x] in ns:
        i = 1
        while d[x-i] in ns and x-i >= 0:
            i += 1
        start = x-i+1
        i = 1
        while d[x+i] in ns and x+i < len(d)-1:
            i += 1

        return int(d[start:x+i])
    else:
        return 0


with open('aoc23_3b_input.txt') as f:
    data = f.readlines()

ns = [str(i) for i in range(10)]
syms = []
nums = []
y = 0
stars = []
id = 0
for d in data:
    for x in range(len(d)):
        c = d[x]
        if c == '*':
            syms.append([x, y, id])
            id += 1
            stars.append([0, 1])
    y += 1

x, y = 0, 0
sym = near_sym(0, 0, syms)
last = 0
for d in data:
    while x < len(d):
        cislo = number(x, d)
        sym = near_sym(x, y, syms)
        if cislo > 0 and sym >= 0:
            stars[sym][0] += 1
            stars[sym][1] *= cislo
            while number(x, d) > 0:
                x += 1
        else:
            x += 1
    y += 1
    x = 0

sum = 0
for s in stars:
    if s[0] == 2:
        sum += s[1]
print(sum)
# for x, y in syms:
#     q = [False]*8
#     if y > 0:
#         d = data[y - 1]
#         for i in range(3):
#             q[i] = d[x-1+i] in ns
#     if y < len(data)-1:
#         d = data[y + 1]
#         for i in range(3):
#             q[i+3] = d[x - 1 + i] in ns
#     if x > 0:
#         d = data[y]
#         q[6] = d[x-1] in ns
#     if x < len(data[0])-1:
#         d = data[y]
#         q[7] = d[x+1] in ns
#
#     if q[1]:
#         d = data[y-1]
#         while k != -1:
#
#
#     if y != 0:
#
#         if d[x] in ns:
#             i = 1
#             while d[x-i] in ns:
#                 i += 1
#                 end = d.find('.', x)
#                 pn = int(d[x-i+1:end])
#         else:
#             if d[x-1] in ns:
#                 i = 1
#                 while d[x - i] in ns:
#                     i += 1
#                     end = d.find('.', x)
#                     pn = int(d[x - i + 1:end])