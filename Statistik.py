def sum(*myData):
    sum=0

    for data in myData:
        sum=sum+data

    jumlah=sum
    print("Jumlahnya: ",jumlah)



def average(*myData):
    sum=0
    i=0

    for data in myData:
        sum=sum+data
        i=i+1

    rata2=sum/i
    print("Rata-ratanya: ",rata2)

def maks(*myData):
    max(myData)
    
    for data in myData:
        max(myData)
        
    maks=max(myData)
    print("Nilai maksimalnya: ",maks)


def minimal(*myData):
    min(myData)
    
    for data in myData:
        min(myData)
        
    minimal=min(myData)
    print("Nilai minimalnya: ",minimal)


