from flask import Flask

app = Flask(__name__)
import views #ВАЖНО! БЕЗ Него не будет отображатсья страницы(404)
