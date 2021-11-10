import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt
import plotly.express as px

class Bitcoin:
    def __init__(self):
        self.bitcoin = 'BTC-USD'
        self.cripto_df = pd.DataFrame()

    def _get_data(self):
        start_data = self._set_date()
        self.cripto_df['BTC-USD'] = data.DataReader(name='BTC-USD', data_source='yahoo', start=start_data)['Close']
        return self.cripto_df

    def _set_date(self):
        day =  int(input('Digite o dia inicial para o grafico: '))
        month = int(input('Digite o mês inicial para o grafico: '))
        year = int(input('Digite o ano inicial para o grafico: '))
        if day < 10:
            day = f'0{day}'
        if month < 10:
            month = f'0{month}'
        if year < 22:
            year += 2000
        date = f'{year}/{month}/{day}'
        return date

    def _see_completed_data(self):
        title = input('Digite um titulo para o grafico (Não obrigatorio): ').title()
        df = self._get_data()
        self.fig = px.line(df, y="BTC-USD", title=title)
        self.fig.show()

    def _see_smaller_data(self):
        title = input('Digite um titulo para o grafico (Não obrigatorio): ').title()
        df = self._get_data()
        self.cripto_df.plot(title=title)
        plt.show()

    def _see_percentual_return(self):
        cripto_df = self._get_data()
        self.cripo_df_normalizated = cripto_df.copy()
        for i in self.cripo_df_normalizated.columns[:]:
            self.cripo_df_normalizated[i] = (self.cripo_df_normalizated[i] / self.cripo_df_normalizated[i][0]) * 100
        print(f'Retorno percentual\n{self.cripo_df_normalizated}')
        self.cripo_df_normalizated.plot(title='Retorno percentual')
        plt.show()
