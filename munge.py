# Place code below to do the munging part of this assignment.
import os



data = []

index = 1
heading = False
with open(os.path.join("data", 'GLB.Ts+dSST.txt'), "r") as reader:
    for line in reader:
        line = line.strip()
        if index > 7:
            if len(line) == 0:
                continue
            if line.startswith("Year"):
                if not heading: # do once if no heading yet
                    data.append(','.join(line.split()))
                    heading = True
                else:
                    continue
            else: # data 
                if line.startswith('Divide'):
                    break
                temp = []
                for item in line.split():
                    if item.startswith("*"):
                        temp.append("")
                    elif int(item) < 1000:
                        temp.append(format((float(item) / 100) * 9/5 , '.1f'))
                    else:
                        temp.append(item)
                data.append(','.join(temp))
        index += 1

with open(os.path.join("data", 'cleaned_data.csv'), "w") as writer:
    for line in data:
        writer.write(line + "\n")

