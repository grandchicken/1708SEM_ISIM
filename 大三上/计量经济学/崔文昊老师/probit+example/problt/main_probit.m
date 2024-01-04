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
LWAGE   = tutu(:,13);
M = tutu(:,14);
F_EDC= tutu(:,15);

Y = UNION;
N = length(Y);

X = [EXP, WKS, OCC, IND, SOUTH, SMSA, MS, FEM, ED, BLK, ones(N,1)];
K = size(X,2);

% Linear probability model
betaHat = inv(X'*X)*X'*Y;
uHat = Y-X*betaHat;
sigma2Hat = sum( uHat.^2 )/(N-size(X,2));
varBetaHat = sigma2Hat*inv(X'*X);
stdError = sqrt(diag(varBetaHat));

betaHat2 = betaHat*2.5;
betaHat2(end) = betaHat2(end)-1.25;

% probit
betaInit = betaHat2;

OPTIONS = optimset('MaxIter', 1000,'MaxFunEvals', 1e5, 'Display', 'off');
[betaMLE, logL] = fminunc(@(beta)logl_probit(beta, Y, X), betaInit, OPTIONS);

% Compute the scores for each observation
s = zeros(N,K);
beta_increment = 1e-8;
for i=1:K
  betaPlus = betaMLE;
  betaPlus(i) = betaPlus(i)+beta_increment;
  
  betaMinus = betaMLE;
  betaMinus(i) = betaMinus(i)-beta_increment;
  
  [tutu, logL_plus]  = logl_probit(betaPlus, Y, X);
  [tutu, logL_minus] = logl_probit(betaMinus, Y, X);
  
  s(:,i) = (logL_plus-logL_minus)/(2*beta_increment);
end
J = (s'*s)/N;

H = hessian(@(beta)logl_probit(beta, Y, X), betaMLE);
I = inv(H);

varMLE1 = I/N;
stdMLE1 = sqrt(diag(varMLE1));

varMLE2 = inv(J)/N;
stdMLE2 = sqrt(diag(varMLE2));

varQMLE = (I*J*I)/N;
stdQMLE = sqrt(diag(varQMLE));

'probit Model'
'Estimates  |   SE MLE(1)  |   SE MLE(2)   | SE  QMLE'
[betaMLE, stdMLE1, stdMLE2, stdQMLE]


'probit Model'
'Estimates  |   t-stat MLE(1)  |   t-stat MLE(2)   | t-stat QMLE'
[betaMLE, betaMLE./stdMLE1, betaMLE./stdMLE2, betaMLE./stdQMLE]

'Log-likelihood'
-N*logL

