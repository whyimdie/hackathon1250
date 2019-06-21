from aiogoogletrans import Translator
translator = Translator()
import asyncio
loop = asyncio.get_event_loop()
print(loop.run_until_complete(translator.translate('Hello World.')))
print(loop.run_until_complete(translator.translate('My Name is Thao!.',dest ='vi',src='en')))
print(loop.run_until_complete(translator.translate('astrobiology!', dest = 'vi', src = 'en')))
print(loop.run_until_complete(translator.translate('Nowadays technology is increasingly being used to monitor what people are saying and doing (for example, through cellphone tracking and security cameras). In many cases, the people being monitored are unaware that this is happening.Do you think the advantages of this development outweigh the disadvantages?!', dest = 'vi', src = 'en')))
a = loop.run_until_complete(translator.translate('Thao is so handsome', dest = 'vi', src = 'en'))
print(a)
print('This is a original form: ',a.origin)
print('This is a translated form: ',a.text)
#translator = Translator(service_urls=[
