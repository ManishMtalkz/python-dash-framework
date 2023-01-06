import pandas as pd
import numpy as np
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px


df = pd.read_csv("sentdata.csv")
print(df.head())


# Pwrovider and its frequency in the dataset-------
df2 = df.groupby('Provider').size().sort_values(ascending=False).reset_index()
df2.rename(columns =  {0:'status'},inplace = True)


app = dash.Dash()   

def status():
    print(df2)

    long_df = px.data.medals_long()
    fig = px.bar(df2, x="Provider", y="status",  title="Long-Form Input")
    return fig

app.layout = html.Div(id = 'parent', children = [
    html.H1(id = 'H1', children = 'provider and its frequency', style = {'textAlign':'center',\
                                            'marginTop':40,'marginBottom':40}),

        
        dcc.Graph(id = 'line_plot', figure = status())    
    ]
                     )



if __name__ == "__main__":
    app.run_server()