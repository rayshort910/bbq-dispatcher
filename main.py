from pprint import pprint

from table import Table, rounds

def main():
    tables = int(input('How many tables for this contest? '))
    samples = int(input('What is the max number of samples for one table? '))
    max_teams = tables * samples
    all_tables = [Table(id=x, limit=samples) for x in range(1,tables+1)]
    for rnd in rounds:
        print('Current round: {}'.format(rnd.upper()))
        for _ in range(max_teams):
            box = input('Next box number or "Done" for round end: ')
            if box == 'Done' or box == 'done':
                break
            box = int(box)
            print('Give box {} to table {}'.format(box, get_able_table(all_tables, rnd, box)))
    for table in all_tables:
        print('Table {}: '.format(table.id))
        pprint(table.boxes)
    return 
        

def get_able_table(tables, rnd, box):
    for table in tables:
        if table.can_take(rnd, box):
            table.add_box(rnd, box)
            return table.id

if __name__ == '__main__':
    main()
