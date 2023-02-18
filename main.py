from novalabs.utils.backtest import BackTest

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

from ta.trend import macd_diff
pd.options.mode.chained_assignment = None


class MACD_HIST (BackTest):

    def __init__(
        self,
        
        exchange: str,
        strategy_name: str,
        candle: str,
        list_pair,
        start: datetime,
        end: datetime,
        fees: float,
        start_bk: float,
        leverage: int,
        max_pos: int,
        max_holding: timedelta,
        quote_asset: str = 'USDT',
        geometric_sizes: bool = False,
        
        # Specific to Backtest Analysis
        save_all_pairs_charts: bool = False,
        update_data: bool = False,
        plot_exposure: bool = False,
        key: str = "",
        secret: str = "",
        passphrase: str = "",
        
        tp_sl_delta: float = 0.005
    ):

        self.tp_sl_delta = tp_sl_delta

        BackTest.__init__(
            self,
            exchange = exchange,
            strategy_name = strategy_name,
            candle = candle,
            list_pair = list_pair,
            start = start,
            end = end,
            fees = fees,
            start_bk = start_bk,
            leverage = leverage,
            max_pos = max_pos,
            max_holding = max_holding,
            quote_asset = quote_asset,
            geometric_sizes = geometric_sizes,
            
            # Specific to Backtest Analysis
            save_all_pairs_charts = save_all_pairs_charts,
            update_data = update_data,
            plot_exposure = plot_exposure,
            key = key,
            secret = secret,
            passphrase = passphrase
        )

    def build_indicators(self, df: pd.DataFrame) -> pd.DataFrame:

        df['macd'] = macd_diff(close=df['close'])

        return df

    def entry_strategy(self, df: pd.DataFrame) -> pd.DataFrame:

        df['entry_signal'] = np.nan
        df['take_profit'] = np.nan
        df['stop_loss'] = np.nan
        df['position_size'] = 1

        long_conditions = (df['macd'] > 0) & (df['macd'].shift(1) < 0)
        short_conditions = (df['macd'] < 0) & (df['macd'].shift(1) > 0)
        df['entry_signal'] = np.where(long_conditions, 1, np.where(short_conditions, -1, np.nan))

        df['take_profit'] = np.where(df['entry_signal'] == 1, df['close'] * (1 + self.tp_sl_delta), np.where(df['entry_signal'] == -1, df['close'] * (1 - self.tp_sl_delta), np.nan))
        df['stop_loss'] = np.where(df['entry_signal'] == 1, df['close'] * (1 - self.tp_sl_delta), np.where(df['entry_signal'] == -1, df['close'] * (1 + self.tp_sl_delta), np.nan))

        return df

    def exit_strategy(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Args:
            df: Dataframe returned bu self.entry_strategy()
        Returns:
            All information necessary for exit points
        """
        
        # df['exit_signal'] = np.where(df['exit_point'] < self.exit_probability, 1, 0)
        df['exit_signal'] = np.nan

        return df
    


strat = MACD_HIST(
    exchange = "binance",
    strategy_name = 'MACD',
    candle = '1h',
    list_pair = ['BTCUSDT', 'ETHUSDT', 'ADAUSDT', 'SOLUSDT', 'DOGEUSDT'],
    start =  datetime(2021, 1, 1),
    end =  datetime(2023, 1, 1),
    fees = 0.0004,
    start_bk = 1000,
    leverage = 5,
    max_pos = 2,
    max_holding = timedelta(hours=12),
    quote_asset = 'USDT',
    geometric_sizes = True,
    
    # Specific to Backtest Analysis
    save_all_pairs_charts = False,
    update_data = False,
    plot_exposure = False,
    key = "",
    secret = "",
    passphrase = "",
    
    tp_sl_delta = 0.05
)


    
    
stats = strat.run_backtest(save=False)