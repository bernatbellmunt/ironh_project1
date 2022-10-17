# SHARK ATTACK!
Bernat Bellmunt Cabutí

![intro](https://user-images.githubusercontent.com/62396094/196137619-22de21e1-76c0-49d4-a9b7-205e91703103.jpeg)



### INTRODUCTION

The aim of this project is to work arround the Shark Attack .csv file that can be found in the following link: https://www.kaggle.com/datasets/teajay/global-shark-attacks?resource=download

This database contains all shark attacks registered so my aim in this project is to work on the following hypothesis:

1. Shark attacks are more fatal in the present.

2. Australia is the country where surfers are more attacked in the summer.

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
Even though the number of attacks have risen with time, the fatality of these attacks has remained stable. Fatality rate was much higher during the 50s and 60s.
Overall the activity that experiences the most attacks is "Other", even though in the last 20 years Surfing is the main cause. However the activity with the highest fatality rate is Swimming. 



### HYPOTHESIS 2: Australia is the country where surfers are more attacked in the summer

   *2.1. What is the season with more attacks?*
   
   *2.2. In the main season, what is the main activity?*
    
   *2.3. If I'm surfing in the season with more attacks, in which country there are more attacks?*
    
   *2.4. In which area should I not surf?*
    

In order to validate or refuse the 2nd hypothesis, I will first look into which hemisphere has a larger number of reported attacks. 
![image](https://user-images.githubusercontent.com/62396094/196156009-f618bc55-52c4-460e-8f91-0bcab20f41b0.png)

Northern hemisphere countries have the highest records of shark attacks: 58% of the attacks happen in the northern hemisphere.

Additionally, we will look into the seasonality of the attacks. We will assume that attacks happen more in the summer time (both in the northern and southern hemisphere) as it is more likely for people to go and swim in the sea. After we take a look at the graph, we can validate this last subhypothesis.
![image](https://user-images.githubusercontent.com/62396094/196159447-70313b61-6768-482e-8811-e0a65db22361.png)


Now that we know that Summer is the shark attack season, which are the main activities that people were performing?
![image](https://user-images.githubusercontent.com/62396094/196159557-384014dd-294c-49de-bbba-440fc42226f8.png)


Summer attacks are majority on Other activities, but since we are looking into surfers, we will focus on the following -> Activity = Surfing, Season = Summer. 
We want to know which is the country has the highest number of attacks to surfers during the summer:
![image](https://user-images.githubusercontent.com/62396094/196159624-1d3d0c82-050b-496f-a316-7bd22b897a07.png)


We can see in the previous graph that **Australia won't be the worst country to surf in the summer, but the USA will!** As the US is such a big country, we will want to know which is the area with more attacks: **FLORIDA**, but at least, these are not fatal!
![image](https://user-images.githubusercontent.com/62396094/196159917-b74d516f-9b95-4892-a753-bf90e8ee3221.png)


In conclusion, we can **refuse the 2nd hypothesis: Australia is the country where surfers are more attacked in the summer**. The country with more attacks registered to surfers in the summer time is USA, lead by Florida.
![image](https://user-images.githubusercontent.com/62396094/196160911-91519405-8afd-4dcb-8d14-6ef876a6879d.png)



### HYPOTHESIS 3: White shark is the most deadly specie and is the specie that attacks more when not provoked

   *3.1. Which species attacks more if unprovoked? How fatal is it?*
   
   *3.2. Which species attacks more if provoked? How fatal is it?*
   
   
   <img width="574" alt="image" src="https://user-images.githubusercontent.com/62396094/196161501-f6d99c13-d68e-4071-a67b-d7c2c1aec26f.png">

Looking at the overall attacks, we see that the Specie that attacks more and has generated the most fatal outcome is the white shark, as we expected from our hypothesis. As we want to look into the type of the accident (provoked or not) we will look into both unprovoked and provoked attacks in order to find the specie that has more attacks of each type.

![image](https://user-images.githubusercontent.com/62396094/196162617-31fa513f-1244-4b70-b794-5a7d555dd34d.png)

![image](https://user-images.githubusercontent.com/62396094/196162655-d1ab7183-0ba2-4c75-8777-66108e29030f.png)

                                 
                                  
After looking into the graphs we can validate the hypothesis: **the white shark is the most deadly specie and the one that attacks the most when there is no provocation from humans**. Humans are not willing to provoke much the white shark, being the nurse shark the specie that has a higher number of recorded provoked attacks.                           


