clear all;clc;
X = imread('img/lenna.png');
k = [0.2989 0.5870 0.1140];
XG = X(:,:,1)*k(1) + X(:,:,2)*k(2) + X(:,:,3)*k(3);
imshow(XG)
% imshow(uint8(XG));
% imshow(XG);
% imwrite(XG,'lenna_gris.png');