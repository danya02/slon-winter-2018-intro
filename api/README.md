#TL;DR: [this script](solution.py)
AKA "The War of the Standards".

This is one of those things that seem simple, and would in an ideal world be simple, but in actuality is very difficult due to how different organizations handle their data.

The problem, of course, is the simple truth that we all have to accept:

APIs are weird.

Yandex provides a [thoroughly spiffy](https://tech.yandex.ru/maps/doc/geocoder/desc/concepts/About-docpage/) (and free!) geocoder service.
They also have a curious [weather API](https://tech.yandex.ru/weather/), but won't let you use it unless you tell them why you need to.
But [OpenWeatherMap](http://openweathermap.org/) do have [a public API](http://openweathermap.org/api) (that requires an API key even for free access, which is annoying).
Unfortunately, the geocoder doesn't output IDs that correspond to OpenWeatherMan's ones, but a hackaround with exchanging latitude and longitude seems to work reasonably well.

And only *then* come the questions of how to calculate distance between points on a sphere (I settled on equirectangular approximation),
how to test if it is raining, which of the cities is the closest one that has no rain, how to accurately convert the coords
of the city into a human-readable name AND make sure that the geocoder doesn't get confused about the object that we get in the end - ET CETERA!

And to cap it all off, it turns out that there are nullable parameters in the OpenWeatherMap output, so the program
can crash if the closest 50 cities either have rain or have the required param nulled, i.e the program's performance, unlike so many cases where it is a hyperbole,
*literally depends on the weather*.

APIs are weird.