# EMC-NorCal-SE-AlexaChallenge-2016
Code and design docs for Alexa Challenge

The intention of this app is to be able to query EMC install base information
from the Amazon Alexa API

# Examples

Input: "Alexa, what customers are in my install base?"
Output: "The following customers are in your install base: CDPH, LDC, CHP, DMV, FTB,...."

Input: "What is installed at CDPH?"
Output: "CDPH has the following hardware installed: 3 VNX5600s, 3 XtremIO, 2 DataDomain 
4500s', etc..."

Input: "What are the serial numbers of CDPH's XtremIO's?"
Output: "XtremIO serial numbers: FM123456, FM987543, FM45678"

These are just a few examples. More will be written here with actual usage.

# Notes

importing CSV file derived from emc opsconsole

creating python wrapper functions that are hard-coded for specific queries and will add
more as we go along

test app usage: "python main.py"


# Resources

Alexa tutorial: https://developer.amazon.com/public/community/post/TxDJWS16KUPVKO/New-Alexa-Skills-Kit-Template-Build-a-Trivia-Skill-in-under-an-Hour

Using sqlite3 database: https://www.sqlite.org

ask-alexa-pykit: https://github.com/anjishnu/ask-alexa-pykit/tree/python_lambda_0.3_release

http://tobuildsomething.com/2015/08/14/Amazon-Echo-Alexa-Tutorial-The-Definitive-Guide-to-Coding-an-Alexa-Skill/
