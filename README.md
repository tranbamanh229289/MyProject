## MyProject
1. How to export the environment:
* Activate the environment: conda activate "name env "
* Save env to file : conda export env > "name file ".yml

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
* Result :This algorithm is quite effective and easy to deploy.In essence, this model does not learn anything from data.
Thí Al can be used in 2 types of classification and regression . 

5.Al Naive Bayes :
* Data : Dataset weather has 4 features: outlook , temperature,humidity,wind  . Each feauture has attibutes as: sunny,rainy,cool,hot , strong, weak ,high...
* Preprocessing data :
* I use the Naive Bayes algorithm for classification problems, to decide whether or not to play?.
In the "Naive Bayes" algorithm, it depends a lot on the distribution P (xi | c). There are 3 models to calculate P (xi | c): Gaussian Naive Bayes, Multinomial Naive Bayes, Bernoulli Naive Bayes. My project uses the Multinomia Naive Bayes model.
* Multinomial Naive Bayes :This model is often used in text classification models.
* Gaussian Naive Bayes :Use in data model is continuous variable ,
* Bernoulli Naive Bayes: This model is applied to data types where each component is a binary value - equal to 0 or 1.
* Result:The model was not very accurate(75%). The reason is that this algorithm is heavily based on the train dataset .If there is little data, the algorithm will not be effective.This algorithm has no machine learning.

