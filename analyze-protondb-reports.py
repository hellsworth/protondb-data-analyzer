#!/usr/bin/python3

import json

def analyze_report():
  f = open ('reports_piiremoved.json')
  dataset = json.load(f)
  p,g,s,br,bo,working = 0,0,0,0,0,0
  for game_data in dataset:
    #print(game_data)
    #print("*******")
    for key,value in game_data.items():
      value = game_data[key]
      #print("{} = {}".format(key, value))
      if key == "rating":
        if value == "Platinum": p+=1
        if value == "Gold": g+=1
        if value == "Silver": s+=1
        if value == "Bronze": br+=1
        if value != "Borked":
          bo+=1
          working+=1
          #print("found a live one!")
  f.close()
  return p,g,s,br,bo,working 


def quick_numbers_check (p,g,s,br,bo,working):
  total_non_borked=0
  total_non_borked=p+g+s+br
  if total_non_borked!=working:
    #raise Exception("Numbers don't match!")
    print("Numbers don't match!")
    print("Sum of non-borked ratings: %d"%total_non_borked)
    print("Counted working: %d"%working)
    diff=total_non_borked-working
    print("The difference is: %d"%diff)


if __name__ == '__main__':
  """
  Protondb publishes monthly data on https://github.com/bdefore/protondb-data
  If you grab any of those report tarballs and unpack it, the resulting
  filename is 'reports_piiremoved.json'

  This script will analyze one report (Nov 2018 - Nov 20219) and print the results.
  Starting in Dec 2019, they changed things and no longer include the rating
  in the json file.
  """

  p,g,s,br,bo,working=analyze_report()
  #quick_numbers_check(p,g,s,br,bo,working)

  print ("%d %d %d %d %d"%(p,g,s,br,bo))
  #print("Platinum = ",p)
  #print("Gold = ",g)
  #print("Silver = ",s)
  #print("Bronze = ",br)
  #print("Borked = ",bo)

