from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import PyPDF2
# Función para leer el contenido de un archivo de texto
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text
# Función para extraer texto de un archivo PDF
def extract_text_from_pdf(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_number in range(len(reader.pages)):
            text += reader.pages[page_number].extract_text()
        return text

# Leer el contenido del archivo PDF
article = extract_text_from_pdf('rimas_y_leyendas.pdf')

# Tokenización y eliminación de palabras de parada
tokens = [w for w in word_tokenize(article.lower()) if w.isalpha()]
no_stops = [t for t in tokens if t not in stopwords.words('spanish')]

# Crear un objeto Counter para contar la frecuencia de cada palabra
countedNoStops = Counter(no_stops).most_common(100)

# Crear un objeto WordCloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(dict(countedNoStops))

# Visualizar la WordCloud
plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Nube de palabras de Rimas y Leyendas")
plt.show()

print("Selected Tokens")
print(tokens)            
countedTokesn=Counter(tokens)
countedNoStops=Counter(no_stops). most_common(20)
CommonTk=countedTokesn.most_common(10)
print("Common tokens on Rimas y Leyendas")
print(CommonTk)
print("No Strops")
print(countedNoStops)
words, counts = zip(*countedNoStops)
# Rotar las etiquetas del eje x en 45 grados
# Añadir etiquetas sobre las columnas
for i, count in enumerate(counts):
    plt.text(i, count + 0.5, str(count), ha='center', va='bottom')
plt.title("Palabras más empleadas en Rimas y Leyendas: Becker")    
plt.xticks(rotation=45)
plt.bar(words, counts)
plt.xlabel("words")
plt.ylabel("counts")
plt.show()



# Leer el contenido del archivo "quijote.txt"
quijote_text = read_text_file('quijote.txt')
#quijote_text = read_text_file('MountyScene01.txt')

# Tokenización y eliminación de palabras de parada para "quijote.txt"
quijote_tokens = [w for w in word_tokenize(quijote_text.lower()) if w.isalpha()]
quijote_no_stops = [t for t in quijote_tokens if t not in stopwords.words('spanish')]

# Crear un objeto Counter para contar la frecuencia de cada palabra en "quijote.txt"
quijote_counted_no_stops = Counter(quijote_no_stops).most_common(100)

# Crear un objeto WordCloud para el texto de "quijote.txt"
quijote_wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(dict(quijote_counted_no_stops))

# Visualizar la WordCloud de "quijote.txt"
plt.figure(figsize=(10, 8))
plt.imshow(quijote_wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Nube de palabras de Don Quijote")
plt.show()


# Tokenización y eliminación de palabras de parada
tokensQ = [w for w in word_tokenize(quijote_text.lower()) if w.isalpha()]
no_stopsQ = [t for t in tokensQ if t not in stopwords.words('spanish')]

# Crear un objeto Counter para contar la frecuencia de cada palabra
countedNoStopsQ = Counter(no_stopsQ).most_common(20)

print("Selected Tokens")
print(tokensQ)            
countedTokensQ = Counter(tokensQ)
CommonTkQ = countedTokensQ.most_common(10)
print("Common tokens on Don Quijote")
print(CommonTkQ)
print("No Stops")
print(countedNoStopsQ)
wordsQ, countsQ = zip(*countedNoStopsQ)

# Graficar las palabras más empleadas
plt.figure(figsize=(10, 6))
plt.bar(wordsQ, countsQ)
plt.title("Palabras más empleadas en Don Quijote de la Mancha: Cervantes")    
plt.xlabel("Palabras")
plt.ylabel("Frecuencia")
plt.xticks(rotation=45, ha='right')
for i, v in enumerate(countsQ):
    plt.text(i, v + 5, str(v), ha='center', va='bottom')
plt.tight_layout()
plt.show()