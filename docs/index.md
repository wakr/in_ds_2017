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

Next plot gives an overview of current crime rates in Chicago, with the year 2017 omitted. 

<img src="tota_crime_rate.png"/>

The overall trend is descending, which is a good thing. However descending trend might be due many different factors as for example how the reporting of crime has changed during the years. It's also notable that in this data, no murders are not being counted in. This is because murders are so cevere crimes so they cannot be included grouped with milder crimes like _thievery_ or _assault_. Later, we will see that the there exists quite direct relationship between crimes and school safety. This is of course due to enviromental factors of ZIP-districts.

However, to see more detailed information about the state of crime in Chicago, we can plot the data per month as seen in the next plot. 

<img src="crime_rate_per_month.png"/>

The Seasonal changes are quite obvious and they are repeated every year. Overall trend is descending, hinting that crime rate is dropping year by year. Interestingly minimum and maximum months per year are the same for pretty much every year.  For example in 2010 lowest crime rate was in February and highest in August and in 2016 lowest was also in February and highest in August.

These two months are interestingly also among the coldest and warmest months in Chicago as seen here

![avg_temps](https://weather-and-climate.com/uploads/average-temperature-united-states-of-america-chicago.png)
Source: [https://weather-and-climate.com/uploads/average-temperature-united-states-of-america-chicago.png](https://weather-and-climate.com/uploads/average-temperature-united-states-of-america-chicago.png)



Individual crime types are visible in quite similar fashion as in overall trend of crimes. This is visible in the following plot, where all crime types are plotted (names excluded for clarity) 

<img src="crimes_per_crime_type.png"/>

Almost all crimes by crime type have decreased, the only exception being narcotics (blue curve).

---

We built a SARIMAX-model (Seasonal Autoregressive integrated moving average)
to forecast for the 2017. The result predictions for 2016 is visible here:

<img src="2016_predicted_crime_rate.png"/>

and overview of predicted values from 2014-2016:

<img src="2014_2016_predictions.png"/>

So in a general case, our model seems to work quite well and we can use this to predict 
the whole 2017. The forecast is visible in the next picture:

<img src="2017_forecasted.png"/>

<img src="2017_forecast_total_crime.png"/> 


### How crimes are distributed inside Chicago?

<img src="crimes_per_zip.png"/>

### Does there exists a possible quantitative relationship to schooling?

<img src="dropouts_chicago.png"/>

Droupout rate in whole Chicago is also [decreasing.](http://www.chicagotribune.com/news/ct-chicago-school-graduation-rate-increase-met-20170903-story.html)

<img src="safety_score.png"/>

Safety score is one measure in [5 Essentials survey](https://illinois.5-essentials.org/2017/). It measures student's perception of safety at school.
Lower safety score means lower perception of safety. As we can see comparing this plot to previous crime distribution plot, crimes and safety score are distributed quite similarly.


<img src="misconducts.png"/>

Misconduct rate is also from 5 Essentials survey. It's still unclear for us, if misconduct rate means percent of misconducting students or something else.
Both safety score and misconducts plots resemble crime plot.

## Conclusions about comparing crimes & school data



## To remember

Quotation from [news article](http://www.chicagotribune.com/news/local/breaking/ct-chicago-violence-first-three-months-met-20170330-story.html):
"Criminologists, however, caution against making comparisons in crime statistics month to month or even year to year, arguing that long-term trends give a truer picture of how violence changes over time."
