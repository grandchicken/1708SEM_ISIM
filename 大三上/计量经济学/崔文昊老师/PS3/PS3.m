clear;
close all;
clc;

tutu = load('earn.txt');

EXP = tutu(:,1);
EXP2 = tutu(:,2);
WKS = tutu(:,3);
OCC = tutu(:,4);
IND = tutu(:,5);
SOUTH = tutu(:,6);
SMSA = tutu(:,7);
MS = tutu(:,8);
FEM = tutu(:,9);
UNION = tutu(:,10);
ED = tutu(:,11);
BLK  = tutu(:,12);
LWAGE = tutu(:,13);
M = tutu(:,14);
F_EDC= tutu(:,15);

Y = UNION;
N = length(Y);
X = [EXP, WKS, OCC, IND, SOUTH, SMSA, MS, FEM, ED, BLK, ones(N,1)];
K = size(X,2);

%用内置函数fitlm完成回归
tbl = table(EXP, WKS, OCC, IND, SOUTH, SMSA, MS, FEM, ED, BLK, UNION, 'VariableNames', ...
    {'EXP', 'WKS', 'OCC', 'IND', 'SOUTH', 'SMSA', 'MS', 'FEM', 'ED', 'BLK', 'UNION'});
mdl = fitlm(tbl, 'UNION~EXP+WKS+OCC+IND+SOUTH+SMSA+MS+FEM+ED+BLK');

%手写回归
betaHat = X'*X \ X'*Y;  %估计量
uHat = Y - X*betaHat;  %离差
sigma2Hat = sum(uHat.^2) / (N-K);  %随机误差项方差估计值
varBetaHat = sigma2Hat * inv(X'*X);  %方差-协方差矩阵
stdBetaHat = sqrt(diag(varBetaHat));  %标准误
t = (betaHat-zeros(K, 1)) ./ stdBetaHat;
pValue = 2*(1-normcdf(abs(t)));

mdl
betaHat = betaHat'
t = t'