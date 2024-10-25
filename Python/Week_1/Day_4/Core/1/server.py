from flask import Flask, render_template
app=Flask(__name__)

@app.route('/play')

def play():
  return render_template('index.html', box_count=3)

@app.route('/play/<int:x>')
def custom(x):
  return render_template('index.html', box_count=x)

@app.route('/play/<int:x>/green')
def green(x):
  return render_template('seconde.html',box_count=x)


if __name__=='__main__':
  app.run(debug=True)