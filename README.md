Given a list of tasks with a priority, estimated number of work hours, and number of days until deadline like below, the program attempts to optimize the number of hours to work on each task on a given day.

![image](https://github.com/LuchianGheorghe/task-scheduler-or/assets/73704963/b592e3e4-2b0d-4df4-9b55-ff0c2db15c2c)

Values for the maximum number of hours to work in a day, and maximum number or tasks to work in a day are specified.

![image](https://github.com/LuchianGheorghe/task-scheduler-or/assets/73704963/3b16c93b-c91d-49e7-9265-eb6a6226f3ac)

Objective function and constraints: 

![image](https://github.com/LuchianGheorghe/task-scheduler-or/assets/73704963/0cc49bac-82b3-4542-a924-368c4b840381)

Example output for the tasks above, ran multiple times and subtracting the hours worked and the passing days:

```
     Task Priority  Hours Estimate  Days To Deadline  Numerical Priority
0  Task_0     High               6                 2                   3
1  Task_1      Low               4                 2                   1
2  Task_2     High               2                 3                   3
3  Task_3   Normal               8                 3                   2
4  Task_4     High               4                 3                   3
5  Task_5      Low               2                 4                   1
6  Task_6     High               6                 4                   3
7  Task_7   Normal               7                 4                   2

{'Task_0': 4.0, 'Task_1': 0.0, 'Task_2': 0.0, 'Task_3': 0.0, 'Task_4': 0.0, 'Task_5': 0.0, 'Task_6': 0.0, 'Task_7': 0.0}
--------------------------------------------------------------------------------

     Task Priority  Hours Estimate  Days To Deadline  Numerical Priority
0  Task_0     High             2.0                 1                   3
1  Task_1      Low             4.0                 1                   1
2  Task_2     High             2.0                 2                   3
3  Task_3   Normal             8.0                 2                   2
4  Task_4     High             4.0                 2                   3
5  Task_5      Low             2.0                 3                   1
6  Task_6     High             6.0                 3                   3
7  Task_7   Normal             7.0                 3                   2

{'Task_0': 2.0, 'Task_4': 2.0, 'Task_1': 0.0, 'Task_2': 0.0, 'Task_3': 0.0, 'Task_5': 0.0, 'Task_6': 0.0, 'Task_7': 0.0}
--------------------------------------------------------------------------------

     Task Priority  Hours Estimate  Days To Deadline  Numerical Priority
0  Task_0     High             0.0                 0                   3
1  Task_1      Low             4.0                 0                   1
2  Task_2     High             2.0                 1                   3
3  Task_3   Normal             8.0                 1                   2
4  Task_4     High             2.0                 1                   3
5  Task_5      Low             2.0                 2                   1
6  Task_6     High             6.0                 2                   3
7  Task_7   Normal             7.0                 2                   2

{'Task_2': 2.0, 'Task_4': 2.0, 'Task_0': 0, 'Task_1': 0, 'Task_3': 0.0, 'Task_5': 0.0, 'Task_6': 0.0, 'Task_7': 0.0}
--------------------------------------------------------------------------------

     Task Priority  Hours Estimate  Days To Deadline  Numerical Priority
0  Task_0     High             0.0                -1                   3
1  Task_1      Low             4.0                -1                   1
2  Task_2     High             0.0                 0                   3
3  Task_3   Normal             8.0                 0                   2
4  Task_4     High             0.0                 0                   3
5  Task_5      Low             2.0                 1                   1
6  Task_6     High             6.0                 1                   3
7  Task_7   Normal             7.0                 1                   2

{'Task_6': 4.0, 'Task_0': 0, 'Task_1': 0, 'Task_2': 0, 'Task_3': 0, 'Task_4': 0, 'Task_5': 0.0, 'Task_7': 0.0}
--------------------------------------------------------------------------------

     Task Priority  Hours Estimate  Days To Deadline  Numerical Priority
0  Task_0     High             0.0                -2                   3
1  Task_1      Low             4.0                -2                   1
2  Task_2     High             0.0                -1                   3
3  Task_3   Normal             8.0                -1                   2
4  Task_4     High             0.0                -1                   3
5  Task_5      Low             2.0                 0                   1
6  Task_6     High             2.0                 0                   3
7  Task_7   Normal             7.0                 0                   2
```
