clear; clc; close all;

%% help function to print measurement in more readable format
% if you use Octave to run this script, you should put function definition here
% if you use Matlab, put comments arond the definition of "print_measure" 
function print_measure(ind, m)
    for loop1 = 1 : length(ind)
        fprintf('%d: %.2f\n', ind(loop1), m(loop1));
    end
end


%H = sparse([3, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8, 8], ...
%           [1, 1, 7, 2, 5, 3, 4, 8, 3, 4, 5, 2, 4, 5, 6, 5, 6, 7, 1], ...
%           [-17.3611, 16.0000, -16.0000, 17.0648, -17.0648, 39.9954, -10.8696 -11.7647, -10.8696, 16.7519, ...
%           -5.8824, -17.0648, -5.8824, 32.8678, -9.9206, -9.9206, 23.8095, -13.8889, -16.0000], ...
%           9,8);

z = transpose([0.6700, 1.6300, 0.8500, 0, -0.9000, 0, -1.0000, 0, -1.2500]);


H = [0         0  -17.3611         0         0         0         0         0 ; ...
   16.0000         0         0         0         0         0  -16.0000         0 ; ...
         0   17.0648         0         0  -17.0648         0         0         0 ; ...
         0         0   39.9954  -10.8696         0         0         0  -11.7647 ; ...
         0         0  -10.8696   16.7519   -5.8824         0         0         0 ; ...
         0  -17.0648         0   -5.8824   32.8678   -9.9206         0         0 ; ...
         0         0         0         0   -9.9206   23.8095  -13.8889         0 ; ...
  -16.0000         0         0         0         0  -13.8889   36.1001   -6.2112 ; ...
         0         0  -11.7647         0         0         0   -6.2112   17.9759];

W = diag(100*ones(1,9));

gain = transpose(H) * W * H;

% indices are based on Table 1 of the instruction 
x_est_ind = [22, 32, 42, 52, 62, 72, 82, 92];
z_ind = [13, 23, 33, 43, 53, 63, 73, 83, 93];

% TODO: calculate x_est based on the formulat given in the lecture
x_est = ;

% Assume that this is the c that the FDIA tries to achieve
c =[0.02;0.01;0.00;-0.01;0.00;0.00;0.01;-0.01];
% TODO: calculate xa_est which is the compromised system states
xa_est = ;
% TODO: based on the conditiion presented in the lecture to calcualte the compromised measurements
a = ;
za = ;

fprintf('***** Estimated States before FDIA *****\n');
print_measure(x_est_ind, x_est);

fprintf('***** Measurements before FDIA *****\n');
print_measure(z_ind, z);

fprintf('***** Estimated States after FDIA *****\n');
print_measure(x_est_ind, xa_est);

fprintf('***** Measurements after FDIA *****\n');
print_measure(z_ind, za);

%% help function to print measurement in more readable format
% if you use Matlab to run this script, you should put function definition here; 
%  remove the comments symbols around the if you use Matlab, arond the definition of "print_measure" 
%{
function print_measure(ind, m)
    for loop1 = 1 : length(ind)
        fprintf('%d: %.2f\n', ind(loop1), m(loop1));
    end
end
%}
