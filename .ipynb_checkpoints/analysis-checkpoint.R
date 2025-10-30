install.packages("ggplot2")
library(ggplot2)
library(corrplot)

# Plotting the graph of time(seconds) vs. distance(meters)
# Since the data set is for very small distances 
# x : distance 0 < x < 1.5
# We use regression to predict for a larger data set but before that
# we shall use curve fitting to find the best curve for the given data set


data_Set <- read.csv("C:/Users/adith/OneDrive/Desktop/sos/datasets/data_copy.csv")

# We extract the first two columns i.e. Time and distance
df <- data_Set[, 1:2]

# We summarize the data set
print("Summary Of the Dataset-1")
summary(data_Set)

#Primary Plot of the data set-1 both linear plot and correlation plot
# --------------------------------------

plot(df$Distance.m., df$Time.s., main = "Graph of Time taken vs. Distance", xlab = "Distance the wave travelled", ylab = "Time taken for wave to bounce back")
# Correlation plot
corr_mat <- cor(df)
print("Checking whether data sets are correlated?")
corr_mat
corrplot(corr_mat)

# Applying regression to extrapolate data
#---------------------------------------
model <- lm(df$Distance.m. ~ df$Time.s.)
summary(model)
summary(model)$coefficients
# using this model to check for larger values, for that we create a sample data vector
x_new <- data.frame(Time.s. = seq(0.1, 0.49, by = 0.01))
y_pred <- predict(model, newdata = x_new)
# plotting the the predicted value
plot( x_new$Time.s.,y_pred, xlab="Time", ylab="Distance", type="l")
slope <- summary(model)$coefficients["df$Time.s.", "Estimate"]
print(slope)

