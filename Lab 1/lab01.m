%% Arrays and Matrices
A = [1 2 3 4 6 4 3 4 5];
B = A + 3

plot(A, 'r*-')
plot(B, 'ko-')

plot(A, B, 'r*-')
xlabel('A')
ylabel('B')

A = [1 2 0 7; 2 5 -1 6; 4 10 -1 8]

B = A'

C = [3 1; 5 2; 6 8; 1 7]

D = A*C

E = A.*B'

F = A.^2

%% Image Processing
fpimg = imread('IMAGES_Biometrics/Fingerprint/fingerprint1.tif');
size(fpimg)
imshow(fpimg, []);

log_filter = fspecial('log')
log_output = imfilter(fpimg, log_filter);
imshow(log_output, [])

fpimg_prewitt = edge(fpimg, 'prewitt');
fpimg_prewitt_horz = edge(fpimg, 'prewitt', 'horizontal');
fpimg_prewitt_vert = edge(fpimg, 'prewitt', 'vertical');

figure;
imshowpair(fpimg, fpimg_prewitt_horz, 'montage'); title('Horizontal Edge Image');
figure;
imshowpair(fpimg, fpimg_prewitt_vert, 'montage'); title('Vertical Edge Image');

fused_edges = imfuse(fpimg_prewitt_horz, fpimg_prewitt_vert);
figure;
imshowpair(fpimg, fused_edges, 'montage'); title('Fused Edge Image')

%% Lab 01 II
figure;
imshow(fpimg, [])

avg_filter = fspecial('average')
avg_output = imfilter(fpimg, avg_filter);
figure;
imshow(avg_output, [])

lap_filter = fspecial('laplacian')
lap_output = imfilter(fpimg, lap_filter);
figure;
imshow(lap_output, [])

mot_filter = fspecial('motion')
mot_output = imfilter(fpimg, mot_filter);
figure;
imshow(mot_output, [])

pre_filter = fspecial('prewitt')
pre_output = imfilter(fpimg, pre_filter);
figure;
imshow(pre_output, [])

sob_filter = fspecial('sobel')
sob_output = imfilter(fpimg, sob_filter);
figure;
imshow(sob_output, [])

uns_filter = fspecial('unsharp')
uns_output = imfilter(fpimg, uns_filter);
figure;
imshow(uns_output, [])

gau_filter = fspecial('gaussian')
gau_output = imfilter(fpimg, gau_filter);
figure;
imshow(gau_output, [])