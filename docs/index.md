# Chicago and its crimes

<img src="http://maps-chicago.com/img/0/chicago-neighborhood-map.jpg" width="400" height="400"/>

Chicago community areas. Source: [http://maps-chicago.com/img/0/chicago-neighborhood-map.jpg](http://maps-chicago.com/img/0/chicago-neighborhood-map.jpg)

## Background

Chicago is notorious for its violent crime rate, topping many other major US cities in violent crimes [1]. We want to easily visualize the current situation in Chicago and provide an info-packet about crimes in Chicago. This can be useful information for many different groups; people who are thinking about moving inside Chicago into a safe area, police who get dispatched to specific areas can prepare for a specific crime or just for the people who are interested in what are the possible causes of Chicago's high crime rates. 

Crimes overall are usually not evenly distributed across one city. A person interested in moving into a new city would possibly want to review different areas and choose the most suitable for him/her. The data about these high-crime areas also gives insight into the police department and helps in pinpointing crime clusters, which are often formed due to sociological differences i.e. poverty, lack of education and low income. 

Taking a look at just the shootings that happened during this year in Chicago shows couple of these clusters. Mainly residing in the western and southern part of Chicago

<img src="chic_shootings.png" width="400" height="400"/>

Source: [http://crime.chicagotribune.com/chicago/shootings](http://crime.chicagotribune.com/chicago/shootings)

Tackling these clusters is one way to make city safer. But unfortunately in Chicago, there also exists internal problems [in the police department](http://www.reuters.com/article/us-chicago-police/chicagos-detective-force-dwindles-as-murder-rate-soars-idUSKCN10Z13A). Another problem are [guns](http://edition.cnn.com/2017/01/02/us/chicago-murder-rate-2016-visual-guide/index.html) which are hard to get rid of or to even regulate, even with strict gun laws.

However, data about crime types and counts provides valuable information about the current state of crimes in Chicago. We believe that smaller crimes create a *butterfly effect* which will ultimately reflect to more serious crimes over time.

The data we use in this visualization are non-homicide crimes from 2010 to 2016 to form a forecast for 2017. We also take little look at education data, which is in form of surveys made for the students or data about dropout rates. 

We raise couple of questions and try to answer then with the crime data
* How the crime rate in Chicago will change in the future?
* How the crimes are distributed inside Chicago?
* Does there exist a possible relationship to education?
* What are the possible causes for Chicagos high crime rates?


[1] https://www.usnews.com/news/articles/2016-09-19/chicago-drives-uptick-in-murders-national-crime-rate-stays-near-historic-lows


## Data

We use crime data from 2010 to 2016 offered by [the city of Chicago](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2). The reason for this is that we want to see the situation as it stands in the 2010s. 

There are over 2 million rows in our filtered data set. Every row contains the crime type, date, latitude and longitude with other fields including e.g. description, police patrol areas and the location of the crime. 

As briefly mentioned before, our data does not contain any murders. This is because we don't want to mix up crimes involving, for example, theft with murder crimes, because their impact to society is very different.

We also determined the ZIP districts of crimes from the coordinates given, as this data wasn't in the original dataset.


## Results

### How crime rate in Chicago is going to change in future?

Next plot gives an overview of current crime rates in Chicago, with the year 2017 omitted: 

<img src="tota_crime_rate.png"/>

The overall trend in criminal activity is descending, which is a good thing. However, this descending trend might be due many different factors as for example how the reporting of crime has changed during the years. It's anyhow interesting, as gun crimes and violence were increasing in Chicago but the overall amount isn't. 

However, to see more detailed information about the state of crime in Chicago, we can plot the data per month as seen in the next plot: 

<img src="crime_rate_per_month.png"/>

The Seasonal changes are quite obvious and they repeat every year. Overall trend is descending, hinting that crime rate is dropping year by year. Interestingly, the minimum and maximum months per year are the same for pretty much every year.  For example in 2010 the lowest crime rate was in February and highest in August, and in 2016 the lowest was also in February and highest in August.

These two months are among the coldest and warmest months in Chicago as seen here:

![avg_temps](https://weather-and-climate.com/uploads/average-temperature-united-states-of-america-chicago.png)
Source: [https://weather-and-climate.com/uploads/average-temperature-united-states-of-america-chicago.png](https://weather-and-climate.com/uploads/average-temperature-united-states-of-america-chicago.png)



Individual crime types are visible in quite a similar fashion as in overall trend of crimes. This is visible in the following plot, where all crime types are plotted (names excluded for clarity):

<img src="crimes_per_crime_type.png"/>

Almost all crimes by crime types have decreased, the only exception being Narcotics (blue curve), but there are no major outliers or types that don't follow the overall trend. It's thus safe to say that all non-violent crimes in Chicago are in a descending trend.

---

For forecasting the overall crime amount, we built a SARIMAX-model (Seasonal Autoregressive integrated moving average)
to forecast for the year 2017. The model automatically adjusts to seasonal changes with a given trend. The resulting predictions for 2016 are visible here:

<img src="2016_predicted_crime_rate.png"/>

and the overview of predicted values from 2014-2016:

<img src="2014_2016_predictions.png"/>

So in a general case, our model seems to work well and we can use this to predict the whole of 2017. The forecast is visible in the next picture:

<img src="2017_forecasted.png"/>

Unsurprisingly, the year 2017 is forecasted to be very similar to 2016. This is mostly as the descending of the overall trend has relaxed from what it was between 2012-2014, so the trend has stabilized slightly between 2014-2017. 

In the next plot, the crime rate with the forecasted total amount in 2017 is visible: 


<img src="2017_forecast_total_crime.png"/> 


### How crimes are distributed inside Chicago?

From our data, we created the following plot using Bokeh, which represents the overall percentages of crimes committed in Chicago divided into specific ZIP-codes:

<img src="crimes_per_zip.png"/>

As can be seen from the plot, the criminal activity in Chicago is heavily divided into two main areas: Garfield Park, Humboldt Park and Austin in the west, and Englewood, Auburn and Pullman in the south.

See interactive plot [here](plot.html), which also contains the specific locations for each crimes inside the ZIP-codes.

In the next plot, we have summed up the top 10 types of crimes (not including homicides) committed in Chicago during our sample of the years 2010 - 2016:

![](crime_type_dist.png)

From the plot, we can easily see that Thefts and Batteries are the leading types of crimes in Chicago, followed by Criminal Damage (To Property) and Narcotics -offenses, with other crimes trailing behind these.

Using this information about the types of crimes committed in Chicago, alongside the ZIP-code data we have, we could pinpoint the most common crimes inside each ZIP-code using aggregated data, as shown in the next plot:

![](crime_type_zip.png)

Not surprisingly, we can see the crime rate divide mirrored in this plot, with the less serious Theft-type crimes being prevalent in areas of low crime rates, and Batteries and Narcotics being the top crimes in high crime rate areas.

What was surprising, however, was that the area around Garfield Park, Humboldt Park and Austin had Narcotics as the top aggregated crime instead of Battery. Considering that Narcotics were only the 4th most prevalent type of crime we found in Chicago during our sample, this is an interesting find, and could be looked at in more detail in future tasks.

### Does a possible quantitative relationship to schooling exist?

In addition to just analyzing the crime data, we wanted to see if crimes have correlations for example with school or health data.
We found the following dropout data from [Chicago Public Schools -page](http://cps.edu/SchoolData/Pages/SchoolData.aspx), and we explain below the following image what dropout rate means.

<img src="dropouts_chicago.png"/>

The dropout rate in Chicago is also [decreasing.](http://www.chicagotribune.com/news/ct-chicago-school-graduation-rate-increase-met-20170903-story.html)
Dropout rate is calculated for 5-year high schools in the following way: For 2016, researchers compared the amount of students who started in 2011 and the amount of students who graduated in 2016 and then calculated the dropout rate.

<img src="safety_score.png"/>

Safety score is one measure in [5 Essentials survey](https://illinois.5-essentials.org/2017/). It measures the students' perception of safety at their schools.
Lower safety score means lower perception of safety. As we can see, comparing this plot to the previous crime distribution plot, crimes and safety score are distributed quite similarly.


<img src="misconducts.png"/>

Misconduct rate is also from 5 Essentials survey. It's still unclear for us whether or not the misconduct rate means percent of misconducting students or something else.
Both the safety score and misconduct plots resemble the crime plot.

### Conclusions about comparing crimes and school data

When comparing crime data and school data (dropout rates, safety scores, misconducts) statistically, it's very unlikely that differences in zip codes have come to exist coincidentally. We still cannot say whether the crimes committed are affecting school life or the other way around.

Before drawing more conclusions than just "we found that these distributions resemble each others", we need more knowledge in research methods of criminology or social sciences.

## Story about ethics and value
### What should we do with our results and is value only for apartment owners true value?

Our main conclusions in data analysis were that crime counts per Zip code vary a lot, and that school safety and misconducts are in a quantitative relationship with the crimes. Chicago has two large areas with a large amount of crimes and low school safety. What should we do now with our results? We can for example:

- Make a machine learning model which predicts apartment prices based on the amount of crimes
- Make other machine learning models which benefits different kinds of owners: apartment owners, car owners, entrepreneurs, parents who can decide which school to choose for their children
- Just looking the numbers, we can also make a model which predicts the amount of crimes based on a percentage of african americans in a given area

Image below is from [Wikipedia](https://en.wikipedia.org/wiki/Demographics_of_Chicago)

<img src="african_american.png"/>

![](http://i.imgur.com/xZoKnTa.gif)

Source: [https://www.huffingtonpost.com/2013/01/29/chicago-racial-demographi_n_2575921.html](https://www.huffingtonpost.com/2013/01/29/chicago-racial-demographi_n_2575921.html)

So we think that the value of, for example, predicting apartment prices is not of true value for the society at large; it's just extra value for the owners.

### Regional police-involved shootings and the race gap in income

When we studied Chicago's regional polarization more, we found interesting plots about police misconducts and the race gap in income. We learned that if you want to get good picture of what's happening in a geographical area, it's good to take a look at data from as many fields of society as possible. 

Image below describes distribution of police-involved shootings and it's from [Chicagotribune](http://www.chicagotribune.com/news/ct-map-where-chicago-police-shot-at-people-20160826-htmlstory.html):

<img src="policeshootings.png"/>

Image below describes the use of force misconducts by police, and it's from [Citizens Police Data Project](https://cpdb.co/data/LjgX1o/citizens-police-data-project)

<img src="police_force.png"/>

<img src="race_gap.png"/>

## To remember

Quotation from [news article](http://www.chicagotribune.com/news/local/breaking/ct-chicago-violence-first-three-months-met-20170330-story.html):

<blockquote>"Criminologists, however, caution against making comparisons in crime statistics month to month or even year to year, arguing that long-term trends give a truer picture of how violence changes over time."</blockquote>
Our data is from years 2010-2016, but our data source [Chicago Data Portal](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2) has same data already from 2001. We decided to concentrate on the years 2010-2016 because of lengthy data preprocessing times for larger sets, but our future research topic would be to analyze data from a longer time period.

### More information of Chicago regional inequality:
- [Brookings article](https://www.brookings.edu/blog/social-mobility-memos/2015/12/21/the-most-american-city-chicago-race-and-inequality/)
- [Employment status in Chicago](https://statisticalatlas.com/place/Illinois/Chicago/Employment-Status)
- [Food Stamp distribution in Chicago](https://statisticalatlas.com/place/Illinois/Chicago/Food-Stamps)
