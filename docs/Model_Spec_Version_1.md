## 1. Input format

- Pattern that would be stored: price data in the last 24h, timeframe 1h
- Query: Price data in the last 12h
- Auxiliary input: price data in the last 12h, timeframe 15m (will be added after testing the performance of main input)
- Input shape:
    + Num sample: Amount of samples of the full dataset.
    + Num instance: Amount of instances per sample (sample length)
    + Num price: Amount of prices per instance (open, close, high, low)

## 2. Preprocess Input

- Not doing anything yet, just testing things out

## 3. Output format

- Price data in the last 24h, timeframe 1h

## 4. Metric

- Similarity between input and output

## 5. Model structure

- 1D conv (no need yet)
- Position encoding
- Hopfield pooling
- Fc
- Selu activation

