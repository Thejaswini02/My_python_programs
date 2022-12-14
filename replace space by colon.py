# Write your code here :-)
import re
p=input('Enter the string with space , comma , dot : ')
print(re.sub('[,\.\s]',':',p))
