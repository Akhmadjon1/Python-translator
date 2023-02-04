#Translate text to another language
from translate import Translator

translator = Translator(from_lang='english', to_lang='korean')
translation =translator.translate('This is better and useful library')
print(translation)