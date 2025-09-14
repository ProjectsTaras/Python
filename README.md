Завантажте та встановіть Git:
Перейдіть на git-scm.com та скачайте інсталятор для Windows. Встановіть Git, під час встановлення залиште стандартні налаштування.
Перезапустіть VS Code або термінал після встановлення.
Перевірте встановлення:
Введіть у терміналі:
git -- version
Якщо бачите версію — все працює.

Введіть у терміналі ці команди (замініть на свої дані):
git config --global user.name "Ваше Ім'я"
git config --global user.email "ваш@email.com"
Наприклад:
git config --global user.name "Taras"
git config --global user.email "taras@example.com"

Щоб додати ваш проект на GitHub, виконайте ці кроки:
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

Якщо репозиторій вже існує на GitHub, просто вкажіть його адресу для вашого локального репозиторію через команду:
git remote set-url origin https://github.com/ProjectsTaras/Python.git

Ця команда оновить адресу віддаленого репозиторію origin на вашу GitHub-сторінку.
Тепер ви можете виконувати команди git push та git pull для синхронізації з GitHub
