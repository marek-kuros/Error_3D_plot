function input_file = Error_plot_3D(file_name)
    input_file = file_name;
    [error, variable] = read_csv(input_file);
    plotdata_3D(error, variable);
end

function [error, variable] = read_csv(file_name)
    data = readtable(file_name);
    error = data(:,1);
    variable = data(:,2);
end

function [] = plotdata_3D(error, variable)
    data = [table2array(error), table2array(variable)];

    figure('Name', 'Error');
    hist3(data,'CDataMode','auto','FaceColor','interp');

    xlabel('Error');
    ylabel('Variable');
    title('ULP?');
end