import csv


def cse(reader):
    for row in reader:
        if row[2]=='CSE':
            if int(row[4])>=75:
                if int(row[5])>=75:
                    if int(row[6])>=75:
                        print(row)


def ece(reader):
    for row in reader:
        if row[2]=='ECE':
            if int(row[4])>=75:
                if int(row[5])>=75:
                    if int(row[6])>=75:
                        print(row)
                        

def eee(reader):
    for row in reader:
        if row[2]=='EEE':
            if int(row[4])>=75:
                if int(row[5])>=75:
                    if int(row[6])>=75:
                        print(row)


def ce(reader):
    for row in reader:
        if row[2]=='CE':
            if int(row[4])>=75:
                if int(row[5])>=75:
                    if int(row[6])>=75:
                        print(row)


def me(reader):
    for row in reader:
        if row[2]=='ME':
            if int(row[4])>=75:
                if int(row[5])>=75:
                    if int(row[6])>=75:
                        print(row)
                        
if __name__=='__main__':
    print("\nResume filtering: \n")
    print("\n1 : CSE\n2 : ECE\n3 : EEE\n4 : CE\n5 : ME\n")
    ch=int(input("\nChoose any option: "))
    
    with open('clg.csv','r') as file:
        reader=csv.reader(file)
        if ch==1:
            cse(reader)
        elif ch==2:
            ece(reader)
        elif ch==3:
            eee(reader)
        elif ch==4:
            ce(reader)
        else:
            me(reader)



















        
