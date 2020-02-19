#!/usr/bin/python

import sys




def rock_paper_scissors(n):
  plays = ['rock', 'paper', 'scissors']
  # Multiple recurssive calls so that each call can 
  # add to the result.
  # if n == 0:
  #   return [[]]
  # if n == 1:
  #   #list length can only be 1 + 1 + 1
  #   return [[plays[0]]] + [[plays[1]]] + [[plays[2]]]
  # if n == 2:
  #   #list length can only be 2 + 2 + 2
  #   print( [[plays[0]] + [plays[0]]] + [[plays[1]] + [plays[1]]] + [[plays[2]] + [plays[2]]] + [[plays[0]] + [plays[1]]] + [[plays[0]] + [plays[2]]] + [[plays[1]] + [plays[2]]] + [[plays[1]] + [plays[0]]] + [[plays[2]] + [plays[0]]] + [[plays[2]] + [plays[1]]] )
  #   return [[plays[0]] + [[plays[0]]]] + [[plays[1]] + [plays[1]]] + [[plays[2]] + [plays[2]]] + [[plays[0]] + [plays[1]]] + [[plays[0]] + [plays[2]]] + [[plays[1]] + [plays[2]]] + [[plays[1]] + [plays[0]]] + [[plays[2]] + [plays[0]]] + [[plays[2]] + [plays[1]]]
  #   #n = list length
  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')