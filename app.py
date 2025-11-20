import os
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configuração da API Key
try:
    GOOGLE_API_KEY = os.getenv('GEMINI_API_KEY')
    if not GOOGLE_API_KEY:
        # Fallback para teste local se a variável não existir (opcional)
        print("Aviso: GEMINI_API_KEY não encontrada nas variáveis de ambiente.")
    
    if GOOGLE_API_KEY:
        genai.configure(api_key=GOOGLE_API_KEY)
        print("Google Gemini configurado com sucesso.")
    
    # Configurações de segurança
    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_ONLY_HIGH"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_ONLY_HIGH"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_ONLY_HIGH"}
    ]

    
    system_prompt = """
    Você é a "Laren", uma assistente de bem-estar e saúde mental da empresa LTAKN.
    
    SUA MISSÃO:
    Analisar dados de funcionários e sugerir melhorias de saúde mental.
    
    SUA PERSONA:
    * Empática, profissional e direta.
    * Responda sempre em Português do Brasil.
    * Se o assunto fugir de "trabalho", "saúde" ou "bem-estar", diga gentilmente que não pode ajudar.
    """

    # Inicializa o modelo
    # Inicializa o modelo
    model = genai.GenerativeModel(
        model_name="models/gemini-pro-latest", # <--- CORRIGIDO
        safety_settings=safety_settings,
        # system_instruction=system_prompt # REMOVA ou COMENTE esta linha se der erro, pois o gemini-pro antigo usa o prompt na mensagem, não na config
    )

except Exception as e:
    print(f"Erro na configuração da IA: {e}")
    model = None

@app.route('/chat', methods=['POST'])
def handle_chat():
    if model is None:
        return jsonify({"erro": "A IA não foi configurada corretamente (verifique a API Key)."}), 500

    try:
        data = request.json
        # O Python espera receber {"mensagem": "..."}
        if not data or 'mensagem' not in data:
            return jsonify({"erro": "JSON inválido. Envie o campo 'mensagem'."}), 400

        user_message = data['mensagem']
        
        # Envia para o Gemini
        response = model.generate_content(user_message)
        
        # Devolve para o Java {"resposta": "..."}
        return jsonify({"resposta": response.text})

    except Exception as e:
        print(f"Erro no processamento: {e}")
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)