# Использование %

team1_num = 5
print('В команде %s участников: %s !' %('Мастера кода', team1_num))
team2_num = 6
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))

# Использование format():

score_2 = 42
print('Команда {} решила задач: {} !'.format('Волшебники данных', score_2))
team1_time = 18015.2
print('{} решили задачи за {} с !'.format('Волшебники данных', team1_time))

# Использование f-строк:

score_1 = 40
print(f'Команды решили {score_1} и {score_2} задач.')
challenge_result = 'победа команды Мастера кода'
print(f'Результат битвы: {challenge_result} !')
tasks_total = 82
time_avg = 350.4
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')