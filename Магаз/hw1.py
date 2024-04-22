from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/clothing')
def clothing():
    return render_template('category.html', category='Одежда')

@app.route('/shoes')
def shoes():
    return render_template('category.html', category='Ботинки')

@app.route('/jacket')
def jacket():
    return render_template('product.html', product='Куртка')

if __name__ == '__main__':
    app.run(debug=True)