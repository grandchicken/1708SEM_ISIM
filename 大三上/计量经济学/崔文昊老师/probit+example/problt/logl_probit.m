function [logL, m] = logl_probit(beta, y, X)

n = length(y);

% l_ind: individual log-likelihood
m = y.*lnormcdf(X*beta) + (1-y).*lnormcdf(-X*beta);

logL = -sum(m)/n;