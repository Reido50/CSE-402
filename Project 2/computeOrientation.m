%% Compute Orientation
fpimg = imread('proj02_q1_fingerprint_images\user001_1.gif');
imshow(fpimg, []);
orientationField = readtable('orientationFielduser001_1.gif.csv');
orientationField = table2array(orientationField);
drawOrientation(fpimg, orientationField)