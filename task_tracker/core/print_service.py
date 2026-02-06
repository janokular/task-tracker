ID = 'ID'
TASKS = 'TASKS'
STATUS = 'STATUS'
CREATED_AT = 'CREATED AT'
UPDATED_AT = 'UPDATED AT'


def table(tasks: dict):
    '''Construct and print table with even spaces for tasks'''
    label_spacing = cal_label_spacing()
    cell_spacing = cal_cell_spacing(label_spacing, tasks)

    border = construct_border(cell_spacing)
    header = construct_header(cell_spacing, label_spacing)
    rows = construct_rows(tasks, cell_spacing)

    print_table(border, header, rows)


def cal_label_spacing() -> dict[str, int]:
    '''Calculate default spacing based on label length'''
    return {
        'id': len(ID),
        'task': len(TASKS),
        'status': len(STATUS),
        'createdAt': len(CREATED_AT),
        'updatedAt': len(UPDATED_AT),
    }


def cal_cell_spacing(spacing: dict, tasks: dict) -> dict[str, int]:
    '''Calculate cell spacing when cell length is bigger than label length'''
    id_spacing = spacing['id']
    task_spacing = spacing['task']
    status_spacing = spacing['status']
    created_spacing = spacing['createdAt']
    updated_spacing = spacing['updatedAt']
    
    for task in tasks:
        if id_spacing < len(str(task['id'])):
            id_spacing = len(str(task['id']))
        if task_spacing < len(task['description']):
            task_spacing = len(task['description'])
        if status_spacing < len(task['status']):
            status_spacing = len(task['status'])
        if created_spacing < len(task['createdAt']):
            created_spacing = len(task['createdAt'])
        if updated_spacing < len(task['updatedAt']):
            updated_spacing = len(task['updatedAt'])

    return {
        'id': id_spacing,
        'task': task_spacing,
        'status': status_spacing,
        'createdAt': created_spacing,
        'updatedAt': updated_spacing,
    }


def construct_border(cell_spacing: dict) -> str:
    '''Construct table border'''
    return (
        '+-'
        f"{'-' * cell_spacing['id']}"
        '---'
        f"{'-' * cell_spacing['task']}"
        '---'
        f"{'-' * cell_spacing['status']}"
        '---'
        f"{'-' * cell_spacing['createdAt']}"
        '---'
        f"{'-' * cell_spacing['updatedAt']}"
        '-+'
    )


def construct_header(cell_spacing: dict, label_spacing: dict) -> str:
    '''Construct table header'''
    id_spacing = cell_spacing['id'] - label_spacing['id']
    task_spacing = cell_spacing['task'] - label_spacing['task']
    status_spacing = cell_spacing['status'] - label_spacing['status']
    created_spacing = cell_spacing['createdAt'] - label_spacing['createdAt']
    updated_spacing = cell_spacing['updatedAt'] - label_spacing['updatedAt']

    return (
        '| '
        f"{ID}{' ' * id_spacing}"
        ' | '
        f"{TASKS}{' ' * task_spacing}"
        ' | '
        f"{STATUS}{' ' * status_spacing}"
        ' | '
        f"{CREATED_AT}{' ' * created_spacing}"
        ' | '
        f"{UPDATED_AT}{' ' * updated_spacing}"
        ' |'
    )


def construct_rows(tasks: dict, cell_spacing: dict) -> list[str]:
    '''Construct table rows'''
    rows = []
    for task in tasks:
        rows.append(
            '| '
            f"{str(task['id'])}{' ' * (cell_spacing['id'] - len(str(task['id'])))}"
            ' | '
            f"{task['description']}{' ' * (cell_spacing['task'] - len(task['description']))}"
            ' | '
            f"{task['status']}{' ' * (cell_spacing['status'] - len(task['status']))}"
            ' | '
            f"{task['createdAt']}{' ' * (cell_spacing['createdAt'] - len(task['createdAt']))}"
            ' | '
            f"{task['updatedAt']}{' ' * (cell_spacing['updatedAt'] - len(task['updatedAt']))}"
            ' |'
        )
    return rows

def print_table(border: str, header: str, rows: list[str]):
    '''Print table'''
    print(border)
    print(header)
    for row in rows:
        print(row)
    print(border)
