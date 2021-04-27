# RDP Cache

Есть два типа файла кеша:
- *.bmc
- Cachennnn.bin (где nnnn - это 4-значное число)

```cmd
  c:\Users\{user}\AppData\Local\Microsoft\Terminal Server Client\Cache\
```

Кэш-файлы хранят сырые растровые изображения в виде плиток. Размер каждой плитки может варьироваться, но общий размер составляет 64 x 64 пикселя. Глубина цвета фрагментов в файле *.bmc обычно составляет 16 или 32 бит на пиксель (bpp). Плитки в файле Cachennnn.bin имеют глубину цвета 32 бит. Несмотря на то, что кешированные фрагменты довольно малы, узнаваемый контент обычно будет отображаться, включая изображения, имена файлов и папок, значки и обои для рабочего стола.

Инструменты

[BMC-Tools](https://github.com/ANSSI-FR/bmc-tools)
[Remote-Desktop-Caching-](https://github.com/Viralmaniar/Remote-Desktop-Caching-?fbclid=IwAR3Zl8NH2FWieiGmCcmn4frajE3l03_3QknTjL5EHB4kUbZ7vaE8JjIrYkw) Может работать с битыми png изображениями
