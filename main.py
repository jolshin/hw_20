from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

if __name__ == '__main__':
    if calculate_salary():
        print('calculate_salary() is OK')

    if get_employees():
        print('get_employees() is OK')

    print(f'Текщее время: {datetime.now()}')
