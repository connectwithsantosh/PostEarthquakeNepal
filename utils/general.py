from pathlib import Path
from configs.translations import TRANSLATIONS


def get_project_root():
    return Path(__file__).parent.parent

# Helper function for translations
def translate(text_key, lang):
    return TRANSLATIONS[lang].get(text_key, text_key)