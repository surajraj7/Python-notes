# write a program to fill ina letter template given below with name and date
letter='''
Dear<|Name|>,
 You are selected!
<|Date|>
 '''
print(letter.replace("<|Name|>", "Harry").replace("<|Date|>","24 september"))
 