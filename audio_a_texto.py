import speech_recognition as sr
import sys


def audio_to_text(audio, language):
	print('Procesando audio...')
	re = sr.Recognizer()
	with sr.AudioFile(audio) as source:
		info_audio = re.record(source)
		return re.recognize_google(info_audio, language=language)


def audio_processed(text, inputFile):
	output_name = inputFile.split('.')[0]
	outputFile = open(f'{output_name}.txt', 'w')
	print('Convirtiendo a texto...')
	outputFile.write(text)
	outputFile.close()


audio = sys.argv[1]
idioma = ['es-ES', 'en-EN']
language = int(input('Selecciona el idioma del audio:\n\n1 - Español\n2 - Ingles\n* '))

text = audio_to_text(audio, idioma[language - 1])
audio_processed(text, audio)
print('Convertido a texto exitosamente!')
