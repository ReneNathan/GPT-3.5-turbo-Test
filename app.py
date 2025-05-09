from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Nova sintaxe


def gerar_descricao_ia(dados):
    try:
        prompt = f"""
        Gere uma descrição persuasiva em português para adoção de animal com estas informações:
        Nome: {dados['nome']}
        Tipo: {dados['animal']}
        Idade: {dados['idade']}
        Vacinado: {'Sim' if dados['vacinado'] else 'Não'}
        Características especiais: {dados.get('caracteristicas', 'Nenhuma informação adicional')}

        A descrição deve:
        - Ser natural e afetuosa
        - Destacar qualidades do animal
        - Incluir todos os dados relevantes
        - Ter no máximo 150 palavras
        """

        response = client.chat.completions.create(  # Sintaxe atualizada
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Você é um assistente especializado em redação para adoção de animais.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=200,
        )

        return response.choices[0].message.content.strip()  # Acesso alterado

    except Exception as e:
        return str(e)


# O restante do código permanece igual
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/gerar-descricao", methods=["POST"])
def handle_gerar_descricao():
    dados = request.get_json()

    if not all([dados.get("nome"), dados.get("animal"), dados.get("idade")]):
        return jsonify({"error": "Preencha todos os campos obrigatórios"}), 400

    descricao = gerar_descricao_ia(dados)

    if "Erro" in descricao:
        return jsonify({"error": descricao}), 500

    return jsonify({"descricao": descricao})


if __name__ == "__main__":
    app.run(debug=True)
