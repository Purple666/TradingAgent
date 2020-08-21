# TradingAgent

This repository is used to record the fight between me and the chaos of trading environments such as: Forex, Bitcoin, Securities

## Agent Brief Design

### 1. Repo Structure

We will mainly follow tensortrade back bone, which includes:
- Exchange: provides observations to the environment and executes the agent's trades.
- FeaturePipeline: optionally transforms the Exchange output into a more meaningful set of features before it is passed to the agent.
- ActionScheme: converts the agent's actions into executable trades.
- RewardScheme: calculates the reward for each time step based on the agent's performance.
- Model: process input data from FeaturePipeline and give us some meaningful outputs or actions.
But we will make some changes to this structure:
- There may be no ActionScheme because our agent could possibly be just a classifier or state estimator,...
- The same applies to RewardScheme because we won't force ourself to use Reinforcement Learning any more.

### 2. Algorithms

#### 2.1. Model 1

We will use Hopefield Network as a state storage and build a classifier based on the result of the network

#### 2.2. Model 2

Build a enegry-based model to evalute the state of the market

### 3. Notes

- Model don't has to be a Machine Learning model, it can be anything as long as it do well with the dataset.
So it's more concise definition would be a mathematical model that we will define later.
- Currency type: BTC
- Dataframe: 1h
### 4. Logs
21-8-2020: Actually start this project, wrote some model design ideas.
