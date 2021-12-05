info = audioinfo('audio.wav')
[s, fs] = audioread('audio.wav');
[nSamples, nChannels] = size(s);

%sound(s,fs);
%sound(s(:,1),fs);
%sound(s(:,2),fs);

fs_low = fs/2;
s = resample(s, fs_low, fs);
audiowrite('audio_low.wav', s, fs_low)

fs_high = fs*2;
s = resample(s, fs_high, fs);
audiowrite('audio_high.wav', s, fs_high)

%sound(s*100, fs)

%s_low = s/10;
%sound(s_low, fs);
%audiowrite('audio_new.wav', s_low, fs)

%sound(s(1:fs*2,:),fs)

%[audio, fs_1] = audioread('audio.wav');
%[noise, fs_2] = audioread('Babble.mp3');
%audio = audio(1:fs_1*5,:)
%noise = noise(1:fs_2*5,:)
%noisyAudio = audio + noise;
%audiowrite('noisyAudio', noisyAudio, fs_1);

spectrogram(s(:,1), 'yaxis');
