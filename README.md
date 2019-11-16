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

3.Data : Dataset Iris Flower for 4 feautures .I do not use the "Pearson" correlation coefficient because the data has been cleaned. I will get all 4 features .I use 100 data points to train .50 data points to test and evaluate.

4.Problem requirements: From the dataset of iris flowers, build a model for classifying 3 types of flowers: "Setona", "Versicolor", "Virginica" using 4 algorithms: KNN, Decision Tree, Navei Bayes, SVM.
