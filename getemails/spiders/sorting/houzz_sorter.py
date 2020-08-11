import csv

mainfile = open('main_houzz.csv','r')
emailfile = open('output_emails1.csv','r')

output_file = open('sorted_output.csv','w')

mainreader = csv.reader(mainfile)
emailreader = csv.reader(emailfile)
'''
for row0 in emailreader:
    email_domain = row0[1].split(';')
    for email in email_domain:
        if email != '':
            email = email.split('@')[1]
            for row1 in mainreader:
                if email in row1[4]:
                    print(email, row1[1])

'''
url_list = []
for row0 in mainreader:
    if row0[3] != "":
        #print(row0[3])
        #output_file.write('{},{},{},{},{}\n'.format(row0[0],row0[1],row0[2],row0[3],row0[4]))
        pass
    else:
        for row1 in emailreader:
            if str(row0[4]) in str(row1[0]):
                print(row0[4], row1[0])
                #output_file.write('{},{},{},{},{}\n'.format(row0[0],row0[1],row0[2],row1[1],row0[4]))
            
