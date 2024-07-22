from os import path
from flask import Flask, render_template, redirect, url_for, request, flash
from datetime import date

dover = Flask(__name__)
#app.config['SECRET_KEY'] = 'IMustNotFearFearIsTheMindKiller

@dover.route('/')
def indexPage():
    return render_template('index.html', title = 'New Dover (By Night Studios Troupe Game)')

@dover.route('/schedule.html')
def schedule():
    return render_template('schedule.html', title = 'Game Schedules')

@dover.route('/setting.html')
def setting():
    return render_template('setting.html', title = 'Setting Document')

@dover.route('/houserules.html')
def houserules():
    return render_template('houserules.html', title = 'House Rules')

if __name__ == '__main__':
    dover.run(debug=True)
