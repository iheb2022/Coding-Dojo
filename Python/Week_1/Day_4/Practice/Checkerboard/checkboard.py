from flask import Flask, render_template # type: ignore
app=Flask(__name__)

@app.route('/')
def default():
  return render_template('index.html', insidebox=8, outsidebox=8)

@app.route('/<int:outsidebox>')
def outsidebox(outsidebox):
  return render_template('index.html',insidebox=8, outsidebox=outsidebox)

@app.route('/<int:insidebox>/<int:outsidebox>')
def custombox(insidebox,outsidebox):
  return render_template('index.html', insidebox=insidebox ,outsidebox=outsidebox)

if __name__=="__main__":
  app.run(debug=True)

