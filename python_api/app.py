from flask import Flask, request, jsonify
from flask_cors import CORS
from main import gerarAmbiente

app = Flask(__name__)
CORS(app)  # Adicione esta linha para configurar o suporte ao CORS


@app.route('/')
def index():
    return 'Minha primeira API!'

@app.route('/api/exemplo', methods=['POST'])
def exemplo():
    dados = request.get_json()
    final = dados.get('final')
    inicio = dados.get('inicio')
    tipo = dados.get('tipo')
    return gerarAmbiente(inicio, final, tipo)

if __name__ == '__main__':
    app.run(debug=True)
