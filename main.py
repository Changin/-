# -*- coding:utf-8 -*-

def isSafe(string, index):
    flag = 1
    for c in string[index+1:]:
        if c == ')' and flag == 1:
            return True
        elif flag == 0:
            return False
        
        if c in "0123456789":
            continue
        else:
            flag = 0
            return False

while True:
    string = input()
    flg = 0
    index = 0
    str_new = ''
    print()
    for c in string:
        if c == '(':
            if isSafe(string, index):
                flg = 1
                index += 1
                continue
            else:
                str_new += c
                flg = 0
                index += 1
                continue
            
        if c == ')':
            if flg == 0:
                flg = 0
                str_new += c
            flg = 0
            index += 1
            continue
        
        if flg == 1:
            index += 1
            continue
        if flg == 0:
            str_new += c
        
        index += 1
        
    print(str_new)
    print("========================================")
