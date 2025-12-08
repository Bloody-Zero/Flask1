from flask import Flask, render_template

app = Flask(__name__)

# ГЛАВНАЯ СТРАНИЦА
@app.route('/')
def main_menu():
    return render_template('index.html')

#  ЛАБА 5: НАСЛЕДОВАНИЕ
@app.route('/lab5')
def lab5():
    return render_template('home.html')

#  ЛАБА 3: ВЫВОД ДАННЫХ
@app.route('/circle_area/<float:radius>/')
def circle_area(radius):
    return render_template('index.html', r=radius, pi=3.14)

@app.route('/circle_area/10.0/')
def circle_area_10():
    return render_template('index.html', r=10.0, pi=3.14)

@app.route('/tuple_calc/')
def tuple_calc():
    numbers = (15, 25, 2, 3, 9, 19)
    return render_template('index.html', numbers=numbers)

@app.route('/round_number/<string:val>/')
def round_number(val):
    return render_template('index.html', val=val)

@app.route('/round_number/1.618/')
def round_golden():
    return render_template('index.html', val='1.618')

# ЛАБА 4: КАЛЬКУЛЯТОР

@app.route('/calc/<float:a>/+/<float:b>/')
def calc_float_plus(a, b):
    return render_template('index.html', a=a, b=b, op='+', task='calc')

@app.route('/calc/<float:a>/-/<float:b>/')
def calc_float_minus(a, b):
    return render_template('index.html', a=a, b=b, op='-', task='calc')

@app.route('/calc/<float:a>/*/<float:b>/')
def calc_float_multiply(a, b):
    return render_template('index.html', a=a, b=b, op='*', task='calc')

@app.route('/calc/<float:a>/:/<float:b>/')
def calc_float_divide(a, b):
    return render_template('index.html', a=a, b=b, op=':', task='calc')

@app.route('/calc/<float:a>/**/<float:b>/')
def calc_float_power(a, b):
    return render_template('index.html', a=a, b=b, op='**', task='calc')

# ЦЕЛЫЕ числа (ДОБАВЬ ЭТО!)
@app.route('/calc/<int:a>/+/<int:b>/')
def calc_int_plus(a, b):
    return render_template('index.html', a=float(a), b=float(b), op='+', task='calc')

@app.route('/calc/<int:a>/-/<int:b>/')
def calc_int_minus(a, b):
    return render_template('index.html', a=float(a), b=float(b), op='-', task='calc')

@app.route('/calc/<int:a>/*/<int:b>/')
def calc_int_multiply(a, b):
    return render_template('index.html', a=float(a), b=float(b), op='*', task='calc')

@app.route('/calc/<int:a>/:/<int:b>/')
def calc_int_divide(a, b):
    return render_template('index.html', a=float(a), b=float(b), op=':', task='calc')

@app.route('/calc/<int:a>/**/<int:b>/')
def calc_int_power(a, b):
    return render_template('index.html', a=float(a), b=float(b), op='**', task='calc')

# ===== ЛАБА 4: МАКРОСЫ =====
@app.route('/macros_test/')
def macros_test():
    values = ["apple", "banana", "cherry", "date", "elderberry"]
    action = "search"
    x = 42
    y = 3.14
    return render_template('index.html',
                          values=values,
                          action=action,
                          x=x,
                          y=y,
                          task='macros')

# ===== ЛАБА 1: МАРШРУТИЗАЦИЯ =====
@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/another_page/')
def another_page():
    return 'Еще одна страница'

@app.route('/contact/')
def contact():
    return 'contact information'

@app.route('/index_old/')
def index_old():
    return 'index'

@app.route('/albums/<int:album_number>/')
def albums(album_number):
    return f'The {album_number} album.'

@app.route('/albums/<int:album_number>/<song_number>/')
def songs(album_number, song_number):
    return f'The {album_number} album and {song_number} musician performer.'

@app.route('/calculate/<int:num1>/<int:num2>/')
def calculate(num1, num2):
    result = num1 ** num2
    return str(result)

# ===== ТЕСТОВЫЕ МАРШРУТЫ =====
@app.route('/template_test/')
def template_test():
    return render_template('index.html', message='Привет из Flask!')

@app.route('/error_test/')
def error_test():
    return render_template('non_existent.html')

# ===== ОБЩИЕ МАРШРУТЫ (В САМОМ КОНЦЕ!) =====
@app.route('/<int:number>/')
def next_number(number):
    return str(number + 1)

@app.route('/<int:num1><operation><int:num2>/')
def calculate_expression(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == ':' or operation == '/':
        if num2 == 0:
            return 'Ошибка: деление на ноль'
        result = num1 / num2
    elif operation == '**':
        result = num1 ** num2
    else:
        return 'Ошибка: неизвестная операция'
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)

# python main.py - запуск