import numpy as np
import matplotlib.pyplot as plt
import csv
import itertools

'''
FIRおよびIIRデジタルフィルタの試行
- 最終更新日: 2022/01/29
- 学籍番号: 953526
- 氏名: 小西巧真
'''

# csvファイルを読み込み，float型リストへ格納
def read_fir_csv(filename: str) -> list:
    with open(filename) as f:
        reader = csv.reader(f)
        data = [float(i) for i in list(itertools.chain.from_iterable(reader))]
    return data

# csvデータセットを読み込む
fir_16 = read_fir_csv("data/fir_16.csv")
fir_32 = read_fir_csv("data/fir_32.csv")
low = read_fir_csv("data/lowpass.csv")
high = read_fir_csv("data/highpass.csv")

#３つの波の周波数
f1 = 3
f2 = 7
f3  =15

wave = [] #合成波
x = [] #横軸t

#-------------------------３つの波を合成------------------------------------------------
for i in range(101):
    t = i/100
    x.append(t)
    wave.append(np.sin(f1*2*np.pi*t) + np.sin(f2*2*np.pi*t) + np.sin(f3*2*np.pi*t))
for i in range(32):
    wave.append(0)

plt.figure()
plt.plot(x, wave[:101])
plt.savefig("img/input_signal.png")
plt.show

#-------------------------IIR-HPF結果--------------------------------------------------
iir_hpf = []
for i in range(101):
    if i == 0:
        iir_hpf.append(0)
    elif i == 1:
        iir_hpf.append(wave[i] * (high[3]/high[0]) + wave[i-1] * (high[4]/high[0]) - iir_hpf[i-1] * (high[1]/high[0]))
    else:
        iir_hpf.append(wave[i] * (high[3]/high[0]) + wave[i-1] * (high[4]/high[0]) + wave[i-2] * (high[5]/high[0])- iir_hpf[i-1] * (high[1]/high[0]) - iir_hpf[i-2] * (high[2]/high[0]))

plt.figure()
plt.plot(x, iir_hpf)
plt.ylim([-3, 3])
plt.savefig("img/iir_hpf.png")
plt.show

#-------------------------IIR-LPF結果---------------------------------------------------
iir_lpf = []
for i in range(101):
    if i == 0:
        iir_lpf.append(0)
    elif i == 1:
        iir_lpf.append(wave[i] * (low[3]/low[0]) + wave[i-1] * (low[4]/low[0]) - iir_hpf[i-1] * (low[1]/low[0]))
    else:
        iir_lpf.append(wave[i] * (low[3]/low[0]) + wave[i-1] * (low[4]/low[0]) + wave[i-2] * (low[5]/low[0])- iir_hpf[i-1] * (low[1]/low[0]) - iir_hpf[i-2] * (low[2]/low[0]))

plt.figure()
plt.plot(x, iir_lpf)
plt.ylim([-4, 4])
plt.savefig("img/iir_lpf.png")
plt.show

#-------------------------FIR-16-LPF----------------------------------------------------
fir_lpf_16 = []
for i in range(101):
    fir_lpf_16.append(
        fir_16[0]*wave[i]+fir_16[1]*wave[i-1]
        +fir_16[2]*wave[i-2]+fir_16[3]*wave[i-3]
        +fir_16[4]*wave[i-4]+fir_16[5]*wave[i-5]
        +fir_16[6]*wave[i-6]+fir_16[7]*wave[i-7]
        +fir_16[8]*wave[i-8]+fir_16[9]*wave[i-9]
        +fir_16[10]*wave[i-10]+fir_16[11]*wave[i-11]
        +fir_16[12]*wave[i-12]+fir_16[13]*wave[i-13]
        +fir_16[14]*wave[i-14]+fir_16[15]*wave[i-15]
    )

plt.figure()
plt.plot(x, fir_lpf_16)
plt.ylim([-4, 4])
plt.savefig("img/fir_lpf_16.png")
plt.show

#-------------------------FIR-32-LPF-16--------------------------------------------------
fir_lpf_32 = []
for i in range(101):
    fir_lpf_32.append(
        fir_32[0]*wave[i]+fir_32[1]*wave[i-1]
        +fir_32[2]*wave[i-2]+fir_32[3]*wave[i-3]
        +fir_32[4]*wave[i-4]+fir_32[5]*wave[i-5]
        +fir_32[6]*wave[i-6]+fir_32[7]*wave[i-7]
        +fir_32[8]*wave[i-8]+fir_32[9]*wave[i-9]
        +fir_32[10]*wave[i-10]+fir_32[11]*wave[i-11]
        +fir_32[12]*wave[i-12]+fir_32[13]*wave[i-13]
        +fir_32[14]*wave[i-14]+fir_32[15]*wave[i-15]
        +fir_32[16]*wave[i-16]+fir_32[17]*wave[i-17]
        +fir_32[18]*wave[i-18]+fir_32[19]*wave[i-19]
        +fir_32[20]*wave[i-20]+fir_32[21]*wave[i-21]
        +fir_32[22]*wave[i-22]+fir_32[23]*wave[i-23]
        +fir_32[24]*wave[i-24]+fir_32[25]*wave[i-25]
        +fir_32[26]*wave[i-26]+fir_32[27]*wave[i-27]
        +fir_32[28]*wave[i-28]+fir_32[29]*wave[i-29]
        +fir_32[30]*wave[i-30]+fir_32[31]*wave[i-31]
    )

plt.figure()
plt.plot(x, fir_lpf_32)
plt.ylim([-4, 4])
plt.savefig("img/fir_lpf_32.png")
plt.show
