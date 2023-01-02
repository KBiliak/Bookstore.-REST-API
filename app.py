from flask import Flask, request

app = Flask(__name__)

@app.get('/query-example')
def query_example():
    return 'Query String Example'

@app.get('/form-example')
def form_example():
    return 'Form Data Example'

@app.post('/json-example')
def json_example():
    body = request.get_json()
    print("body:", body)
    print("name:", body["name"])
    return 'JSON Object Example'

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)