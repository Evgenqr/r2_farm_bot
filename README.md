


<br>
<h1 align="center"> r2_farm_bot </h1>
<p align="center"> Бот-фармер для игры R2 Online</p>

***В проекте используются следующие технологии:***

    - Python
    - Tesseract Ocr
    - Для работы pytesseract необходимо предварительно скачать дистрибутив Tesseract-OCR c официального сайта и установить его.

***О проекте***

    Данная программа представляет собой бота, фармящего самостоятельно определенных монстров в игре R2 Online.
    В проекте используется  PyTesseract - мощный инструмент компьютерного зрения, который может распознавать текст с изображений многих форматов. 
    Так же используется библиотека компьютерного зрения OpenCV, которая предназначена для анализа, классификации и обработки изображений. 
    Для поиска мобов (монстров) в режиме реального времени использолся каскад Хаара, заранее натренированный на их поиск, и библиотека OpenCV.
    В проекте используется многопоточность с помощью модуля threading.
   
***Принцип работы бота следующий:***

    - Со стартом бота запускается 4 потока:
         1. первый контролирует уровень здоровья персонажа и при снижении до определенного уровня перемещается в безопасный город для восстановления. 
         После чего продлжает фармить.;
         2. второй отвечает за перемещение персонажа по карте (телепортация);
         3. третий отвечает за периодической использование зелий и скиллов (умений);
         4. четвертый отвечает непосредственно за поиск монстров и фарм.
  
***Примечание***
    *В настоящий моментданная программа-бот потеряла актуальность, так как игра официально закрылась в России.
    Исключением является адаптация программы для пиратских серверов проекта.*

***Запуск проекта:***

    git clone https://github.com/Evgenqr/r2_farm_bot
    cd r2_farm_bot
    python -m venv venv
    venv\scripts\activate
    pip install -r req.txt
    python startbot.py
