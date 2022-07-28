#!/usr/bin/python

"""
Output lines selected randomly from a file

Copyright 2005, 2007 Paul Eggert.
Copyright 2010 Darrell Benjamin Carbajal.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

Please see <http://www.gnu.org/licenses/> for a copy of the license.

$Id: randline.py,v 1.4 2010/04/05 20:04:43 eggert Exp $
"""

import random, sys
import argparse
#import string

class shuf:
    def __init__(self, filename):
        f = open(filename, 'r')
        self.lines = f.readlines()
        f.close()

    def chooseline(self):
        return random.choice(self.lines)

def main():
    version_msg = "%prog 2.0"
    usage_msg = """%prog [OPTION]... FILE

Output randomly selected lines from FILE."""

    #parser = OptionParser(version=version_msg,
    #                      usage=usage_msg)
    #parser.add_option("-n", "--numlines",
    #                  action="store", dest="numlines", default=1,
    #                  help="output NUMLINES lines (default 1)")
    #options, args = parser.parse_args(sys.argv[1:])

    parser = argparse.ArgumentParser(prog="shuf")
    
    #echo: takes from stdin, anything separated by whitespace is considered a diff line
    parser.add_argument('--echo','-e', nargs = '*', action='append', dest='echo_args', help="Treat each command-line operand as an input line.")

    #input range
    #since the range is 'a-b' no whitespaces, should  nargs=1 and then i isolate a and b?
    parser.add_argument('--input-range', '-i', action='append', dest='irange', nargs=1, help= 'Act as if input came from a file containing the range of unsigned decimal integers lo…hi, one per line.')

    #head count
    parser.add_argument('--head-count', '-n', nargs=1, action='store', dest='hcount', type=int, help='Output at most count lines. By default, all input lines are output.')

    #repeat
    parser.add_argument('--repeat', '-r', action='store_true', dest='repeat', help='Repeat output values, that is, select with replacement. With this option the output is not a permutation of the input; instead, each output line is randomly chosen from all the inputs. This option is typically combined with --head-count; if --head-count is not given, shuf repeats indefinitely.')

    #help
    #parser.add_argument('--help', action='store_true', dest='needhelp', help= 'provides help')

    #take stdin (-)
    #parser.add_argument('-', action='store_true', dest='takestdin', default= not None, help='reads from stdin')

    #work with files
    parser.add_argument('file', action='store', nargs='?')

    options = parser.parse_args()
   # print(options)

    # if someone runs shuf without any options, are their destination variables initialized?
    # so would these come up as compilation errors?
    # if they are uninitialized, I should use try instead right?
    # how can i make hcount work as a flag, but also store value?

           # TF
           # TT
           # FT
           # FF

          # F R
          # F H
          # F
           
    #file or stdin
    #if (options.standard is not None):
     #   if (options.repeat):
            
    #potential echo inputs
    if options.echo_args is not None:
        lines = options.echo_args
        #to test
        #print("echo was used")
        #print(lines[0])
        if options.irange is not None:
            print("shuf: cannot combine -e and -i options")
            return
        if (options.hcount is not None) and (not options.repeat):
            #choose random element from echo_args. Output at most hcount lines
            if options.hcount[0] > len(options.echo_args[0]):
                for i in range(len(options.echo_args[0])):
                    a = random.choice(lines[0])
                    print(a)
                    lines[0].remove(a)
                return
            else:
                for i in range(options.hcount[0]):
                    a = random.choice(lines[0])
                    print(a)
                    lines[0].remove(a)
                return
        if (options.hcount is not None) and (options.repeat):
            #choose random element from echo_args with replacement. Output at most hcount lines
            for i in range(options.hcount[0]):
                a = random.choice(lines[0])
                print(a)
            return
        if (options.hcount is None) and (options.repeat):
            #choose random element from echo_args with replacement: GOES INDEFINITELY
            while len(lines[0]) != 0:
                print(random.choice(lines[0]))
            return
        if (options.hcount is None) and (not options.repeat): #when we arent doing hcount, not repeating ONLY -e
            while len(lines[0]) != 0:
                a = random.choice(lines[0])
                print(a)
                lines[0].remove(a)
            return
        
    if options.irange is not None:
        #first dismantle narg
        #print(options.irange[0][0])
        if (options.file is not None):
            print("extra operand")
            return
        parts = options.irange[0][0].split("-")
        if len(parts) != 2:
            print('bad input')
            return

        #get a and b, make a list of all numbers between them (inc)
        a = int(parts[0])
        b = int(parts[1])
        numbers = list(range(a,b+1))

        #print(a)
        #print(b)
        #print(numbers)
        #error catching
        if (options.echo_args is not None):
            print("shuf: cannot combine -e and -i options")
            return
        if a > b:
            print('bad input')
            return
        elif (options.hcount is None) and (not options.repeat): #basic case
            for i in range(len(numbers)):
                num = random.choice(numbers)
                print(num)
                numbers.remove(num)
            return
        elif (options.hcount is not None) and (options.repeat): #only print hcount lines with repetition
            for i in range(options.hcount[0]):
                print(random.choice(numbers))
            return
        elif (options.hcount is not None ) and (not options.repeat): #only print hcount lines, no repetition
            for i in range(options.hcount[0]):
                num = random.choice(numbers)
                print(num)
                numbers.remove(num)
            return
        elif (options.hcount is None) and (options.repeat): #no hcount, yes repeat, goes indef
            while len(numbers) != 0:
                print(random.choice(numbers))
            return


    #first prompt for input
    if (options.file is not None and options.file != '-'):
        inlist = open(options.file, 'r').read().splitlines()
    else:
        inlist = []
        for line in sys.stdin:
            a = line.replace('\n', '')
            inlist.append(a)
    #print(inlist)
    #basic case
    if (options.hcount is None) and (not options.repeat):
        #print("hi1")
        for i in range(len(inlist)):
            a = random.choice(inlist)
            print(a)
            inlist.remove(a)
        return
    #with repetition, no hcount: indefinite
    if (options.hcount is None) and (options.repeat):
        #print("hi2")
        while len(inlist) != 0:
            print(random.choice(inlist))
        return
    #with repetition and hcount
    if (options.hcount is not None) and (options.repeat):
        #print("hi3")
        for i in range(options.hcount[0]):
            print(random.choice(inlist))
        return
    #with hcount, no repetition
    if (options.hcount is not None) and (not options.repeat):
        #print("hi4")
        #when there is more hcount than lines
        if (options.hcount[0]) > len(inlist):
            for i in range(len(inlist)):
                a = random.choice(inlist)
                print(a)
                inlist.remove(a)
            return
        else: #when there are more lines than hcount
            for i in range(options.hcount[0]):
                a = random.choice(inlist)
                print(a)
                inlist.remove(a)
            return
    '''
    # if it is just HC and nothing else except repeat
    if (options.hcount is not None) and (options.echo_args is None) and (options.irange is None):
        if (options.file is not None):
            inlist2 = open(options.file, 'r').read().splitlines()
            #print(inlist2)
        else:
            inlist2 = []
            for line in sys.stdin:
                a = line.replace('\n', '')
                #print(inlist2)
                inlist2.append(a)
        #for just basic hc
        if (not options.repeat):
            if (options.hcount[0]) > len(inlist2):
                for i in range(len(inlist2)):
                    a = random.choice(inlist2)
                    print(a)
                    inlist2.remove(a)
                return
            else: #when there are more lines than hcount
                for i in range(options.hcount[0]):
                    a = random.choice(inlist2)
                    print(a)
                    inlist2.remove(a)
                return
        #for just hc and rep
        if (options.repeat):
            for i in range(options.hcount[0]):
                a = random.choice(inlist2)
                print(a)
            return

     #for just repeat by itself
    if (options.repeat) and (options.hcount is None) and (options.echo_args is None) and (options.irange is None) and (options.file != '-'):
        if (options.file is not None):
            inlist3 = open(options.file, 'r').read().splitlines()
            #print(inlist3)
        else:
            inlist3 = []
            #get input
            for line in sys.stdin:
                a = line.replace('\n', '')
                #print(inlist3)
                inlist3.append(a)
        while len(inlist3) != 0:
            print(random.choice(inlist3))
        return
        '''
        
if __name__ == "__main__":
    main()
