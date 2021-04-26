import xml.etree.ElementTree as ET
from dateutil.parser import parse

tree = ET.parse('1.xml')
root = tree.getroot()

events = root.findall('{http://schemas.microsoft.com/win/2004/08/events/event}Event')
result_list = []

#print(parse('2020-08-06T16:17:05.3599659Z').strftime("%m/%d/%Y %H:%M:%S"))
#print(date.fromisoformat(events[0][0][7].attrib['SystemTime']))

for event in events:
    #print (parse(event[0][7].attrib['SystemTime']).strftime("%m-%d-%Y %H:%M:%S"))
    result_list.append(parse(event[0][7].attrib['SystemTime']).strftime("%d-%m-%Y %H:%M:%S") +','+str(event[1][0][1].text)+ '\\' + str(event[1][0][0].text) +','+str(event[1][0][2].text))

#print (result_list)


f = open('text.csv', 'w')

with open(r"D:\Артефакты\text.csv", "w") as file:
    file.writelines("%s\n" % line for line in result_list)
