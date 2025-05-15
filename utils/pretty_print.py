rows = []
maxes = {'id_len': 0, 'desc_len': 0, 'status_len': 0}


def add_table_data(task):
    '''Append task and max length for dynamic column sizes'''
    rows.append(task)

    if maxes['id_len'] < len(str(task['id'])):
        maxes['id_len'] = len(str(task['id']))

    if maxes['desc_len'] < len(task['description']):
        maxes['desc_len'] = len(task['description'])

    if maxes['status_len'] < len(task['status']):
        maxes['status_len'] = len(task['status'])


def display_table():
    '''Print table with tasks inside dynamic columns'''
    if rows:
        max_id_len = maxes['id_len']
        max_desc_len = maxes['desc_len']
        max_status_len = maxes['status_len']

        print('·-' + '-' * max_id_len + '-' 
            + '·-' + '-' * max_desc_len + '-' 
            + '·-' + '-' * max_status_len 
            + '-·--------------------------·--------------------------·')

        for row in rows:
            print('| {} '.format(row['id']) 
                    + ' ' * (max_id_len - len(str(row['id'])))
                    + '| {} '.format(row['description']) 
                    + ' ' * (max_desc_len - len(row['description']))
                    + '| {} '.format(row['status']) 
                    + ' ' * (max_status_len - len(row['status']))
                    + '| {} | {} |'.format(row['createdAt'], row['updatedAt']))

        print('·-' + '-' * max_id_len + '-' 
            + '·-' + '-' * max_desc_len + '-' 
            + '·-' + '-' * max_status_len 
            + '-·--------------------------·--------------------------·')
