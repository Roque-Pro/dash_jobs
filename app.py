from flask import Flask, render_template, jsonify
from flask_cors import CORS  # Para permitir CORS, caso necessário

# Inicializando o Flask
app = Flask(__name__)

# Permite que as requisições sejam feitas de origens diferentes (útil no desenvolvimento)
CORS(app)

# Rota inicial - carrega o HTML
@app.route("/")
def index():
    return render_template("index.html")

# Rota de API com dados fictícios
@app.route("/api/dashboard")
def dashboard_data():
    # Dados de exemplo (podem ser substituídos por dados reais de um banco de dados ou de outra API)
    data = {
        "vagas_criadas": 1999,
        "vagas_fechadas": 1792,
        "vagas_abertas": 207,
        "eficacia": 12.5,
        "backlog": 77.29,
        "tempo_medio": 58,
        "empresas": ["XP Import", "Gpower Analytics", "Garha T&D e BI", "Findaclick Arts"],
        "vagas_criadas_empresa": [490, 506, 485, 460],
        "vagas_fechadas_empresa": [400, 430, 410, 460],
        "setores": ["Contratos A", "GMNT", "Suprimentos", "Contratos B"],
        "vagas_criadas_setor": [490, 506, 485, 460],
        "vagas_fechadas_setor": [400, 430, 410, 460],
        "meses": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "vagas_criadas_tempo": [79, 62, 60, 65, 59, 61, 61, 68, 64, 70, 61, 68],
        "vagas_fechadas_tempo": [40, 54, 50, 49, 51, 59, 60, 61, 60, 58, 61, 57],
        "recrutadores": ["Zulmira Alves", "Tiago Mendes", "Ana Vasquez"],
        "vagas_criadas_recrutador": [50, 55, 51],
        "vagas_fechadas_recrutador": [45, 44, 46]
    }
    return jsonify(data)

# Rodando o Flask
if __name__ == "__main__":
    app.run(debug=True)
