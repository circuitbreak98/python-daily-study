import operator
PEOPLE = [('Donald', 'Trump', 7.85),
          ('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Alan', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]

def format_sort_records1(records):
    sorted_records = sorted(records, key=operator.itemgetter(1,0))
    for r in sorted_records:
        print(f'{r[1]:10} {r[0]:10} {r[2]:5.2f}')

def format_sort_records(records):
    output = []
    template = '{1:10} {0:10} {2:5.2f}'
    for person in sorted(records, key=operator.itemgetter(1,0)):
        output.append(template.format(*person))
    return output

#format_sort_records(PEOPLE)
print('\n'.join(format_sort_records(PEOPLE)))