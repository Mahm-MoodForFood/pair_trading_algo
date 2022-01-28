# pair_trading_algo

This is the first algoritham I have made public. It is already widely known in industry so I hope it will provide myself and others to help. This is a running project that I will come back to over time and eventually complete and to continiously update overtime. I will also order the repository to easily find different versions of the algoritham. I wish to also test this strategy on the DeFi market. 

###Please read the log.md file for updates on the project.

## Brief Description:
- Chaotic map K-mean Clustering to identify different pairs - This is in my opinion the best option for finding pairs as it does not require any prior knowledge of the cluster. To test whether this two pairs are correctly identified as pairs, the "found pairs" will be tested using the Pearson Correlation Coefficient and Cointegration. Again this is a starting point and over time this may change but I will highlight the changes in this file and any other accompanying files.
-  Idenify Entry Points - This is where I will be most experimenting as I would like to test the best entry point methods and whether certian strategies perform better during different market scenarios. If correlation is found between the different market "periods" such as a bearish, bullish, etc I would like it if the algoritham adjusts to it. 
-  Identifying Exist Points - Similar to the above point but applied to exit points.
-  Risk - Risk is something I haven't explored that much and it is something that I will like to test to to ensure that the algoritham does not overexpose itself. Using a Walk-Forward-Analysis and Monte-Carlo Simulations I believe is the best way to mitigate curve-fitting and to identify a risk profile. 
-  Conclusion - I would like to take each iteration of the algoritham and improve it in some way so that this becomes learning process for me to develop my skills. 

## Other Notes
I will try to make this algoritham easy to use and plan on using it on a custom made API for Trading-212 I have developed. The project may have stalls in its progress as I am a student and will not be working on this full time.

# Disclamer
I am not liable for any losses or damages occured by the use of the algoritham. The algoritham is for educational purposes only. If you choose to use the algoritham, do so at your own discretion and please note that it may not behave as presented and may result in significant financial damage. 
