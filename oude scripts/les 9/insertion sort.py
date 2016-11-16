__author__ = 'alexander'

def insertionSort(stations):
   for index in range(1,len(stations)):

     currentvalue = stations[index]
     position = index

     while position>0 and stations[position-1]>currentvalue:
         stations[position]=stations[position-1]
         position = position-1

     stations[position]=currentvalue

stations = ['Geldermalsen', 'Utrecht Centraal', 'Amsterdam Centraal', '\'s-hertogenbosch']
insertionSort(stations)
print(stations)
