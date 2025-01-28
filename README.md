 Thriftopia

Thriftopia je moderní e-shop zaměřený na prodej secondhand oblečení. Projekt byl vytvořen jako závěrečný úkol kurzu programování v Pythonu a kombinuje robustní backend v Django s efektivním a uživatelsky přívětivým frontendem.


Funkcionality
- Plně funkční e-shop s možností procházení produktů.
- Správa uživatelských účtů, přihlášení a registrace.
- Administrace pro správu produktů, včetně přidávání, úprav a mazání.
- Databázová struktura implementovaná pomocí SQL.



Technologie
- Python – hlavní programovací jazyk projektu.
- Django – backendový framework zajišťující vývoj aplikace a správu databáze.
- HTML a CSS – tvorba statického uživatelského rozhraní.
- JavaScript – implementace dynamických prvků frontendu.
- SQL – databázový systém pro ukládání a správu dat.



Instalace a spuštění
1. Klonujte repozitář do svého lokálního prostředí:
 
  ```bash
   git clone <URL_TO_REPO>

   ```
2. Přesuňte se do adresáře projektu:

   ```bash
   cd thriftopia
   ```

3. Vytvořte a aktivujte virtuální prostředí:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Na Windows: .venv\Scripts\activate
   ```

4. Nainstalujte všechny závislosti uvedené v `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

5. Proveďte migrace databáze:

   ```bash
   python manage.py migrate
   ```

6. Spusťte vývojový server:

   ```bash
   python manage.py runserver
   ```

7. Aplikace bude dostupná na: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).



Autoři
Tomáš Gombár
Jiří Petr Soukup
Kateřina Weingartová
