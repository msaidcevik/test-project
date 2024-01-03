from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/electronics')
def electronics():
    return render_template('electronics.html')

@app.route('/Laptops')
def Laptops():
    return render_template('Laptops.html')

@app.route('/Mobiles')
def Mobiles():
    return render_template('Mobiles.html')

if __name__ == '__main__':
    app.run(debug=True)

