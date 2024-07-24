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

@dover.route('/docs/<page_type>')
def docs_page(page_type):
    if page_type == 'setting':
        page_title = 'Setting Guide'
        page_frame = 'https://docs.google.com/document/d/1TDTreos86OU8qP7nBU-jgVxFgf_PDH-aNohtZvMPeiE/pub?embedded=true'
    elif page_type =='houserules':
        page_title = 'House Rules'
        page_frame = 'https://docs.google.com/document/d/1HljO2WZ1dKUEDkkcUWdbelbRtR2MQGsfsZeFK01WbKE/pub?embedded=true'
    return render_template('docs.html', title = page_title, frame = page_frame)

if __name__ == '__main__':
    dover.run(debug=True)
