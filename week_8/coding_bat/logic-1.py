<<<<<<< HEAD
#cigar_party
def cigar_party(cigars, is_weekend):
  if 40<=cigars<=60:
    return True
  elif cigars>=60 and is_weekend:
    return True
  return False

#date_fashion
def date_fashion(you, date):
  if you<=2 or date<=2:
    return 0
  elif you>=8 or date>=8:
    return 2
  elif 2<you<8 or 2<date<8:
    return 1

#squirrel_play
def squirrel_play(temp, is_summer):
  
  if 60<=temp<=90:
    return True
  elif 90<temp<=100 and is_summer==False:
    return False
  elif 90<temp<=100 and is_summer==True:
    return True
  return False

#caught_speeding
def caught_speeding(speed, is_birthday):
  if is_birthday:
      speed-=5
  if speed<=60:
    return 0
  elif 61<=speed<=80:
    return 1
  elif speed>=81:
    return 2

#sorta_sum
def sorta_sum(a, b):
  sum = a+b
  if 10<=sum<=19:
    return 20
  return sum

#alarm_clock
def alarm_clock(day, vacation):
  if (day==1 or day==2 or day==3 or day==4 or day==5) and not vacation:
    return "7:00"
  elif ((day==0 or day==6) and not vacation) or ((day==1 or day==2 or day==3 or day==4 or day==5) and vacation):
    return "10:00"
  else:
    return "off"

#love6
def love6(a, b):
  if a==6 or b==6 or a+b==6 or abs(a-b)==6:
    return True
  return False

#in1to10
def in1to10(n, outside_mode):
  if outside_mode and (n>=10 or n<=1):
    return True
  elif 1<=n<=10 and not outside_mode:
    return True
  return False

#near_ten
def near_ten(num):
  if (num%10)<=2 or num%10>=8:
    return True
  return False

=======
#cigar_party
def cigar_party(cigars, is_weekend):
  if 40<=cigars<=60:
    return True
  elif cigars>=60 and is_weekend:
    return True
  return False

#date_fashion
def date_fashion(you, date):
  if you<=2 or date<=2:
    return 0
  elif you>=8 or date>=8:
    return 2
  elif 2<you<8 or 2<date<8:
    return 1

#squirrel_play
def squirrel_play(temp, is_summer):
  
  if 60<=temp<=90:
    return True
  elif 90<temp<=100 and is_summer==False:
    return False
  elif 90<temp<=100 and is_summer==True:
    return True
  return False

#caught_speeding
def caught_speeding(speed, is_birthday):
  if is_birthday:
      speed-=5
  if speed<=60:
    return 0
  elif 61<=speed<=80:
    return 1
  elif speed>=81:
    return 2

#sorta_sum
def sorta_sum(a, b):
  sum = a+b
  if 10<=sum<=19:
    return 20
  return sum

#alarm_clock
def alarm_clock(day, vacation):
  if (day==1 or day==2 or day==3 or day==4 or day==5) and not vacation:
    return "7:00"
  elif ((day==0 or day==6) and not vacation) or ((day==1 or day==2 or day==3 or day==4 or day==5) and vacation):
    return "10:00"
  else:
    return "off"

#love6
def love6(a, b):
  if a==6 or b==6 or a+b==6 or abs(a-b)==6:
    return True
  return False

#in1to10
def in1to10(n, outside_mode):
  if outside_mode and (n>=10 or n<=1):
    return True
  elif 1<=n<=10 and not outside_mode:
    return True
  return False

#near_ten
def near_ten(num):
  if (num%10)<=2 or num%10>=8:
    return True
  return False

>>>>>>> 02dce2f7d1883584c5b5f3cac5f0e37321f79bfe
