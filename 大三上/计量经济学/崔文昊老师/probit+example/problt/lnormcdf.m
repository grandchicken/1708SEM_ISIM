function [y] = lnormcdf(x)

% The natural logarithm of the CDF of the standard normal, ln(Phi(x)), is
% numerically tricky to estimate when 'x' gets very large (something
% like x>8) or very small (something like x<-37). For these two cases,
% there exist a more accurate result than what log(normcdf(x)) will report.

y1 = -exp(-0.5*x.^2)./(x*sqrt(2*pi));
y2 = -0.5*x.^2-log(-x*sqrt(2*pi));
y3 = log(normcdf(x));

case1 = (x>8);
case2 = (x<-37);
case3 = 1-case1-case2;

y = case1.*y1 + case2.*y2 + case3.*y3;

end