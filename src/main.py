import pandas as pd
from pulp import LpMaximize, LpProblem, LpVariable, lpSum, LpStatus, value, PULP_CBC_CMD


def get_hours_allocation(df, priority_dict):
    model = LpProblem(name='Task_Scheduling', sense=LpMaximize)

    max_hours_per_day = 4
    max_tasks_per_day = 4

    task_count = len(df['Task'])
    
    hours_vars = LpVariable.dicts('Hours_Task', list(range(task_count)), lowBound=0, upBound=max_hours_per_day, cat='Integer')
    total_hours_per_day = LpVariable("Total_hours_per_day", lowBound=0, upBound=max_hours_per_day, cat='Integer')

    chosen_tasks = LpVariable.dicts('Chosen_Task', list(range(task_count)), cat='Binary')
    total_tasks_per_day = LpVariable("Total_tasks_per_day", lowBound=0, upBound=max_tasks_per_day, cat='Integer')

    # Objective function: maximize sum of Hours_Task_i * Priority_i / Days_To_Deadline_i for all tasks
    model += lpSum([hours_vars[i] * priority_dict[df.loc[i, 'Priority']] / df.loc[i, 'Days To Deadline'] for i in range(task_count)])

    # Constraint: a task is either chosen or not
    for i in range(task_count):
        model += hours_vars[i] <= chosen_tasks[i] * df.loc[i, 'Hours Estimate'], f'Choose_Task_{i}'

    # Constraint: the total number of chosen tasks must not exeed the maximum number of tasks per day
    model += lpSum([chosen_tasks[i] for i in range(task_count)]) <= total_tasks_per_day

    # Constraint: the total hours allocated per day across all tasks must not exceed the maximum available hours per day
    model += lpSum([hours_vars[i] for i in range(task_count)]) <= total_hours_per_day
    model += total_hours_per_day <= max_hours_per_day, 'Max_Hours_per_Day'

    model.solve(PULP_CBC_CMD(msg=False))

    status = LpStatus[model.status]
    # print(f'Status: {status}')

    hours_allocation = {df.loc[i, 'Task']: value(hours_vars[i]) for i in range(task_count)}
    return hours_allocation


def main():
    #df = pd.read_excel('src/data/work_tasks.xlsx')
    #df = pd.read_excel('src/data/university_tasks.xlsx')
    df = pd.read_excel('src/data/running_example_1.xlsx')
    priority_dict = {"High": 3, "Normal": 2, "Low": 1}
    df['Numerical Priority'] = df['Priority'].map(priority_dict)
    default_hours_allocation = {df.loc[i, 'Task']: 0 for i in range(len(df['Task']))}

    days = 0

    while not df[(df['Hours Estimate'] > 0) & (df['Days To Deadline'] > 0)].empty:
        day_hours_allocation = get_hours_allocation(df[(df['Hours Estimate'] > 0) & (df['Days To Deadline'] > 0)].reset_index(drop=True), priority_dict)
        day_hours_allocation = dict(default_hours_allocation, **day_hours_allocation)

        print(df)
        print()
        print(dict(sorted(day_hours_allocation.items(), key=lambda item: item[1], reverse=True)))
        print('--------------------------------------------------------------------------------')
        print()

        df['Hours Estimate'] = df['Hours Estimate'].sub(list(day_hours_allocation.values()))
        df['Days To Deadline'] = df['Days To Deadline'].sub(1)

        days += 1

    print(df)
    print()
    print('Days worked: ' + str(days))


main()