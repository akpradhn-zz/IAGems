# Refrence
############################
# 1. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5009026/

# Library Neural Net
install.packages("neuralnet")

require(neuralnet)

# Data : infert

dim(infert)

# Activation Function : linear.output = TRUE

iris$Setosa<-as.numeric(iris$Species=='setosa')
iris$versicolor<-as.numeric(iris$Species=='versicolor')
iris$virginica<-as.numeric(iris$Species=='virginica')




nn  = neuralnet(Setosa+versicolor+virginica ~  Sepal.Length+Sepal.Width+Petal.Length+Petal.Width,
                data = iris,
                hidden = 2,
                err.fct = "ce",
               # algorithm = "backprop",
                #learningrate = 0.01,
                linear.output = FALSE)

lm = lm(Species_new ~  Sepal.Length+Sepal.Width+Petal.Length+Petal.Width,
        data = iris)

plot(nn)
# Target Variable
nn$response
# Input Variables
nn$covariate

# names of Input are Ourput Varible
nn$model.list

# Error Function
# The argument “err.fct” defines the error function,
# which can be either “sum of squared error (sse)” or “cross entropy (ce)
nn$err.fct

# Activation Function
nn$act.fct

# Linear Output :logical
# If act.fct should not be applied to the output neurons set linear output to TRUE,
# otherwise to FALSE.
nn$linear.output

# Complete Data Set
nn$data


nn$net.result

# View the weights
nn$weights

# Start Weights
nn$startweights

nn$generalized.weights

# Result Matrix
nn$result.matrix


###########################
####### Predicting ########
###########################

# Create an Input Vector
new.mother <- matrix(c( 5.1, 3.5,1.4,0.2,6,3.4,4.5,1.6,7.6,3,6.6,2.1),byrow=4,ncol=4)

pred<-compute(nn,new.mother)

round(pred$net.result)

pred$neurons
