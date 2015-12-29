#!/bin/bash

R '--vanilla' << R

sheet <- read.table(file="~/Documents/Survey\ Astronomy/Refine_Catalogue/Pristine_2arc_Corrected.csv", header=TRUE, sep=",")

summary(sheet)
names(sheet)
attach(sheet)
fit1 <- lm(U0 ~ NU0 + I(G0 - R0) + I(I0 - Z0))
fit2 <- lm(U0 ~ NU0 + I(NU0 - FU0) + I(G0 - R0) + I(I0 - Z0))
fit3 <- lm(U0 ~ NU0 + FU0)
fit4 <- lm(U0 ~ I(FU0 - NU0) + I(G0-R0))
fit5 <- lm(U0 ~ NU0 + FU0 + G0 + R0)
fit6 <- lm(U0 ~ NU0 + FU0 + G0 + R0 + I0 + Z0)
fit7 <- lm(U0 ~ NU0 + FU0 + I(G0 - R0))
fit8 <- lm(U0 ~ NU0 + FU0 + I(G0-R0) + I((G0-R0)^2))


fit9 <- lm(U0 ~ NU0 + G0 + R0 + I0 + Z0)
fit10 <- lm(U0 ~ NU0 + I(G0 - R0) + I((I0 - Z0)^2))
fit11 <- lm(U0 ~ NU0 + I((G0 - R0)^2) + I(I0 - Z0))

fit12 <- lm(U0 ~ NU0 + I((G0 - R0)^2))

fitfirst <- lm(U0 ~ NU0 + G0 + R0 + I0+ Z0)
fitsecond <- lm(U0 ~ NU0 + I(G0-R0))
fitthird <- lm(U0 ~ NU0 + I(G0-R0) + I(I0-Z0))


summary(fit2)
summary(fit3)
summary(fit4)
summary(fit5)

summary(fit6)
summary(fit7)
summary(fit8)

summary(fit9)
summary(fit10)
summary(fit11)
summary(fit12)

summary(fitfirst)
summary(fitsecond)
summary(fitthird)
q("no")

