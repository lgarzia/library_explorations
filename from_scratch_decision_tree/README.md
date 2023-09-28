Objective: Decision trees host a simple and powerful concept of finding and cutting on information. 
I intend to deepen my intuition by walking through logic from scratch. 

Also - Compare Usual Approach (articles, codes, etc.) versus Assistant AI

[Decision Tree From Scratch](https://medium.com/swlh/decision-tree-from-scratch-a72069240293)
[Decision Trees for Dummies](https://medium.com/analytics-vidhya/decision-trees-for-dummies-a8e3c00c5e2e)
Classification versus Regression

Decision Tree Algorithm
* ID3: Iterative Dichotomiser 3
* C4.5: the successor of ID3
* CART: Classification and Regression Tree
* CHAID: Chi-square automatic interaction detection
* MARS: multivariate adaptive regression splines

**Splitting Points**
* Gini impurity: If a split results in one class being more predominant than another, 
e.g. 80% of class A and 20% of class B, this means that the split is 80% pure. The algorithm iteratively tries to find percentages like these of independent values, which produce homogenous classes.
* Information Gain: Information gain measures whether or not we lower the system’s entropy after splitting.

Intuition - how much information in categorical column; how much information conditioned on target

**Regressor, CART algorithm**
Uses variance reduction as a measure of best split; 
Intuition - what cut of data would lower variance within target


* [Entropy](https://machinelearningmastery.com/what-is-information-entropy/#:~:text=Entropy%20can%20be%20calculated%20for,*%20log(p(k))))

* Low Probability Event: High Information (surprising)
* High Probability Event: Low Information (unsurprising)
measure *information*
 h(x) = -log(p(x)) <--- log is base 2

The lowest entropy is calculated for a random variable that has a single event with a probability of 1.0, a certainty. The largest entropy for a random variable will be if all events are equally likely.

```from math import log2```
Information will be zero when the probability of an event is 1.0 or a certainty, e.g. there is no surprise.

For example, if we wanted to calculate the information for a random variable X with probability distribution p, this might be written as a function H(); for example:
Calculating the information for a random variable is called “information entropy,” “Shannon entropy,” or simply “entropy“. 
H(X) = -sum(each k in K p(k) * log(p(k)))  <--- I see - it's weighted average of information
The lowest entropy is calculated for a random variable that has a single event with a probability of 1.0, a certainty. The largest entropy for a random variable will be if all events are equally likely.
*In the case where one event dominates, such as a skewed probability distribution, then there is less surprise and the distribution will have a lower entropy.*
* Skewed Probability Distribution (unsurprising): Low entropy.
* Balanced Probability Distribution (surprising): High entropy.

[Gini Implementation](https://stackoverflow.com/questions/39512260/calculating-gini-coefficient-in-python-numpy)

Implementation of the Gini coefficient - It's half the relative mean absolute difference.

[Relative mean absolute difference](https://en.wikipedia.org/wiki/Mean_absolute_difference#Relative_mean_absolute_difference) - mean absolute difference in comparison to size of the mean and is dimensionless. 

(MD) Mean absolute difference is defined as the "average" of absolute differences
(AM) Arithmetic Mean

A Gini index of 0 represents perfect equality, while an index of 100 implies perfect inequality
s commonly recognized that Gini index<0.2 corresponds with perfect income equality, 0.2–0.3 corresponds with relative equality, 0.3–0.4 corresponds with a relatively reasonable income gap, 0.4–0.5 corresponds with high income disparity, above 0.5 


