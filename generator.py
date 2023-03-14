import pandas as pd
from workout import rm_duplicates

# Read the CSV file into a pandas dataframe
df = pd.read_csv("file_name.csv")

# Extract the unique values of intents and actions from the dataframe
intents = df['intent/action name'].unique().tolist()
actions = [i.split(':')[1].strip() for i in intents if 'action' in i]
intents = [i.split(':')[1].strip() for i in intents if 'intent' in i]
# Create the nlu.yml file
with open('nlu.yml', 'w') as f:
    for intent in intents:
        examples = df[df['sms type']=='incoming'][df['intent/action name']=='intent: '+intent]['message'].tolist()
        examples = "\n    - ".join(examples)
        f.write(f"- intent: {intent}\n")
        f.write(f"  examples: |\n    - {examples}\n\n")
# Create the stories.yml file
with open('stories.yml', 'w') as f:
    stories = []
    apns = df['apn'].unique().tolist()
    act_list=[]
    int_list=[]
    total_value=[]
    for apn in apns:
        df_apn = df[df['apn'] == apn]
        actions_list = df_apn['intent/action name'].tolist()
        intents_list = df_apn['intent/action name'].tolist()
        total_value.append(actions_list)
        act_list.append(actions_list)
        int_list.append(intents_list)
    for i in range(len(total_value)):
        total_value[i].append(apns[i])
    total_value1=total_value
    for i in range(len(total_value)):
        del total_value[i][-1]
    my_instance = rm_duplicates()
    ac_lists = my_instance.remove_duplicates(act_list)
    in_lists = my_instance.remove_duplicates(int_list)
    total_value=my_instance.remove_duplicates(total_value)
    print(total_value)
    apn=[]

    for i in range(len(total_value)):
        index=total_value1.index(total_value[i])
        apn.append(apns[index])

    list1 = []
    list2 = []
    print(apn)
    for aclist in ac_lists:
     actions_list = [j.split(':')[1].strip() for j in aclist if 'action' in j]
     list1.append(actions_list)
    for inlist in in_lists: 
     intents_list = [j.split(':')[1].strip() for j in inlist if 'intent' in j]
     list2.append(intents_list)
    for i in range(len(apn)):
        f.write(f"- story: story-{apn[i]}\n")
        f.write("  steps:\n")
        for j in total_value[i]:
          f.write(f"  - {j}\n")
        f.write("\n")
