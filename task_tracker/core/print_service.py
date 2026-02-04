def table_print(tasks: dict):
    '''Print tasks inside a table'''
    id_spacing = 0
    desc_spacing = 0
    status_spacing = 0

    for t in tasks:
        if id_spacing < len(str(t['id'])):
            id_spacing = len(str(t['id']))
        if desc_spacing < len(t['description']):
            desc_spacing = len(t['description'])
        if status_spacing < len(t['status']):
            status_spacing = len(t['status'])

    BORDER = (
        '+-'
        f'{'-' * id_spacing}'
        '---'
        f'{'-' * desc_spacing}'
        '---'
        f'{'-' * status_spacing}'
        '---'
        '-------------------'
        '---'
        '-------------------'
        '-+'
    )
    HEADER = (
        '| '
        f'{' ' * id_spacing}'
        ' | '
        f'TASKS:{' ' * (desc_spacing - len('TASKS:'))}'
        ' | '
        f'{' ' * status_spacing}'
        ' | '
        f'CREATED AT:        '
        ' | '
        f'UPDATED AT:        '
        ' |'
    )

    print(BORDER)
    print(HEADER)
    for t in tasks:
        ROW = (
            '| '
            f'{str(t['id'])}{' ' * (id_spacing - len(str(t['id'])))}'
            ' | '
            f'{t['description']}{' ' * (desc_spacing - len(t['description']))}'
            ' | '
            f'{t['status']}{' ' * (status_spacing - len(t['status']))}'
            ' | '
            f'{t['createdAt']}'
            ' | '
            f'{t['updatedAt']}'
            ' |'
        )
        print(ROW)
    print(BORDER)
