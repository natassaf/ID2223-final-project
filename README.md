# ID2223-final-project
An MLOPS pipeline for predicting cryptocurrency prices.

Athanasia Farmaki, farmaki@kth.se

Michail Roussos, michailr@kth.se


# Solana Price Prediction Dashboard


## Solana Price Predictions
Here we can see the price predictions for Solana from our model.
![Price_predictions](./img/solana_predictions_plot.png)



## Model Performance Monitoring
Here we can see a comparison between our predictions and the actual values.
![Hindcast](./img/solana_predictions_plot.png)



## Correlation HeatMap
Here we have the correlation heatmap for the open values of Solana, Bitcoin and Fear and Greed index.
![HeatMap](./img/sln_btc_fng_heatmap.png)



## Trend Analysis
Here we have the trend analysis for the open values of Solana (actual and predictions), Bitcoin and Fear and Greed index.
![Trend_analysis](./img/trend_analisis.png)


# Description

We implemented an MLOPS pipeline for predicting Solana prices. As input we are using historical Solana prices, Bitcoin prices and the Fear and Greed index. We saved all the data in Hopsworks. We created a GitHub Actions Workflow so that every day we fetch the new data and make new predictions. We are also creating some graphs that are also updated daily.

## Data

We downloaded historical data for Bitcoin and Solana from the first site in the sources and stored it locally. We also get all the fear and greed index info from the second url in the sources. We created three feature groups, one for solana, one for bitcoin and one for fear and greed index.

## Sources
[1] https://developers.cryptocompare.com/documentation/data-api/spot_v1_historical_days
[2] https://alternative.me/crypto/fear-and-greed-index/#api