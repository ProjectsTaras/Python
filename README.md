1. Завантажте та встановіть Git:
Перейдіть на git-scm.com та скачайте інсталятор для Windows. Встановіть Git, під час встановлення залиште стандартні налаштування.
Перезапустіть VS Code або термінал після встановлення.
Перевірте встановлення:
Введіть у терміналі:
git -- version
Якщо бачите версію — все працює.

2. Введіть у терміналі ці команди (замініть на свої дані):
git config --global user.name "Ваше Ім'я"
git config --global user.email "ваш@email.com"
Наприклад:
git config --global user.name "Taras"
git config --global user.email "taras@example.com"

3. Щоб додати ваш проект на GitHub, виконайте ці кроки:
Створіть новий репозиторій на GitHub.
Ініціалізуйте git у вашій папці проекту (якщо ще не зроблено):

git init
Додайте всі файли до git:

git add .

Зробіть перший коміт:

git commit -m "first commit"

git branch -M main

Підключіть ваш репозиторій на GitHub як remote:

git remote add origin https://github.com/ProjectsTaras/www.git

Відправте файли на GitHub:

push -u origin main
Після цього ваш проект буде на GitHub.

git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ProjectsTaras/name.git
push -u origin main

4. Якщо репозиторій вже існує на GitHub, просто вкажіть його адресу для вашого локального репозиторію через команду:
git remote set-url origin https://github.com/ProjectsTaras/Python.git

Ця команда оновить адресу віддаленого репозиторію origin на вашу GitHub-сторінку.
Тепер ви можете виконувати команди git push та git pull для синхронізації з GitHub

5. Після цього всі подальші пуші можна робити звичайним способом:
git add .
git commit -m "опис змін"
git push

Коли ви вдруге виконали

git branch -M main

ви перейменували гілку, і git тепер плутається, бо локальна і віддалена гілки можуть мати різні назви або історію. Тому при пуші з’являється помилка.
Щоб виправити:
Подивіться, на якій гілці ви зараз:
git branch

Вона повинна показати * main.
Якщо ваша локальна гілка main, просто зробіть force push, щоб синхронізувати з GitHub:

git push -u origin main --force

⚠️ Це перезапише віддалену гілку main вашими локальними змінами. Якщо на GitHub є важливі коміти, їх буде втрачено.

pip install matplotlib