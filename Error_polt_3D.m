close all, clear all, clc

%CONST
FILENAME_STRING = 'Errors.csv';
%

[error, variable] = read_csv(FILENAME_STRING);
plotdata_3D(error, variable);


function [error, variable] = read_csv(file_name)
    data = readtable(file_name);
    error = data(:,1);
    variable = data(:,2);
end

function [] = plotdata_3D(error, variable)
    data = [table2array(error), table2array(variable)];

    figure('Name','___ Put name');
    hist3(data,'CDataMode','auto','FaceColor','interp');

    xlabel('Error')
    ylabel('Variable')
    title('ULP?')
end