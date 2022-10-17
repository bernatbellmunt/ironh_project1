# SHARK ATTACK!
Bernat Bellmunt Cabutí

![intro](https://user-images.githubusercontent.com/62396094/196137619-22de21e1-76c0-49d4-a9b7-205e91703103.jpeg)



### INTRODUCTION

The aim of this project is to work arround the Shark Attack .csv file that can be found in the following link: https://www.kaggle.com/datasets/teajay/global-shark-attacks?resource=download

This database contains all shark attacks registered so my aim in this project is to work on the following hypothesis:

1. Shark attacks are more fatal in the present.

2. Australia is the region with more shark attacks.

3. White shark is the most deadly specie and is the specie that attacks more when not provoked.



### CLEANING

**Step 1**: I remove the columns that I don't want -> ['Injury','Investigator or Source', 'pdf', 'href formula', 'href',
'Case Number.1', 'Case Number.2', 'original order', 'Unnamed: 22','Unnamed: 23']. I additionally remove all lines that have null information or more than 2 fields that are null and rename the Columns Sex and Species in order to remove the space located in the last character.

```python 
df= df_raw.drop(columns=['Injury','Investigator or Source', 'pdf', 'href formula', 'href',
       'Case Number.1', 'Case Number.2', 'original order', 'Unnamed: 22',
       'Unnamed: 23'])
df = df.dropna(how="all")
df = df.dropna(thresh=3)
df.rename(columns = {"Species ":"Species"}, inplace=True)
df.rename(columns = {"Sex ":"Sex"}, inplace=True)
```

The new DF will result in the following columns, which will need to be cleaned:
<img width="1122" alt="image" src="https://user-images.githubusercontent.com/62396094/196143150-8e2c3fc7-7b4d-439a-99e0-33cca9d2bb52.png">



**Step 2**: I will keep data with year > 1900 and will remove data with no Year associated and change the data type column to integer.
```python
df.drop (df[df.Year < 1900].index, inplace=True)
df = df[df.Year.notna()]
df["Year"] = df["Year"].astype(int)
df.dtypes
```


**Step 3**: I will clean Country column by turning all of the to Capital letters and Type Column by removing empty values.


**Step 4**: I will obtain both days and months based on the Case Number column. Once retrieved, I will remove Case Number column from the DF. ["Day", "Month", "Year"] will be Integers
```python
df["Date"] = df["Date"].str.replace("Reported ","")
df.insert(2,"Months",df['Case Number'].str.extract('\.(\d{2})\.'))
df.insert(2,"Day",df['Case Number'].str.extract('\.\d{2}\.(\d{2})'))
df["Year"] = df["Year"].astype(int)
df["Months"] = df["Months"].astype(int)
df["Day"] = df["Day"].astype(int)
```


**Step 5**: I want to create a new column -> Season. In order to do this, I will first need to know the Country's Hemisphere ["NORTH", "SOUTH"] and based on the month the attack will happen in ["SUMMER", "AUTUMN", "WINTER", "SPRING"]. I will rearrange columns too.
<img width="1126" alt="Screenshot 2022-10-17 at 11 43 49" src="https://user-images.githubusercontent.com/62396094/196145623-cb6d0019-5eae-45d8-b8eb-baeb74c05763.png">


**Step 6**: I will clean Age, Fatality and Sex columns in order to keep the following: integer, Y/N and M/F.
```python
df["Age"] = df["Age"].str.extract("(\d{1,2})")
df["Fatal (Y/N)"] = df["Fatal (Y/N)"].str.extract("(^Y|N)")
df["Sex"] = df["Sex"].str.extract("(^M|F)")
```


**Step 7**: I will clean the Species column. I will do that by keeping "shark" and the previous word from it.
```python
df["Species"] = df["Species"].str.extract("([A-Z|a-z]{1,}\s{1}shark)")
```


**Step 8**: Finally I will clean the Activity column by grouping the activities in the following: ["Diving", "Surfing", "Swimming", "Fishing","Walking", "Sailing","Other"]



### HYPOTHESIS 1: Shark attacks are more fatal in the present

1. Analysis on the evolution of attacks throughout the years.

   *1.1. How has fatality evolutioned*
   
   *1.2. What are the main activities people were performing when attacked?*
   
   *1.3. Is there a more fatal activity?*
   

<img width="565" alt="image" src="https://user-images.githubusercontent.com/62396094/196149421-3f29d584-07f3-4f58-aae8-adc03a380c24.png">

Overall, the number of shark attacks has followed a positive tendency throughout the years. 
The gragh is split based on the fatality.
- None fatal attacks have increased during the last 20 years.
- Fatal attacks have remained stable throughout the years observed.

![image](https://user-images.githubusercontent.com/62396094/196152999-adb65f02-df35-4f4d-85e8-2f6c729ee78c.png)
During the last years, the attacks to surfers have experienced an important growth, being this the main activity from 1990s to the present.
Surfing is not the most fatal activity overall, nor the most likely to happen. More attacks have been registered for Other activities.

In proportion, the most fatal activity is swimming.
![image](https://user-images.githubusercontent.com/62396094/196153896-f6757687-3c91-4088-8623-9fcf6eddd9f2.png)

Therefore we can **refuse the first hypothesis**.
Even though the number of attacks have risen with time, the fatality of these attacks has remained stable. Overall the activity that experiences the most attacks is "Other", even though in the last 20 years Surfing is the main cause. However the activity with the highest fatality rate is Swimming. 



2. If I were a surfer, when and where is it more likely I will get attacked?

   *2.1. What is the season with more attacks?*
   
   *2.2. In the main season, what is the main activity?*
    
   *2.3. If I'm surfing in the season with more attacks, in which country there are more attacks?*
    
   *2.4. In which area should I not surf?*
    




3. Study the shark species, which one attacks more?

   *3.1. Which species attacks more if unprovoked? Where?*
   
   *3.2. Which species attacks more if provoked? Where?*
