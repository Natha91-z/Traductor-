from translate import Translator

Translator = Translator(from_lang='spanish', to_lang='english')

txt = input('Que deseas traducir?')

res = Translator.translate(txt)

print(res)