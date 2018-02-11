import csv
from wordcloud import WordCloud


def conv_csv_wctext(csv_path):
    s = ''
    with open(csv_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            s += (row['word'] + ',') * int(row['count'])
    return(s)


def generate_wordcloud(text, save_path,
                       font_path='/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc'):

    WordCloud(background_color='white', width=600, height=800,
              font_path=font_path, max_font_size=None,
              regexp=r"\w[-|\w']+"
              ).generate(text).to_file(save_path)


if __name__ == '__main__':
    s = conv_csv_wctext('wordlist.csv')
    generate_wordcloud(s, 'clipping.png')
