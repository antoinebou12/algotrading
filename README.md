# Algorithmic Trading

Developing Algorithmic Trading Strategies Based Leveraging Novalabs.ai Backtesting Tool

This guide will help you develop algorithmic trading strategies leveraging the Novalabs.ai backtesting tool.

## I - Create a new python environment

If you haven't installed Anaconda yet, please download and install it (https://www.anaconda.com/) before proceeding with the following steps:

Create a new environment:

```shell
conda create --name algotrading python=3.8
```

Activate the environment:

```shell
conda activate algotrading
```

## II - Install Libraries

Install the required libraries by running:

```shell
pip install -r requirements.txt
```

## III - Watch Novalabs.ai Tutorial

Before getting started, we recommend watching the Novalabs.ai tutorial, available at:
https://www.youtube.com/watch?v=1r8eDuDf3Qo&ab_channel=BryanSichoix

## IV - Tips

Here are some tips to help you during the development process:

- Look at the execution of "run_backtest" of the library "novalabs"
- The exposure plot takes a really long time to execute => Should be equal to false plot_exposure
- When the performance graph is poping up on your display, you have to close it to continu the execution

We hope this guide helps you develop successful trading strategies using Novalabs.ai!

## V - Example

Go to the folder "example" and run jupyter notebook

```shell
cd example
pip3 install jupyter jupyterlab
jupyter notebook
```
