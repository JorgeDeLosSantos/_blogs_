clear;clc;
import javax.swing.*

fig = figure('Name','Ejemplo MATLAB-Java',...
    'NumberTitle','off',...
    'MenuBar','none',...
    'Position',[0,0,200,100]);
centerfig(fig);

% str = ['<html><ul>'...
%       '<li>Pizza</li>'...
%       '<li>Material</li>'...
%       '<li>Material2</li>'...
%       '</ul><html>'];
lab = JLabel('JLabel Java');
[hJLab,hMLab] = javacomponent(lab, 'East', fig);
% hJLab.setOpaque(true);
% hJLab.setForeground(java.awt.Color.RED);
% hJLab.setBackground(java.awt.Color.YELLOW)
% hJLab.setHorizontalAlignment(JLabel.CENTER);
%  
% hJLab.setBackground(Color.BLUE);
% hJLab.setHorizontalAlignment(JLabel.CENTER);
% hJLab.setVerticalAlignment(JLabel.TOP);

% mlab = uicontrol(fig,'Style','text',...
%                  'String','Label MATLAB',...
%                  'Position',[10,50,120,25]);