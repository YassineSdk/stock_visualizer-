import pandas as pd 
import streamlit as st
import yfinance as yf 
import plotly.graph_objs as go
import matplotlib.pyplot as plt 




st.set_page_config(page_title="stock visualizer",
                   page_icon="📈",
                   layout='wide')

st.title('STOCK DASHBOARD')


st.sidebar.header('INDICE AND DATE ')
tickers = ('TSLA','AAPL','MSFT','KO','ETH_USD')
dropdown = st.sidebar.multiselect(' Choose the stock name',tickers)

start = st.sidebar.date_input('START',value = pd.to_datetime('2024-01-01') )
end  = st.sidebar.date_input('END  ',value = pd.to_datetime('today') )

def relative_return(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod() - 1
    cumret = cumret.fillna(0)
    return cumret


col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

if len(dropdown) > 0 :
    #df = yf.download(dropdown,start,end )["Adj Close"
    df = relative_return(yf.download(dropdown,start,end )["Adj Close"])
    st.header(f'Returns of {format(dropdown)}')
    c = st.container(border = True)
    c.line_chart(df)

    for idx, stock in enumerate(dropdown):
        data = yf.download(stock,start,end)
        data.reset_index(inplace=True)
        plt.figure(figsize=(10,8))
        Candl = go.Figure(data=[go.Candlestick(
        x=data['Date'],
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close']
)])
        Candl.update_layout(
        title=f'{format(stock)} Candlestick Chart ',
        xaxis_title='Date',
        yaxis_title='Price',
        xaxis_rangeslider_visible=False,
        xaxis=dict(showgrid=True),  
        yaxis=dict(showgrid=True)
        
)
 
        
        if idx == 0:
            col1.plotly_chart(Candl)
        elif idx == 1:
            col2.plotly_chart(Candl)
        elif idx == 2:  
            col3.plotly_chart(Candl)
        elif idx == 3: 
            col4.plotly_chart(Candl)        


        











