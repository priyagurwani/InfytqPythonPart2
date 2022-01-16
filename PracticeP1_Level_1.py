
def add_string(str1):
  new_str=""
  if(len(str1)>=3):
      # print(str[-3:])
      if(str1[-3:]!="ing"):
          return new_str.join(str1 + "ing")
      else:
          return new_str.join(str1 + "ly")
  else:
      return str1

str1="com"
print(add_string(str1))
