#catalogue = raw_input("Please input name of catalogue.")
#duplicate = raw_input("Please input name of duplicate list.")

catalogue = '1445275010693A.csv'
duplicate = 'duplicates.txt'

try:
    fh_cat = open(catalogue)
except:
    print "ERROR: Cannot open catalogue."

try:
    fh_dup = open(duplicate)
except:
    print "ERROR: Cannot open duplicate list."

file_out = open('refined_list_2arc.csv', 'w')

Dup_array = []
for element in fh_dup:
    Dup_array.append(element.strip())
    print element.strip()

size = len(fh_cat)
count = 0
for line in fh_cat:
    name = line.strip().split(',')
    print "STATUS =  ", int(count/size) * 100, "%"
    #print name[16]
    flag = 0;
    for element in Dup_array:
        if (element == name[16]):
        #if (element.strip() == line.strip()):
            flag = 1
            print "CATCH!"
    if (flag == 0):
        file_out.write(line)
    count += 1
