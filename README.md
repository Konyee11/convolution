# Convolution-2021

FIR および IIR デジタルフィルタの試行

# Features

ディレクトリ構成

```bash
tree .
.
├── README.md
├── main.py
├── data
│   ├── fir_16.csv
│   ├── fir_32.csv
│   ├── highpass.csv
│   └── lowpass.csv
└── img
    ├── fir_lpf_16.png
    ├── fir_lpf_32.png
    ├── iir_hpf.png
    ├── iir_lpf.png
    └── input_signal.png
```

- input_signal.png : 入力信号
- iir_hpf.png : IIR-HighPassFilter 処理結果
- iir_lpf.png : IIR-LowPassFilter 処理結果
- fir_lpf_16.png : FIR-LowPassFilter(次数 16)の処理結果
- fir_lpf_32.png : FIR-LowPassFilter(次数 32)の処理結果

# Requirement

- python 3.9.7 64-bit
- matplotlib 3.4.3
- numpy 1.20.3

# Installation

matplotlib をインストールする

```bash
pip install matplotlib
```

numpy をインストールする

```bash
pip install numpy
```

# Usage

```bash
cd convolution
python main.py
```

# Author

- 小西巧真
- 京都産業大学 情報理工学部 3 年 玉田研究室
- g1953526
- konyee.527@gmail.com
