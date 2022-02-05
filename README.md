# rasp4throttler
라즈베리파이의 온도를 자동으로 관리해주는 cpu 뜨로틀러입니다.</br>
cpu 온도를 측정해서 특정 온도를 초과하면 cpu 성능에 제한을 걸어서 발열을 제어해줍니다

필요한 패키지 : python3, cpufrequtils </br>
root 권한으로 실행하셔야 정상 동작합니다

설치 방법(우분투 기준)</br>
sudo apt-get update && sudo apt-get upgrade && sudo apt-get install python3 cpufrequtils && git clone https://github.com/dnjswndbf/rasp4throttler.git

실행 방법</br>
sudo python3 ther.py
