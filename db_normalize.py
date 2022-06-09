
infile = open('Database_Limited.csv', 'r')
outfile = open('database_discretized.csv', 'w')
#skip the header 
header = infile.readline()
header = header[:-1]
header_fields = header.split(',')

#change the attribute 'state' into 'region' and printing the header to outfile
header_fields[2] = 'Region'
header = ','.join(header_fields)
print(header, file=outfile)

#lists for discretizing 
list1 = ['ME', 'VT', 'NH', 'MA', 'RI', 'CT', 'NJ', 'PA', 'NY']
list2 = ['DE', 'MD', 'DC', 'WV', 'VA', 'KY', 'NC', 'TN', 'SC', 'MS', 'AL', 'GA', 'LA', 'FL', 'AR']
list3 = ['OK', 'TX', 'NM', 'AZ']
list4 = ['ND', 'MN', 'WI', 'MI', 'SD', 'NE', 'KS', 'MO', 'IA', 'IL', 'IN', 'OH']
list5 = ['WA', 'OR', 'CA', 'ID', 'NV', 'MT', 'WY', 'UT', 'CO', 'AK', 'HI']

list6 = ['MILITARY', 'GOVERNMENT', 'US COAST GUARD', 'US CUSTOMS AND BORDER', 'US DEPT OF JUSTICE ']
list7 = ['BOMBARDIER BUSINESS JET SOLUTIONS', 'BOMBARDIER BUSINESS JET', 'BUSINESS', 'BUSINESS AVIATION COURIER', 'BUSINESS EXPRESS','DELTA AIRELITE BUSINESS JETS']
list8 = ['AIR CARGO CARRIERS', 'AIR CHINA CARGO', 'ALOHA AIR CARGO', 'ASTAR AIR CARGO', 'AVIANCA CARGO', 'CAPITAL CARGO INTL', 'CARGOJET AIRWAYS','CARGOLUX AIRLINES INTL',  'CENTURION CARGO', 'CONTRACT AIR CARGO', 'KITTY HAWK AIR CARGO', 'LAN CARGO COLUMBIA', 'LUFTHANSA CARGO', 'LYNDEN AIR CARGO', 'MOUNTAIN AIR CARGO', 'NIPPON CARGO AIRLINES', 'NORTHERN AIR CARGO', 'PACCAIR (PRO AIRE) CARGO', 'POLAR AIR CARGO', 'SHANGHAI CARGO', 'SINGAPORE AIRLINES']
list9 = ['FEDEX EXPRESS', 'UPS AIRLINES']
list10 = ['PRIVATELY OWNED']

for line in infile:
    line = line[:-1]
    fields = line.split(',')
    #Discretizing the attribute 'region'
    if fields[2] in list1: 
        fields[2] = fields[2].replace(fields[2], 'NORTHEAST')
        newline = ','.join(fields)        
    elif fields[2] in list2: 
        fields[2] = fields[2].replace(fields[2], 'SOUTHEAST')
        newline = ','.join(fields)
    elif fields[2] in list3: 
        fields[2] = fields[2].replace(fields[2], 'SOUTHWEST')
        newline = ','.join(fields)
    elif fields[2] in list4: 
        fields[2] = fields[2].replace(fields[2], 'MIDWEST')
        newline = ','.join(fields)
    elif fields[2] in list5: 
        fields[2] = fields[2].replace(fields[2], 'WEST')
        newline = ','.join(fields)
        
    #Discretizing the attribute 'operator'   
    if fields[4] in list6:
        fields[4] = fields[4].replace(fields[4],'GOVERNMENT')
        newline = ','.join(fields)
        print(newline, file=outfile)
    elif fields[4] in list7:
        fields[4] = fields[4].replace(fields[4],'BUSINESS')
        newline = ','.join(fields)
        print(newline, file=outfile)
    elif fields[4] in list8:
        fields[4] = fields[4].replace(fields[4],'CARGO')
        newline = ','.join(fields)
        print(newline, file=outfile)
    elif fields[4] in list9:
        fields[4] = fields[4].replace(fields[4],'SHIPPING')
        newline = ','.join(fields)
        print(newline, file=outfile)
    elif fields[4] in list10:
        fields[4] = fields[4].replace(fields[4],'PRIVATE')
        newline = ','.join(fields)
        print(newline, file=outfile)
    else:
        fields[4] = fields[4].replace(fields[4],'COMMERCIAL')
        newline = ','.join(fields)
        print(newline, file=outfile)

outfile.close()
infile.close()
