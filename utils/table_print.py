def print_table(tasks: dict):
    '''Print tasks inside a table'''
    id_col_len = 0
    desc_col_len = 0
    status_col_len = 0

    for task in tasks:
        if id_col_len < len(str(task['id'])):
            id_col_len = len(str(task['id']))

        if desc_col_len < len(task['description']):
            desc_col_len = len(task['description'])

        if status_col_len < len(task['status']):
            status_col_len = len(task['status'])

    print('+-' + '-' * id_col_len
          + '---' + '-' * desc_col_len
          + '---' + '-' * status_col_len
          + '-------------------------------------------------------+')

    for task in tasks:

        print('| {} '.format(str(task['id']))
              + ' ' * (id_col_len - len(str(task['id'])))
              + '| {} '.format(task['description'])
              + ' ' * (desc_col_len - len(task['description']))
              + '| {} '.format(task['status'])
              + ' ' * (status_col_len - len(task['status']))
              + '| {} | {} |'.format(task['createdAt'], task['updatedAt']))

    print('+-' + '-' * id_col_len
          + '---' + '-' * desc_col_len
          + '---' + '-' * status_col_len 
          + '--------------------------------------------------------')
