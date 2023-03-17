import pandas as pd
from workout import rm_duplicates
from datetime import datetime, timedelta
import datetime
import math
import yaml
df = pd.read_csv("Cash offer question report-2023-03-08-23-10-56.xlsx - Copy of Cash offer question report.csv")
df['Created Date'] = pd.to_datetime(df['Created Date'], format='%m/%d/%Y %I:%M %p')
#when include sececonds include this code df['Created Date'] = pd.to_datetime(df['Created Date'], format='%m/%d/%Y %I:%M:%S %p')
df = df.sort_values(by='Created Date', ascending=True)
intents = df['intent & action'].unique().tolist()
intents = [i.split(':')[1].strip() for i in intents if isinstance(i, str) and 'intent' in i]
intent=[]
for value in intents:
    if value != '':
       intent.append(value)
value2=[]
for value1 in intent:
    if value1 not in value2:
        value2.append(value1)
apns = df['Lead: Real Estate Number'].unique().tolist()
# Getting only incoming real_estate number
incoming = df[df['SMS History: SMS Type']=='Incoming'].values.tolist()
# values collect total row values
incoming_str = str(incoming)
incoming_str = incoming_str.encode('utf-8', errors='ignore')
data_str = incoming_str.decode('utf-8', errors='ignore')
data_str=data_str.strip()
real_estate_number=[]
for i in range(len(apns)):
    if str(apns[i]) in data_str:
        real_estate_number.append(apns[i])
total_value=[]
for apn1 in real_estate_number:
    result = df[(df['Lead: Real Estate Number'] == apn1)]['intent & action'].tolist()
    total_value.append(result)
res=[]
intent_list=[]
# Create the nlu.ynl file
with open('nlu.yml', 'w',encoding="utf-8") as f:
    for i in range(len(value2)):
        intent_list.append(value2[i])
        value2[i]='- intent: '+value2[i]
        examples = df[(df['SMS History: SMS Type']=='Incoming') & (df['intent & action']==str(value2[i]))]['Message'].unique().tolist()
        result=[]
        for item in examples:
              item= ' '.join(item.splitlines())
              result.append(item)
        f.write(f"{value2[i]}\n")
        f.write("  examples: |\n")
        for i in range(len(result)):
            f.write(f"    - {result[i]}\n")
# Create the stories.yml file
with open('stories.yml', 'w') as f:
    total_value1=[]
    # when n number of action: utter_offer in starting we consider only one so remove other
    for elem in total_value:
        for i in range(len(elem)):
          if len(elem)>1:
            j=1
            if elem[0]=='- action: utter_offer':
                if elem[0] == elem[j]:
                    del elem[j]
                else:
                    break
            if j!=len(elem):
                j=j+1
        total_value1.append(elem)
    # remove null values
    total_value = [inner_list for inner_list in total_value1 if not any(isinstance(element, float) and math.isnan(element) for element in inner_list)]
    my_instance = rm_duplicates()
    # call the class
    total_value=my_instance.remove_duplicates(total_value)
    for i in range(len(total_value)):
        f.write(f"- story: story-{i+1}\n")
        f.write("  steps:\n")
        f.write(f"     - intent: start_cash_offer\n")
        for j in total_value[i]:
          if 'intent' in j or 'action' in j:
            f.write(f"     {j}\n")
          else:
            if j[2::] not in intent_list:
                 f.write(f"     - action:{j[1::]}\n")
            else:
                 f.write(f"     - intent:{j[1::]}\n")  
        f.write("\n")

