import statsmodels.tsa.stattools as ts
import yfinance as yf  #import data via Yahoo


def cointegrated_pairs(data):
    n =  (len(data.columns) -1)
    stocks = data.iloc[:,1:].columns.values #pulls all stock names 
    data = data.to_numpy()
    pvalue_matrix = np.zeros((n,n),dtype = float)
    pairs = np.empty((n*n,2),dtype=object)
    m = 0
    #loop through all possilbe combintions of stocks ie 3!=6
    for i in range(0,n):
        for j in range(0,n):
            S1 = data[:,i+1]
            S2 = data[:,j+1]
            result = ts.coint(S1,S2)
            pvalue_matrix[i,j] = result[1]
            #storing all paris in matrix form
            if (result[1] < 0.05) & (i!=j):
                pairs[m,0] = stocks[i]
                pairs[m,1] = stocks[j] 
                m = m +1
    return pvalue_matrix,  pairs



today = datetime.today()
sp_list = ['SPY','DIA']
offset = max(1, (today.weekday() + 6) % 7 - 3)
timed = timedelta(offset)
today_business = today - timed
print("d1 =", today_business)
today = today_business.strftime("%Y-%m-%d")
start = '2020-01-01' 
end = today
print('S&P500 Stock download')
spy = yf.download(sp_list, start,end)

scipy.stats.pearsonr(S1,S2)

result = ts.coint(S1,S2)
result[1]

def PnL(signals):
    signals_np = np.array(signals) # converts our pandas df into numpy array
    nu_shift = np.array(signals['nu'].shift(periods=1)) #lag timeseries by 1 trading day
    vol_shift = np.array(signals['volatility'].shift(periods=1)) #lag timeseries by 1 trading day
    negvol_shift = np.array(signals['negvolatility'].shift(periods=1)) #lag timeseries by 1 trading day
    vec_sig = np.zeros(len(signals))
    for i in range(len(signals)-1):
        #innovation > volatilty & innovation+1 < volatilty+1
        if (signals_np[i,0] > signals_np[i,1]): # t1 & t0 SHORT asset when current t changes to nu > volatlity
            vec_sig[i] = -1
        elif(signals_np[i,0] < signals_np[i,2]): #LONG assets when current t changes to nu < negvol
            vec_sig[i] = 1
        else:
            vec_sig[i] = 0
    # at the current day we enter our position
    vec_sig = pd.DataFrame({'vec_sig':vec_sig})
    return vec_sig

def backtesting(vec_sig,S1,S2):
    num_shares_y = vec_sig['vec_sig'].iloc[1:] * 1000
    num_shares_x = vec_sig['vec_sig'].iloc[1:] * -1000
    #forward fill x & y postion 
    PLX = num_shares_x.values * S1.pct_change().iloc[1:].values # difference of column X 
    PLY = (num_shares_y.values)  * S2.pct_change().iloc[1:].values #difference of column y 
    profit_loss = PLX + PLY
buy_hold_x = 1000
    buy_hold_y = 1000
    buy_hold_x = buy_hold_x *  S1.pct_change().iloc[1:] # 
    buy_hold_y = buy_hold_y *  S2.pct_change().iloc[1:]
    buy_hold   = buy_hold_x + buy_hold_y    
    buy_hold = sum(buy_hold)
    profit_loss = sum(profit_loss)
return profit_loss , buy_hold
