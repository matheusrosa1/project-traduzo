from deep_translator import GoogleTranslator
from flask import Blueprint, render_template, request
from models.language_model import LanguageModel

translate_controller = Blueprint("translate_controller", __name__)


@translate_controller.route("/", methods=["GET", "POST"])
def index():
    languages = LanguageModel.list_dicts()

    text_to_translate = "O que deseja traduzir?"
    translate_from = "pt"
    translate_to = "en"
    translated = "What do you want to translate?"

    if request.method == "POST":
        text_to_translate = request.form.get("text-to-translate", "")
        translate_from = request.form.get("translate-from", "pt")
        translate_to = request.form.get("translate-to", "en")

        if text_to_translate:
            try:
                translated = GoogleTranslator(
                    source=translate_from, target=translate_to
                ).translate(text_to_translate)
            except Exception as e:
                translated = f"Erro na tradução: {str(e)}"

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )
