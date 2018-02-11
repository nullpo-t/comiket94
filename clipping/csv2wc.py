import random
import csv
from wordcloud import WordCloud


def conv_csv_wctext(csv_path):
    s = ''
    with open(csv_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            s += (row['word'] + ' ') * int(row['count'])
    return(s)


def randomize(text):
    l = text.split(' ')
    return ' '.join(random.sample(l,len(l)))


def generate_wordcloud(text, save_path, font_path=None):

    WordCloud(background_color='white', width=590, height=700,
              font_path=font_path, max_font_size=None,
              regexp=r"\w[\w'|()._-]+"  # include symbols
              ).generate(text).to_file(save_path)


if __name__ == '__main__':
    font_path = '/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc'  # macOS
    csv_path = './wordlist.csv'
    output_path = './clipping.png'

    text = randomize(conv_csv_wctext(csv_path))
    generate_wordcloud(text, output_path, font_path)

