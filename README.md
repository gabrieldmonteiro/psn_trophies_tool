# PSN Trophies - Get the hours needed to platinum/100% your game list from [PSN Profiles](https://psnprofiles.com/)

* Update games.csv file adding your game list (only game name) below GAMES,HOURS row

  e.g.:
  ```csv
  GAMES, HOURS
  Remnant
  Superliminal
  Death Stranding
  ```
* Create a virtual env and activate it
  ```bash
  python -m venv venv  
  ```
  then,
  
  Windows:
    ```bash
    venv/Scripts/activate 
    ```
    
  Linux/MacOS
    ```bash
    venv/bin/activate 
    ```

* Install requirements.txt

  ```bash
  pip install -r requirements.txt
  ```  

* Then run main.py to generate GameList excel file

  ```bash
  python .\main.py
  ```

