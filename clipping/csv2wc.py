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
    return ' '.join(random.sample(l, len(l)))


def generate_wordcloud(text, font_path=None):
    return WordCloud(background_color='white', width=590, height=700,
                     font_path=font_path, max_font_size=None,
                     regexp=r"\w[\w'|()._-]+"  # include symbols
                     ).generate(text)


def mono_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % 0  # monochrome


if __name__ == '__main__':
    font_path = '/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc'  # macOS
    csv_path = './wordlist.csv'
    color_output_path = './clipping_color.png'
    mono_output_path = './clipping_mono.png'

    text = randomize(conv_csv_wctext(csv_path))
    wc = generate_wordcloud(text, font_path)
    wc.to_file(color_output_path)
    wc = wc.recolor(color_func=mono_color_func)
    wc.to_file(mono_output_path)
