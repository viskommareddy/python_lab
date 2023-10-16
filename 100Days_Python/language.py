from flask import Flask, request
import openai_secret_manager
import openai

app = Flask(__name__)
secrets = openai_secret_manager.get_secret("openai")

openai.api_key = secrets["api_key"]

def translate_text(text, source_lang, target_lang):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Translate the following text from {source_lang} to {target_lang}: {text}",
        temperature=0.5,
        max_tokens=1024,
        n=1,
        stop=None,
        timeout=10,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].text.strip()

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data['text']
    source_lang = data['source_lang']
    target_lang = data['target_lang']
    translated_text = translate_text(text, source_lang, target_lang)
    return {'translated_text': translated_text}
