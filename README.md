# TradingAgent

This repository is used to record the fight between me and the chaos of trading environments such as: Forex, Bitcoin, Securities

## 1. Repo Structure

We will mainly follow tensortrade back bone, which includes:
- Exchange: provides observations to the environment and executes the agent's trades.
- FeaturePipeline: optionally transforms the Exchange output into a more meaningful set of features before it is passed to the agent.
- ActionScheme (optional): converts the agent's actions into executable trades.
- RewardScheme (optional): calculates the reward for each time step based on the agent's performance.
- Model: process input data from FeaturePipeline and give us some meaningful outputs or actions.
But we will make some changes to this structure:
- There may be no ActionScheme because our agent could possibly be just a classifier or state estimator,...
- The same applies to RewardScheme because we won't force ourself to use Reinforcement Learning any more.

## 2. Model types:

### Input format

- Input format 1: sequence of prices data(normalized or standardized). Shape (N, 4) 
- Input format 2: sequence of open prices, close prices... Shape (4, N)
- I dont think the order of two input schemes above is really important here, but we must use experiments to verify that idea
- Time frame: 24h
- Side inputs: Basically the same input but in lower time frame (15 mins)
- Output: sequence of prices data in the next 8 hours (timeframe 1h)
- 

### How to process input

- We will try to use some normalization techiniques and matrix profiling methods
- Input must be quite clean and understandable before feeded to the model
- ... (to be continue)

### Possible model ideas

- We will use Hopefield Network as a state storage and build a classifier based on the result of the network
- Build a enegry-based model to evalute the state of the market

### Output options

- 1): predicted sequence price data of the next 24h (could be hard)
- 2): classification score of each class that the next sequece of price data will belong to: Bulling, Bearing, Side-way (too vague)
- 3): next trade action: buy, hold, sell, buy limit, sell limit.
- 4): approximately future price in the next 24h (only one price, not the whole sequence)
- 5): possible direction of the next price moves - multiple directions and their probability

## 3. Notes

- Model doesn't have to be a Machine Learning model, it can be anything as long as it do well with the dataset.
So it's more concise definition would be a mathematical model that we will define later.
- Currency type: BTC
- Dataframe: 1h

## 4. Logs

21-8-2020: Actually start this project, wrote some model design ideas.
14-9-2020: Start first baseline model, we will use Hopfield network as a pattern storage and query for future price sequence
15-9-2020: Improve model spec, start perform EDA first because its more important than testing Hopfield Network, 
Hopfield network is just a tool and we dont know for sure that we would rely on it after EDA

## 5. Install

- Environment: Python3.6+
- OS: Ubuntu 14+, Windows
- Run ```pip3 install -r requirements.txt```
- Download data from here: https://drive.google.com/drive/u/1/folders/1TcFK_nMnyr4weSWpA4OymY5Tme45k0Ig
- Extract and copy it to folder __data/eur_usd__
