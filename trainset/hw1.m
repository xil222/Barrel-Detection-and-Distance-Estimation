clear all
P1 = imread('5.6.png');
figure
imagesc(P1)
BW = roipoly
[xR,yR] = find(BW == 1)
figure
imagesc(P1)
BW = roipoly
[xnR,ynR] = find(BW == 1)
figure
imagesc(P1)
BW = roipoly
[xY,yY] = find(BW == 1)
figure
imagesc(P1)
BW = roipoly
[xBr,yBr] = find(BW == 1)

save label5.6mat xR yR xnR ynR xY yY xBr yBr




