clear; clc; close all;

%addpath(genpath('/home/hugo/Dropbox/Experiments/matpower5.0'));
addpath(genpath('/home/hugo/source/matpower7.0'));

cur_case = loadcase(case3);

%% how to generate ybus
[Ybus, Yf, Yt] = makeYbus(cur_case);

%% how to run power flow analysis
baseresult = runpf(cur_case, mpoption('model', 'AC'));

%% how to run state estimation
% whether adding noises or not
USE_NOISE = 1;
% using matpower constant
[PQ, PV, REF, NONE, BUS_I, BUS_TYPE, PD, QD, GS, BS, BUS_AREA, VM, ...
    VA, BASE_KV, ZONE, VMAX, VMIN, LAM_P, LAM_Q, MU_VMAX, MU_VMIN] = idx_bus;
[F_BUS, T_BUS, BR_R, BR_X, BR_B, RATE_A, RATE_B, RATE_C, ...
    TAP, SHIFT, BR_STATUS, PF, QF, PT, QT, MU_SF, MU_ST, ...
    ANGMIN, ANGMAX, MU_ANGMIN, MU_ANGMAX] = idx_brch;
[GEN_BUS, PG, QG, QMAX, QMIN, VG, MBASE, GEN_STATUS, PMAX, PMIN, ...
    MU_PMAX, MU_PMIN, MU_QMAX, MU_QMIN, PC1, PC2, QC1MIN, QC1MAX, ...
    QC2MIN, QC2MAX, RAMP_AGC, RAMP_10, RAMP_30, RAMP_Q, APF] = idx_gen;

nline = length(baseresult.branch(:,1));
nbus = length(baseresult.bus(:, 1));

idx.idx_zPF = transpose(1:nline);
idx.idx_zPT = [];
idx.idx_zPG = [];
idx.idx_zVa = [];
idx.idx_zQF = transpose(1:nline);
idx.idx_zQT = [];
idx.idx_zQG = [];
idx.idx_zVm = transpose(1:nbus);

% specify measurement variances
sigma.sigma_PF = 0.02;
sigma.sigma_PT = [];
sigma.sigma_PG = [];
sigma.sigma_Va = [];
sigma.sigma_QF = 0.02;
sigma.sigma_QT = [];
sigma.sigma_QG = [];
sigma.sigma_Vm = 0.1;

% specify measurements
measure.PF = baseresult.branch(:, PF) / baseresult.baseMVA + USE_NOISE * normrnd(0, sigma.sigma_PF, [nline, 1]);
measure.PT = [];
measure.PG = [];
measure.Va = [];
measure.QF = baseresult.branch(:, QF) / baseresult.baseMVA + USE_NOISE * normrnd(0, sigma.sigma_QF, [nline, 1]);
measure.QT = [];
measure.QG = [];
measure.Vm = baseresult.bus(:, VM) + USE_NOISE * normrnd(0, sigma.sigma_Vm, [nbus, 1]);


% check input data integrity
[success, measure, idx, sigma] = checkDataIntegrity(measure, idx, sigma, nbus);
if ~success
    error('State Estimation input data are not complete or sufficient!');
end

% run state estimation
%casename = 'case14.m';
type_initialguess = 2; % flat start
%[baseMVA, bus, gen, branch, success, et, z, z_est, error_sqrsum] = run_se(casename, measure, idx, sigma, 1e-3, 100, type_initialguess);
[baseMVA, bus, gen, branch, success, et, z, z_est, error_sqrsum] = run_se(cur_case, measure, idx, sigma, type_initialguess);

freedom = length(z) - 2*(nbus-1);
baddata_t = chi2inv((1-0.9), freedom);
