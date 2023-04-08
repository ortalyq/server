from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# URL вашего приложения на компьютере
url = 'http://2.135.66.150:8080/receive_data'
print('hello world')

@app.route('/receive_data', methods=['POST'])
def receive_data():
    # Получение данных из формы
    photo = request.files['photo']
    text = request.form['text']

    # Отправка данных на ваше приложение на компьютере
    files = {'photo': photo.read()}
    data = {'text': text}
    response = requests.post(url, files=files, data=data)

    if response.status_code == 200:
        return 'Данные успешно отправлены на ваш компьютер!'
    else:
        return 'Произошла ошибка при отправке данных на ваш компьютер.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
