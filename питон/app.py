import os
import fitz
from flask import Flask, render_template, request, redirect, url_for, abort, send_from_directory, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_EXTENSIONS'] = ['.pdf']
app.config['UPLOAD_PATH'] = 'uploads'

@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('index.html', files=files)

@app.route('/', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            return "Трубуется формат .PDF", 400
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    return '', 204

@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)


@app.route('/square/', methods=['POST'])
def square():
    dick = 'Получается могу любые данные вывести?'




    # конкретный кусок кода, который потом станет модулем:
    pdf_document = "./uploads/pol_1.pdf"
    doc = fitz.open(pdf_document)

    page1 = doc.loadPage(0)
    page1text = page1.getText("text")
    if page1text == '':
        print('Ничего')
    print(page1text)

    list_of_lines = page1text.split('\n')
    print(list_of_lines)
    for line in list_of_lines:
        if line.upper().replace(" ", "") == 'ПОЛОЖЕНИЕ':  # в верхний регистр + убираем пробелы
            dick = 'Успех'  # Я ебать предполагаю, что это положение
    # ============================================================================================


    data = {'square': dick}
    data = jsonify(data)
    return data


if __name__ == '__main__':
    app.run(debug=True)