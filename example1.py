from flask import Flask

app = Flask(__name__)

@app.route('/user/<userphrase>')

def FunTranslate(userphrase):
	inputtext = userphrase
	translated = yoda(inputtext)
	return translated

if __name__ == '__main__':
	app.run()

def yoda(original):
	from google.cloud import translate
	translate_client = translate.Clien()
	#text = u'Hello, world!'
	text = original
	target = 'ru'
	translation = translate_client.translate(text, target_language=target)
	yousaid = u'Text: {}'.format(text)
	finalWords = u'Translation: {}'.format(translation['translatedText'])
	return finalWords


