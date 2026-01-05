Each test in every case is executed 10000 times

For each sorting algorithm test was done on the array of 10,100 and 1000 elements

Time is shown in seconds

|Algorithm name| Data | Pattern |             Time(s) |
|:------------:|:----:|:-------:| -------------------:|
|Boyer-Moore   |Text 1|valid    |1.6233163999859244   |
|Boyer-Moore   |Text 2|valid    |2.5674346999730915   |
|Boyer-Moore   |Text 1|made up  |2.4362504000309855   |
|Boyer-Moore   |Text 2|made up  |3.4608921001199633   |
|KMP           |Text 1|valid    |9.039448900148273    |
|KMP           |Text 2|valid    |11.712761600036174   |
|KMP           |Text 1|made up  |14.31343310000375    |
|KMP           |Text 2|made up  |20.635187400039285   |
|Rabin-Karp    |Text 1|valid    |23.182723599951714   |
|Rabin-Karp    |Text 2|valid    |30.01080509996973    |
|Rabin-Karp    |Text 1|made up  |36.175092899939045   |
|Rabin-Karp    |Text 2|made up  |52.79901509988122    |

### Conclusion
From test results we can see that Boyer-Moore Algorithm perfomed the best for both texts with both finable pattern as well as made-up pattern. So, Boyer-Moore Algorithm was the fastest in general.