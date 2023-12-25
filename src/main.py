import pandas as pd
from pulp import LpMaximize, LpProblem, LpVariable, lpSum, LpStatus, value

def main():
    df = pd.read_excel('src/data/work_tasks.xlsx')

    priority_dict = {"High": 3, "Normal": 2, "Low": 1}
    df['Numerical Priority'] = df['Priority'].map(priority_dict)

    print(df)

    model = LpProblem(name='Task_Scheduling', sense=LpMaximize)

    max_hours_per_day = 8
    task_count = len(df['Task'])
    
    hours_vars = LpVariable.dicts('Hours_Task', list(range(task_count)), lowBound=0, upBound=max_hours_per_day, cat='Continuous')
    total_hours_per_day = LpVariable("Total_hours_per_day", lowBound=0, upBound=max_hours_per_day, cat='Continuous')

    # Objective function: maximize sum of Hours_Task_i * Days_To_Deadline_i * Priority_i for all tasks
    model += lpSum([hours_vars[i] * df.loc[i, 'Days To Deadline'] * priority_dict[df.loc[i, 'Priority']] for i in range(task_count)])

    # Constraint: each task must be completed within the available days
    for i in range(task_count):
        model += hours_vars[i] * df.loc[i, 'Days To Deadline'] >= df.loc[i, 'Hours Estimate'], f'Complete_Task_{i}'

    # Constraint: the total hours allocated per day across all tasks must not exceed the maximum available hours per day
    model += lpSum([hours_vars[i] for i in range(task_count)]) == total_hours_per_day
    model += total_hours_per_day <= max_hours_per_day, 'Max_Hours_per_Day'

    model.solve()

    status = LpStatus[model.status]
    print(f'Status: {status}')

    hours_allocation = {df.loc[i, 'Task']: value(hours_vars[i]) for i in range(task_count)}
    total_hours = value(total_hours_per_day)
    print(hours_allocation, total_hours)

main()