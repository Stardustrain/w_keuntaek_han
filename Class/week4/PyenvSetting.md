### 1. Pyenv Install
>- dependency Library install
>> `$ sudo apt-get install make build-essential libssl-dev zlib1g-dev libbz2-dev
>> libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils`
>
>- [pyenv installer](https://github.com/yyuu/pyenv-installer) for Pyenv install
>> `$ curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash`
>
>- insert export path to ~/.bashrc or ~/.zshrc
>> `export PYENV_ROOT="$HOME/.pyenv"`<br>
>> `export PATH="$PYENV_ROOT/bin:$PATH"`<br>
>> `eval "$(pyenv init - zsh)"`<br>
>> `eval "$(pyenv virtualenv-init - zsh)"`
>
>- restart shell or input this command : `source ~/.zshrc(~/.bashrc)`

### 2. install specific version of python and create virtual enviroment
>- install python 3.4.3

>> ```shell
>> $ pyenv install 3.4.3
>> ```
>
> create virtualenv
>> ```shell
>> $ pyenv virtualenv 3.4.3 django
>>```
>
>- init virtual enviroment "django" and install django package

>> ```shell
>> $ pyenv activate django
>> $ pip install django
>> ```
>

### 3. make directory for django project
>- make project directory and move into that.
>>```shell
>> $ mkdir django_project
>> $ cd django_project
>>```
>
>- settings turn on virtualenv 'django' when into this directory
>>```shell
>> $ pyenv local django
>>```
>

### 4. django project
>- auto build django project
>>```shell
>> (django)$ django-admin startproject test_app
>>```
>>- options : We possible to changes project directory names. But we *don't changing name of project directory* that **'manage.py' with same path**.
>
>>```shell
>>(django)$ mv test_app django
>>```
>
>- make django application
>
>>```shell
>> (django)$ cd django
>> (django)$ python manage.py startapp my_app
>>```
>

### 5. IDE settings
>- running IntelliJ of Pycharm
>- (if use IntellJ)
>- open django Project directory
>
>>- File - Open - Choose Django project directory
>
>- open [Project Structure] menu
>
>>- Ctrl + Alt + Shift + s, or
>>- File - Project Structure
>
>- SDK configure
>
>>- Project SDK -> New -> pythonSDK -> choose 'python' that pyenv.<br> 
>> (e.g. : [pyenv path]/versions/django/bin/python) 
>
> **PROFIT!!**

