import pandas as pd

dataset = pd.read_csv('GlobalLandTemperaturesByCity.csv', sep=',', encoding='utf-8')

dataset = dataset.drop(columns=['AverageTemperatureUncertainty', 'Latitude', 'Longitude'])
dataset = dataset.dropna()

dataset = dataset.rename(columns={'dt': 'Data', 'AverageTemperature': 'Temperatura Média', 'City': 'Cidade', 'Country': 'País'})
dataset['Data'] = pd.to_datetime(dataset['Data'])

def temperatura_media_cidade(dataset, data_inicial, data_final, cidade):

    '''
    
    Calcula a temperatura média de uma cidade em um período de tempo específico.

    Parâmetros:

    - dataset: DataFrame contendo os dados da tabela;
    - data_inicial: Data inicial do período de tempo informado;
    - data_final: Data final do período de tempo informado;
    - cidade: Nome da cidade selecionada.

    Tipos:

    - dataset: DataFrame;
    - data_inicial: str (Formato de YYYY-MM-DD);
    - data_final: str (Formato de YYYY-MM-DD);
    - cidade: str.

    Retorno:

    Retorna uma string contendo as informações da temperatura média da cidade informada e formatada para duas casas decimais.
    
    Em caso de uma cidade não encontrada no dataset, retorna uma mensagem informando que a cidade não foi encontrada.

    Em caso de informações incompletas para o cácula da temperatura, retorna uma mensagem informando que não há dados
    o suficiente para retorna a média.
        
    '''

    if cidade in dataset['Cidade'].values:
        dataset_final = dataset[
            (dataset['Data'] >= data_inicial) & 
            (dataset['Data'] <= data_final) &
            (dataset['Cidade'] == cidade)
        ]

        if not dataset_final.empty:
            
            temperatura_media = dataset_final['Temperatura Média'].mean()
            return f'A temperatura média entre o período selecionado foi de {temperatura_media:.2f}°C.'
        
        else:
            return 'Não há dados o suficiente para retornar a média.'
    
    else:
        return 'Cidade não encontrada no dataset.'

data_inicial = '2012-01-01' # Substitua pela data inicial que desejar
data_final = '2012-12-31' # Substitua pela data final que desejar
cidade = 'São Paulo' # Substitua pela cidade que desejar

temperatura_calculada = temperatura_media_cidade(dataset, data_inicial, data_final, cidade)

print(temperatura_calculada)