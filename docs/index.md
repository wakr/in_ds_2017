# Chicago and its crimes

<img src="http://maps-chicago.com/img/0/chicago-neighborhood-map.jpg" width="400" height="400"/>

Chicago community areas. Source: [http://maps-chicago.com/img/0/chicago-neighborhood-map.jpg](http://maps-chicago.com/img/0/chicago-neighborhood-map.jpg)

## Background

Chicago is being notorious for its violent crime rate, topping many major US city in violent crimes [1]. 

Crimes are usually not evenly distributed across a city, and a person who might be interested to move to Chicago would probably want to see which areas are worse inside Chicago. Based on that data, a new candidate could compare between areas inside Chicago and choose a more crime-free district to live. The data about these bad areas gives also insight to the police department and helps to pinpoint crime clusters, which often are formed due to sociological differences i.e. poverty and education. 

Taking a look at just shootings happened during this year in Chicago shows couple of these clusters 

<img src="chic_shootings.png" width="400" height="400"/>

Source: [http://crime.chicagotribune.com/chicago/shootings](http://crime.chicagotribune.com/chicago/shootings)

Tackling with these crime clusters would make the city safer, even though there might be internal problems [in the police department](http://www.reuters.com/article/us-chicago-police/chicagos-detective-force-dwindles-as-murder-rate-soars-idUSKCN10Z13A). The other problem are [guns](http://edition.cnn.com/2017/01/02/us/chicago-murder-rate-2016-visual-guide/index.html) which are hard to get rid of, even with strict gun laws.

However, data about crime types and counts provides valuable information about the current state of crimes in Chicago. We believe that smaller crimes, create *butterfly effect* which will ultimately reflect to more serious crimes over time.

The data we use are crimes in non-murder crimes from 2010 to 2016 and school inquiries/statistics to form a forecast for 2017. This raises couple of questions that can be answered
* How crime rate in Chicago is going to change in future?
* How crimes are distributed inside Chicago?
* Does there exists a possible relationship to schooling?


[1] https://www.usnews.com/news/articles/2016-09-19/chicago-drives-uptick-in-murders-national-crime-rate-stays-near-historic-lows


## Data

We use data from 2010 to 2016 offered by [the city of Chicago](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2). There are over 2 million rows in our filtered data set.
Every row contains at least crime type, date, latitude and longitude.

## Why

We wish to create an easy-to-understand visualization of the current non-murder crimes and also explore possible quantitative relations
between crimes and school dropouts.

## How

Seeing ZIP-codes. We omit the violent crimes i.e. murders. 

## Results

### How crime rate in Chicago is going to change in future?

<img src="tota_crime_rate.png"/>


<img src="crime_rate_per_month.png"/>

Seasonal changes repeated every year. Overall trend is descending. Interestingly minimum and maximum
months per year are the same for 2010 and 2016 and for almost all years. 
For example in 2010 lowest crime rate was in february and highest in august and in 2016 lowest was also in february and highest in august.

<img src="crimes_per_crime_type.png"/>

Almost all crimes by crime type have decreased: the only exception is narcotics (blue curve).

### How crimes are distributed inside Chicago?


### Does there exists a possible relationship to schooling?

<img src="dropouts_chicago.png"/>

Droupout rate in whole Chicago is also decreasing.

## To remember
