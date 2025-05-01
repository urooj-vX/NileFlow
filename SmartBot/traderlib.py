#LOOP until timeout reached (ex. 2hrs)
#POINT ECHO: INITIAL CHECK
# check the position: ask the broker API if we have an open position with "asset"
    # IN: asset (string)
    # OUT: True (exists) / False (does not exist)

# check if tradable: ask the broker API if "asset" is tradable
    #IN: asset (string)
    #OUT: True (exists) / False (does not exist)

#GENERAL TREND (this is in series)
# load 30 min candles: demand the API the 30 min candles
    # IN: asset (or whatever the API needs), time range, candle size
    # OUT: 30 min candles (OHLC for every candle)

#perform general trend analysis: detect interesting trend (UP / DOWN / NO TREND)
    # IN: 30 min candles data (Close data)
    # OUT: UP / DOWN / NO TREND (string)
    #If no trend defined, go back to beginning to POINT ECHO

    #LOOP until timeout reached (ex. 30 mins)
    # POINT DELTA
    # STEP 1: load 5 min candles
        # IN: asset (or whatever the API needs), time range, candle size
        # OUT: 5 min candles (OHLC for every candle)
        #If failed then go back to POINT DELTA

    # STEP 2: perform instant trend analysis: confirm the trend detected by GT (General Trend) analysis
        # IN: 5 min candles data (Close data), output of the GT analysis (UP / DOWN string)
        # OUT: True (confirmed) / False (not confirmed)
        #If failed then go back to POINT DELTA

    # STEP 3: perform RSI analysis
        # IN: 5 min candles data (Close data), output of the GT analysis (UP / DOWN string)
        # OUT: True (confirmed) / False (not confirmed)
        #If failed then go back to POINT DELTA

    # STEP 4: perform stochastic analysis
        # IN: 5 min candles data (OHLC data), output of the GT analysis (UP / DOWN string)
        # OUT: True (confirmed) / False (not confirmed)
        #If failed then go back to POINT DELTA

#SUBMIT ORDER
#submit order(limit order): interact with broker API
    # IN: number of shares to operate with asset, desired price
    # OUT: True (confirmed) / False (not confirmed), position ID
    # If false, abort / go back to POINT ECHO

# check position: see if the position exists
    # IN: position ID
    # OUT: True (confirmed) / False (not confirmed)
    # If false, abort / go back to POINT ECHO

#LOOP until timeout reached (ex. ~8hrs)
#ENTER POSITION MODE: check the conditions in parallel
# ELIF check take profit -> close position
    #IN: current gains (earning money)
    #OUT: True / False

# ELIF check stop loss -> if True -> close position
    #IN: current gains (loosing money)
    #OUT: True / False

# ELIF check stochastic crossing. If True -> close position
    # STEP 1: pull 5 minutes OHLC data
        #IN: asset
        #OUT: True / False

    # STEP 2: see whether the stochastic curves are crossing
        #IN: OHLC data (5 min candles)
        #OUT: True / False

#GET OUT
#SUBMIT ORDER
#submit order (market): interact with broker API
    # IN: number of shares to operate with asset, position ID
    # OUT: True (confirmed) / False (not confirmed), position ID
    # If false, retry until it works

# check position: see if the position exists
    # IN: position ID
    # OUT: True (still exists) / False (does not exist)
    # If false, abort / go back to SUBMIT ORDER


# wait 15 min

#end
