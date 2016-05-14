clear all;clc;
X = imread('Lenna.png');
XG = rgb2gray(X);
XB = edge(XG,'sobel');
% [dx,dy] = gradient(double(XG));
% M = uint8(sqrt(dx.^2+dy.^2));
imshow(XB);
imwrite(XB,'img/lena_sobel.png');