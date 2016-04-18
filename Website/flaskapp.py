from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
	return render_template('Website.html')


@app.route('/where')
def where():
	return render_template('where.html')

@app.route('/home')
def home():
	return render_template('Website.html')
@app.route('/pictures')
def pics():
	return render_template('Pictures.html')
	

if __name__ == '__main__':
	app.run(debug=True)
