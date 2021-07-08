# Candlestick Pattern Analyzer
The program aims to efficiently analyze the candlestick chart/patterns to determine which stocks are consolidating or breaking out. The program is built in Python and uses Python’s Technical Analysis Library (TA-lib) and Flask framework.

## Functions
<ol>
  <li> Analyze the dataset to determine which stocks are consolidating and breaking out. </li>
  <li> Web based technical scanner to display the stocks which have formed a certain pattern. </li>
  <li> Display stocks with their charts in which the selected pattern has been found. </li>
  <li> The end candle of the pattern will be indicated with a small red arrow. </li>
</ol>

## Tech Stack
<ol>
<li> Python 3 </li>
<ul>
    <li> Flask Framework </li>
    <li> Technical Analysis Library </li>
    <li> Yahoo Finance Library </li>
</ul>
<li> HTML 5 </li>
<li> CSS3 </li>
<ul><li> Bootstrap 4 </li></ul>
<li> JavaScript </li>
</ol>

## Additional Information
### What is Flask ?
Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.
<br>Documentation: https://flask.palletsprojects.com/en/1.1.x/

### What is Technical Analysis Library ?
TA-Lib is an open-source python library that is used in analyzing the stock market's historical data like share price, volume, etc. in order to predict the future price or the market direction so that we can make our investments accordingly.
<br>Documentation: https://ta-lib.org/hdr_lnk.html

## Technical Scanner
The technical scanner will scan for the data of various stocks and provide all the stocks which has formed a particular pattern along with its candlestick chart like in the below image which shows the `Doji` pattern formed in the stock `COALINDIA`.

## Usage
<ul>
  <li>Clone the repository and then execute the 'flask run' command on terminal in the project directory.</li>
  <li>The project will be accessible on localhost.</li>
  <li>Access the project on http://127.0.0.1:5000/ instead of http://localhost:5000/ after starting the flask server.</li>
</ul>

### Navigate to the Scanner Page
<ol>
  <li>Update the Dataset</li>
  <ul>
    <li>Click on Fetch Button.</li>
    <b>Note: This will update the dataset.</b>
  </ul>
  <br>
  <li>To Check stocks with certain patterns:</li>
  <ul>
    <li>Select the pattern from the drop down list.</li>
    <li>Click on the Scan button after selecting the pattern.</li>
    <li>The results will be displayed according to the pattern selected.</li>
  </ul>
  <br>
  <li>To Get the Stocks according to their State:</li>
  <ul>
    <li>After updating the dataset, click on the State button.</li>
    <li>The result will be displayed in a web modal.</li>
  </ul>
</ol>
<b>Note: The pattern will be indicated by a small red arrow which will appear above the candle where the pattern has completed.</b>