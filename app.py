import pandas as pd
from flask import Flask, render_template


def datos():
    dato = pd.read_csv('db2.csv', on_bad_lines='skip', delimiter=';', low_memory=False)
    df = pd.DataFrame(dato)
    print(df.head())
    print(df)
    return df

app = Flask(__name__)

@app.route('/')
def index():
    db = datos()
    df_agrupado = db.groupby('vernacularName')['individualCount'].sum().reset_index()
    df_html = df_agrupado.to_html(classes='data',header='true')
    return render_template('indexx.html',tables=[df_html])


#Handler: manejo de Errores
@app.errorhandler(404)
def error_404(error):
    return render_template('404.html', error=error)

