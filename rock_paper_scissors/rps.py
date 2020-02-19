#!/usr/bin/python

import sys




def rock_paper_scissors(n):
  plays = ['rock', 'paper', 'scissors']
  
  possibilites = []

  #Recursive Case
  def choice(round, num):
    #Base Case
    for i in range(0, len(plays)):
      round.append(plays[i])
      if num >= n:
        possibilites.append(round[0:len(round)]
      elif n == 0:
        return possibilites.append([])
      else:
        #Progress made at each invocation of the 
        # recursive function.
        choice(round, num + 1)
      round.pop()
  
  choice([],1)
  return possibilites



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')