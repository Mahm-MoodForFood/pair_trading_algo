# Development Log

This is a simple development log that I can use to keep track of progress and to highlight updates and changes with the project. 
  
 ## 07/12/2021
 Created the repository with the readme file and added a cointegartion file. I plan on changing things up drasticly as it is obviously not good practice to develop any piece of software in this manner. 
 ## 08/12/2021
I will first need to find all of the instruments listed by Trading-212 (T212) as I will be testing the algoritham on T212. I won't be uploading the scraping script but I will be making available the list of instruments. 

##28/01/2022
Currently the cointegration algoritham works. It will simply test between SPY and DIA and use similar it will exicute based on trading signals simialar to boilinger bands. From the readme.md file this is very far from the final result. I will need to create functions to find the price of the payoff for put and call options. 

There are many reasons as to why this isn't a good model at the moment such as; bid/ask spread is not taken in account, using end of the day price not indtraday price, broker fees, smooth transaction etc... 

Therefore the algoritham still is very incomplete before I can test different scenarious and techniques as described in the readme.md file. I am at the same time working on my own personal algorithams which I am debating on whether to show the results and release the code for. 
