#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "jupiter2018"

import sys

def main(args):
    """Add your code here"""
    if len(sys.argv) != 2:
        print 'Please add a filename as a second argument'
        sys.exit(1)
    filename = sys.argv[1]
    print(filename)
    fileToOpen = open(filename)
    fileToWrite = open("output.txt", "a")
    charDict={">":"<","]":"[","}":"{","*)":"(*",")":"("} 
    for line in fileToOpen:
        if(line.isspace()):
            break
        #print(line)
        openChar = []
        num = 0
        count=0
        while(num < len(line)):
                if line[num] in "(<[{":
                    if line[num+1] == "*" and line[num]=="(":
                       openChar.append("(*")
                       num = num + 2
                       
                    else:
                        openChar.append(line[num])
                        num +=1
                    count +=1
                    # print(openChar)  
                elif line[num] in ">}]*)":
                    if line[num]=="*" and line[num+1]==")":
                        
                        curChar = "*)"
                        num += 2
                    elif(not line[num] == "*"):
                        curChar = line[num]
                        num +=1
                    else:
                        count += 1
                        num += 1
                        continue
                    count += 1    
                    
                    if openChar[-1] == charDict[curChar]:
                        # print(curChar, num)
                        openChar.pop(-1)
                    else:
                        fileToWrite.write("NO "+str(count)+"\n")
                        break
                else:
                    num += 1
                    count += 1
        # print(openChar)  
        
        if(not openChar):
            fileToWrite.write("YES\n")
        elif(openChar and len(line)== count):
            fileToWrite.write("NO "+str(count)+"\n")
        

            
              
    
    

if __name__ == '__main__':
    main(sys.argv)
