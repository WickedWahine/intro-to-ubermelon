log_file = open("./um-server-01.txt")

def sales_reports(log_file):
    '''Function pulls Monday delivery data from server file'''

    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)

sales_reports(log_file)
