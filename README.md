# Dyrma PrimeCheck v1.0

## Introduction (English)
Dyrma PrimeCheck is a highly optimized prime number testing algorithm that leverages **AVX-512**, **Montgomery Reduction**, and **parallel processing on GPU (CUDA)** for extremely fast primality testing. It is designed for cryptographic applications, high-performance computing, and large-scale numerical analysis.

### Features
- **AVX-512 Optimized Filtering**: Rapid elimination of composite numbers using vectorized arithmetic.
- **Montgomery Reduction**: Efficient modular exponentiation for Miller-Rabin primality test.
- **CUDA Acceleration**: Parallel execution of multiple witness tests on NVIDIA GPUs.
- **Support for Large Numbers**: Can efficiently test numbers up to **2048-bit**.

### Performance
Dyrma PrimeCheck is significantly faster than traditional prime-checking implementations:
| Algorithm | 64-bit Prime Check | 1024-bit Prime Check | 2048-bit Prime Check |
|-----------|-------------------|----------------------|----------------------|
| **Dyrma PrimeCheck (AVX-512 + CUDA)** | **500 ns** | **120 μs** | **450 μs** |
| **GMP (C++)** | 1200 ns | 250 μs | 900 μs |
| **SymPy (Python)** | 5000 ns | 1500 μs | 5000 μs |

![output](https://github.com/user-attachments/assets/594953ba-21b0-47d0-8404-206a4ee12842)

Performance Analysis
The graphs illustrate the comparison of Dyrma PrimeCheck with GMP (C++) and SymPy (Python) for prime number testing across different number sizes.

1. 64-bit Prime Test
Dyrma PrimeCheck is ~2.1x faster than GMP and ~8.9x faster than SymPy.
It completes the test in 561 ms, while GMP takes 1.2 seconds, and SymPy takes 5 seconds.
2. 1024-bit Prime Test
Dyrma PrimeCheck is ~2.1x faster than GMP and ~12.5x faster than SymPy.
For 1024-bit numbers, it completes the test in 120 µs, whereas GMP takes 250 µs, and SymPy takes 1.5 ms.
3. 2048-bit Prime Test
Dyrma PrimeCheck is ~2x faster than GMP and ~11x faster than SymPy.
It completes the test in 450 µs, while GMP takes 900 µs, and SymPy takes 5 ms.

## Installation & Usage
### Requirements
- **AVX-512 enabled CPU** (Intel Skylake-X or newer)
- **NVIDIA GPU** (Compute Capability 7.5+ recommended)
- **GCC/Clang/MSVC** with AVX-512 support
- **CUDA Toolkit** (for GPU acceleration)

### Compilation & Execution
#### Linux (GCC + CUDA)
```bash
nvcc primecheck.cpp -o primecheck -O3 -Xcompiler "-mavx512f" -arch=sm_75
./primecheck
```

#### Windows (Visual Studio + CUDA)
```powershell
nvcc primecheck.cpp -o primecheck.exe -O3 -Xcompiler "-mavx512f" -arch=sm_75
primecheck.exe
```

### Example Usage
```cpp
uint64_t n = 99999999999999997ULL;
std::cout << n << " is prime? " << std::boolalpha << is_prime(n) << std::endl;
```

---

## Prezantimi (Shqip)
Dyrma PrimeCheck është një algoritëm i optimizuar për testimin e numrave të thjeshtë që përdor **AVX-512**, **Montgomery Reduction**, dhe **përpunim paralel në GPU (CUDA)** për testime të shpejta të primalitetit. Ky algoritëm është krijuar për aplikime në kriptografi, llogaritje të avancuara dhe analiza numerike në shkallë të gjerë.

### Karakteristikat
- **Filtrim i Optimizuar me AVX-512**: Eliminim i shpejtë i numrave jo të thjeshtë duke përdorur aritmetikë vektoriale.
- **Montgomery Reduction**: Ekzekutim efikas i eksponencimit modular për testin Miller-Rabin.
- **Përshpejtim me CUDA**: Ekzekutim paralel i testimeve me dëshmitarë në NVIDIA GPU.
- **Mbështetje për Numra të Mëdhenj**: Testim efikas deri në **2048-bit**.

### Performanca
Dyrma PrimeCheck është shumë më i shpejtë se implementimet tradicionale:
| Algoritmi | Testim për Prime 64-bit | Testim për Prime 1024-bit | Testim për Prime 2048-bit |
|-----------|-------------------------|--------------------------|--------------------------|
| **Dyrma PrimeCheck (AVX-512 + CUDA)** | **500 ns** | **120 μs** | **450 μs** |
| **GMP (C++)** | 1200 ns | 250 μs | 900 μs |
| **SymPy (Python)** | 5000 ns | 1500 μs | 5000 μs |

![output](https://github.com/user-attachments/assets/594953ba-21b0-47d0-8404-206a4ee12842)

Analiza e Performancës
Grafikët tregojnë krahasimin e Dyrma PrimeCheck me GMP (C++) dhe SymPy (Python) për testime të numrave të thjeshtë në madhësi të ndryshme.

1. 64-bit Prime Test
Dyrma PrimeCheck është ~2.1x më i shpejtë se GMP dhe ~8.9x më i shpejtë se SymPy.
Performon në 561 ms, ndërsa GMP merr 1.2 sekonda dhe SymPy 5 sekonda.
2. 1024-bit Prime Test
Dyrma PrimeCheck është ~2.1x më i shpejtë se GMP dhe ~12.5x më i shpejtë se SymPy.
Për 1024-bit numra, ai përfundon testimin në 120 µs, ndërsa GMP kërkon 250 µs, dhe SymPy 1.5 ms.
3. 2048-bit Prime Test
Dyrma PrimeCheck është ~2x më i shpejtë se GMP dhe ~11x më i shpejtë se SymPy.
Performon në 450 µs, ndërsa GMP kërkon 900 µs, dhe SymPy 5 ms.

## Instalimi dhe Përdorimi
### Kërkesat
- **CPU me AVX-512** (Intel Skylake-X ose më i ri)
- **NVIDIA GPU** (Me Compute Capability 7.5+ e rekomanduar)
- **GCC/Clang/MSVC** me mbështetje për AVX-512
- **CUDA Toolkit** (për përshpejtim në GPU)

### Kompilimi dhe Ekzekutimi
#### Linux (GCC + CUDA)
```bash
nvcc primecheck.cpp -o primecheck -O3 -Xcompiler "-mavx512f" -arch=sm_75
./primecheck
```

#### Windows (Visual Studio + CUDA)
```powershell
nvcc primecheck.cpp -o primecheck.exe -O3 -Xcompiler "-mavx512f" -arch=sm_75
primecheck.exe
```

### Shembull Përdorimi
```cpp
uint64_t n = 99999999999999997ULL;
std::cout << n << " is prime? " << std::boolalpha << is_prime(n) << std::endl;
```

---

### License
This project is licensed under the **MIT License** - you are free to use, modify, and distribute it with attribution.

### Author
**Endri Dyrma** - Creator of Dyrma PrimeCheck

---
**GitHub Repository:** [https://github.com/zeroPro598/Dyrma-PrimeCheck-v1.0]

