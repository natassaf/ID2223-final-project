# ID2223-final-project
An MLOPS pipeline for predicting cryptocurrency prices.

Athanasia Farmaki, farmaki@kth.se

Michail Roussos, michailr@kth.se

GitHub Pages URL: https://natassaf.github.io/ID2223-final-project/

# Problem Description

We implemented an MLOPS pipeline for predicting Solana prices. As input we are using historical Solana prices, Bitcoin prices and the Fear and Greed index. We saved all the data in Hopsworks. We created a GitHub Actions Workflow so that every day we fetch the new data and make new predictions. We are also creating some graphs that are also updated daily.

## Data

We downloaded historical data for Bitcoin and Solana from url [1] in the sources and stored it locally. We also get all the fear and greed index info from url [2] in the sources. We created three feature groups, one for solana, one for bitcoin and one for the fear and greed index. We start by storing in the respective feature groups the historical data. Then everyday that the workflow is executed the data is updated with recent values, before we make predictions.

## Tools

The framework we are using for the model is tensorflow's keras, sklearn for the scalers and the metric's calculation and matplotlib and seaborn for the plots.

## Method

Predictions are generated using an LSTM model, which is manually trained. Each day, when the workflow is executed, the model forecasts prices for the next 10 days. Updated plots are also created to visualize the latest data trends.

Long Short-Term Memory (LSTM) is a type of recurrent neural network (RNN) architecture designed to effectively model sequential or time-series data. It was specifically developed to address the shortcomings of traditional RNNs such as the vanishing/exploding gradients during training. We chose LSTM for this task because it is particularly well-suited for time-series prediction problems like forecasting cryptocurrency prices. We use 15 time steps as input and we set the number of hidden states to 30 for the LSTM layer. On top of the LSTM layer we add a Dense Layer with 10 Neurons to enable the modelling of non-linear relationships. The last linear layer is used to return the predictions of 10 days and thus we add 10 neurons on the last layer.  


## Instructions

1. Get the code from the repository.
2. Go to the 1st URL from the sources and create an API key.
3. Go to Hopsworks.com and create an account and an API key.
4. You need to create an python env (e.g. conda env) based on the 'requirements.txt' file.
5. You need to set as environment variables the two keys as "HOPSWORKS_API_KEY" and "CRYPTO_API_KEY".
6. Alternatively you can create a ".env" file and add the two keys there, but adjustments may be needed in the files.
7. Run the files with the following order "feature_backfill", "feature_pipeline", "training_pipeline", "inference_pipeline" and "plots".
8. If you want to run the workflow in github you need to also create the two keys in the repository secrets.

## Sources
[1] https://developers.cryptocompare.com/documentation/data-api/spot_v1_historical_days

[2] https://alternative.me/crypto/fear-and-greed-index/#api


