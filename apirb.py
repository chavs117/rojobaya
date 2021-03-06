from sanic import Sanic
from sanic.response import json
from pyArango.connection import *

app = Sanic("App Name")

conn = Connection(arangoURL="http://localhost:1234",username="root", password="doorandy123")
db = conn["interruptor"]
@app.route("/guardarData", methods=["POST"])
async def echo(request):
	if request.json:
		doc=(request.json)
		bind = {"doc": doc}
		aql = "INSERT @doc INTO estados LET newDoc = NEW RETURN newDoc"
		queryResult = db.AQLQuery(aql, bindVars=bind)
		return json(request.json)
	return json({"R":"NO fue un json"})
	
@app.get('/ObtenerData')
async def handler(request,res):
	res.send({"estados"})


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000)
