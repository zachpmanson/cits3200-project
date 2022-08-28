from translate import Translator

languages = ['fr', 'es', 'zh-CN', 'ja', 'it', 'ru', 'de', 'id']

text = input('Enter the text would you like to be translated:')

for language in languages:
    translator = Translator(provider='libre', from_lang='en', to_lang='language')
    translation = translator.translate(text)
    print(f'{language}:{translation}')