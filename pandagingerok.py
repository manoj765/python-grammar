from gingerit.gingerit import GingerIt
import pandas 
#text = input("Enter text to be corrected")
text = pandas.read_csv('train.csv')
result = GingerIt().parse(text)
corrections = result['corrections']
correctText = result['result']
print(text)

print("AFTER APPYING GRAMMAR CHECK THE TEXT IS:")

print("Correct Text:",correctText)
print()
print("CORRECTIONS")
for d in corrections:
  print("________________")  
  print("Previous:",d['text'])  
  print("Correction:",d['correct'])   
  print("Definiton:",d['definition'])
 
