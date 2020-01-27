@echo off
:: running the behave to execute the feature file with tagname given in behave.ini
behave -f allure_behave.formatter:AllureFormatter -o result ./features


set current_dir=%cd%

::get the latest folder name
cd /d .\output
for /f %%i in ('dir /b/od/t:c') do set LATEST_FOLDER=%%i

::Move the behave created Json to Latest timestamp output folder
cd..
cd result
move *.json %current_dir%\output\%LATEST_FOLDER%
cd..

::Generate the Allure report
cd %current_dir%\output
%current_dir%\Lib\allure-2.7.0\bin\allure serve %LATEST_FOLDER%