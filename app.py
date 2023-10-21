from flask import Flask, render_template, request
from flask_babel import Babel
import tg_photos_parse
import datetime
import json

app = Flask(__name__, static_url_path='/static')
babel = Babel(app)


app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'
app.config['LANGUAGES'] = ['en', 'ru']  # List of supported languages
app.config['BABEL_DEFAULT_LOCALE'] = 'en'  # Default language


def get_locale():
    # Get language from URL parameter or default to 'en'
    lang = request.args.get('lang', 'en')
    if lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    with open('media.json', 'r', encoding='utf-8') as json_file:
        media = json.load(json_file)

    artworks = tg_photos_parse.get_imgs('iriscot_arts')

    current_year = datetime.datetime.now().year
    user_language = get_locale()
    return render_template('index.html',
                           media=media,
                           artworks=artworks,
                           current_year=current_year,
                           user_language=user_language)


if __name__ == '__main__':
    app.run(debug=True)
