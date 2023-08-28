import csv

def passwd_to_csv1(passwd_path, write_path):
    passwd = {}
    with open(passwd_path) as f:
        for line in f:
            if line[0] == '#':
                continue
            else:
                infos = line.split(':')
                username, userid = infos[0], infos[2]
                passwd[username] = userid
    
    with open(write_path,'w') as f:
        o = csv.writer(f, delimiter='\t')
        for key, value in passwd.items():
            o.writerow((key, value))
            
def passwd_to_csv(passwd_filename, csv_filename):
    with open(passwd_filename) as passwd, open(csv_filename, 'w') as output:
        infile = csv.reader(passwd, delimiter=':')
        outfile = csv.writer(output, delimiter='\t')
        for record in infile:
            if len(record) > 1:
                outfile.writerow((record[0],record[2]))


passwd_to_csv('./passwd', 'passwd.csv')
