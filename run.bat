behave -f allure_behave.formatter:AllureFormatter -o result ./features

set current_dir=%cd%
cd /d .\output
for /f %%i in ('dir /b/od/t:c') do set LATEST_FOLDER=%%i
echo The most recently created file is %LATEST_FOLDER%
cd..
cd result
move *.json %current_dir%\output\%LATEST_FOLDER%
cd..

cd %current_dir%\output

%current_dir%\Lib\allure-2.7.0\bin\allure serve %LATEST_FOLDER%