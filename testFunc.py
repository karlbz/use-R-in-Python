import rpy2.robjects as robjects ## import rpy2
from rpy2.robjects.packages import importr ## module to import installed R libraries

r = robjects.r
r.source("testFunc.R") ## source is used to import external lib from directory

r.testFunction() ## if valid, will print value from function
x = r.testFunction() ## store sting contents in the x variable
