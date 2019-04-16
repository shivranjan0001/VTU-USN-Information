usn = input('Enter your USN: ')
div = usn[0]
colcode = usn[1:3]
year = usn[3:5]
branch = usn[5:7]
rcode = usn[7:]
print('Division: {}\nCollege Code: {}\nYear: {}\nBranch: {}\nRoll Number: {}'.format(div,colcode,year,branch,rcode) )
