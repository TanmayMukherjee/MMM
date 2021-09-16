import csv
from collections import Counter

with open('SOCR-HeightWeight.csv',newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)

newData=[]
for i in range(len(file_data)):
    n_num=file_data[i][1]
    newData.append(float(n_num))

n=len(newData)
total=0
for x in newData:
    total=total+x
mean=total/n
print("Mean Is: "+str(mean))

newData.sort()
if n%2==0:
    median1=float(newData[n//2])
    median2=float(newData[n//2-1])
    median=(median1+median2)/2
else:
    median=newData[n//2]

print("Median Is-> "+str(median))

data=Counter(newData)
modeDataForRange={
    "50-60":0,
    "60-70":0,
    "70-80":0
}
for height,occurence in data.items():
    if 50<float(height)<60:
        modeDataForRange["50-60"]+=occurence
    elif 60<float(height)<70:
        modeDataForRange["60-70"]+=occurence
    elif 70<float(height)<80:
        modeDataForRange["70-80"]+=occurence

mode_range, mode_occurence = 0, 0
for range, occurence in modeDataForRange.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"Mode is -> {mode:2f}")

