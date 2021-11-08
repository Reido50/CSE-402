%% Compute Orientation
fpimg = imread('proj02_q1_fingerprint_images\user001_1.gif');
imshow(fpimg, []);
sob_output = imfilter(fpimg, sob_filter);
figure;
imshow(sob_output, [])
drawOrientation(fpimg, sob_output)