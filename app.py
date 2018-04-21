from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/pokemon/<ext>', methods=['GET'])
def poke(ext):
	req = requests.get('https://www.pokeapi.co/api/v2/pokemon/'+ext)
	r = req.json()

	if(req.status_code != 200):
		return "<h1>Whoops</h1>"

	if (r["name"] == ext):
		return "<h1>The pokemon with id {} is {}</h1>".format(ext, r["id"])

	elif(r["id"] == int(ext)):
		return "<h1>{} has id {}</h1>".format(ext, r["name"])


if __name__ == '__main__':
    app.run()
