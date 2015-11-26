###########################################################
#   Task 1
###########################################################

genotype <- read.csv("genotype.csv", row.names = 1)
expression <- read.csv("expression.csv", row.names = 1)


###########################################################
#   Task 2
###########################################################

genes = expression[,1:5]
attach(mtcars)
par(mfrow=c(2,3))  
hist(genes[,1], xlab = "expression", main = paste("Histogram of gene", colnames(genes)[1]))
hist(genes[,2], xlab = "expression", main = paste("Histogram of gene", colnames(genes)[1]))
hist(genes[,3], xlab = "expression", main = paste("Histogram of gene", colnames(genes)[1]))
hist(genes[,4], xlab = "expression", main = paste("Histogram of gene", colnames(genes)[1]))
hist(genes[,5], xlab = "expression", main = paste("Histogram of gene", colnames(genes)[1]))

###########################################################
#   Task 3
###########################################################

yeast_ids <- genotype[3:7,]
yeast_ids <- yeast_ids[-c(1)]
yeast_ids[yeast_ids == 0] <- NA
yeast_ids = t(yeast_ids)
row.names(yeast_ids) <- NULL 
par(mfrow=c(5,1))
plot(yeast_ids[,1], type = "l", ylab = 'Yeast 1', xlab = 'SNP')
plot(yeast_ids[,2], type = "l", ylab = 'Yeast 2', xlab = 'SNP')
plot(yeast_ids[,3], type = "l", ylab = 'Yeast 3', xlab = 'SNP')
plot(yeast_ids[,4], type = "l", ylab = 'Yeast 4', xlab = 'SNP')
plot(yeast_ids[,5], type = "l", ylab = 'Yeast 5', xlab = 'SNP')
