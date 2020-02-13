## MyProject
1. How to export the environment:
* Activate the environment: conda activate "name env "
* Save env to file : conda export env -f > "name file ".yml

2.How to create environment with my file .yaml :Dowload my file .yaml Then open conda prompt command :conda env create  -f "name file ".yml

3.How to run my source code :
* Create environment with file my .yml
(Note: that you don't need to supply the name of the new environment, as the yaml file also contains the name of the environment it saved. Make sure you don't give your environment an embarassing name, as everyone who recreates from the yaml file will see the name you used!)
* Use run my code :dowload my dataset and code .Save it into a file. Copy the address of that file .Then open your anaconda prompt , create env with my file .yml .Activate this env .Finally command :
(cd "Paste the copied address " 
python "namecode.py")

4.Al KNN :
* Data : Dataset Iris Flower for 4 feautures .I use 100 data points to train .50 data points to test and evaluate.
* Preprocessing data :Missing values :Data set: full data, not missing .No need to handle missing data.  
* Problem requirements: From the dataset of iris flowers, build a model for classifying 3 types of flowers: "Setona", "Versicolor", "Virginica" using KNN.
* Evaluating algorithm results:This algorithm is quite effective and easy to deploy.In essence, this model does not learn anything from data.
* This Al can be used in 2 types of classification and regression . 

5.Al Naive Bayes :
* Data : Dataset weather has 4 features: outlook , temperature,humidity,wind  . Each feauture has attibutes as: sunny,rainy,cool,hot , strong, weak ,high...
* Preprocessing data :
* I use the Naive Bayes algorithm for classification problems, to decide whether or not to play?.
* In the "Naive Bayes" algorithm, it depends a lot on the distribution P (xi | c). There are 3 models to calculate P (xi | c): Gaussian Naive Bayes, Multinomial Naive Bayes, Bernoulli Naive Bayes. My project uses the Multinomia Naive Bayes model.
* Multinomial Naive Bayes :This model is often used in text classification models.
* Gaussian Naive Bayes :Use in data model is continuous variable ,
* Bernoulli Naive Bayes: This model is applied to data types where each component is a binary value - equal to 0 or 1.
* Evaluating algorithm results:The model was not very accurate(75%). The reason is that this algorithm is heavily based on the train dataset .If there is little data, the algorithm will not be effective.This algorithm has no machine learning.

6.AI Decision Tree :
* Data : Dataset weather has 4 features: outlook , temperature,humidity,wind  . Each feauture has attibutes as: sunny,rainy,cool,hot , strong, weak ,high...
* Preprocessing data :
* I use a decision tree model, which uses the ID3 algorithm for my problem,to decide whether or not to play?.
* In decision trees,leaf nodes will have data points of the same layer. So you must understand the terms "entropy" and "information gain" (read more) to to classify well .We need to build a decision tree so that the leaf nodes will have entropy = 0 or approximately 0 to ensure the data points in the leaf nodes are clean.So it is important to choose the order of the nodes in the decision tree. Each node is an attribute.Any node with a large information gain will be arranged in advance for rapid division, and the entropy of the nodes will decrease as quickly as possible.
* In ID3, if we continue to divide forever, then our decision tree will be very complex, many leaf nodes have only 1 or 2 data points. To overcome this, we will have the stopping conditions:
* The depth of the node must be limited.
* The division of that node does not reduce entropy too much will be stopped
* that node has fewer elements than the threshold.
* Evaluating algorithm results: The algorithm depends heavily on training data. The biggest drawback of ID3 and the decision tree is generally that if a new data point falls into the wrong branch at the first split, the end result will be different. so many, so much .

7. Ai Group SVM :
- Data :Self-created in code.I use the normal distribution and covariance matrix to create data.
- The SVM algorithm group has the following algorithms:
  - Hard Magins:  With "linear separation" data .Bringing issues about convex planning format.Then the problem is solved in 2 ways. Method 1 is calculated directly and satisfies Slayter and regular conditions as convex objective function and constraint set as convex set. Then deduce that the solution of the problem is the solution of the system "K K T".Method 2 approaches the problem by solving a simpler problem. The problem of finding the max is the solution of the other problem to find min. I use this method 2 because method 1 solves it directly, I have to solve the "KKT" system: it is very complicated and not feasible. Because the number of equations and number of cases of the "KKT" system is too big .For method 2, I use the CVXOPT library to solve the convex optimization problem.
  - Soft Magins : With data problems near "linear separation".Similar to Hard Margins. The objective function of this problem is to add the sacrifices of the noise data points.
  -
