# Iriscot Frontpage

A personal frontpage showcasing my projects.
See iriscot.org


## Build & running

1. Clone the repo

2. Run the automated install script
```
./update.sh
```

3. Reverse proxy from port 4888

4. ????

5. PROFIT!!!11


## Updating

To update simply execute installation script
```
./update.sh
```


## Localization

1. **Extract Translatable Strings:**
   ```bash
   pybabel extract -F babel.cfg -o messages.pot .
   ```
   This command extracts translatable strings and generates a template file (`messages.pot`) containing these strings.

2. **Update Translations:**
   ```bash
   pybabel update -i messages.pot -d translations
   ```
   After extracting translatable strings, you can update existing translation files or create new ones using this command. It takes the template file (`messages.pot`) and updates the translation files in the `translations` directory accordingly.

3. **Compile Translations:**
   ```bash
   pybabel compile -d translations
   ```
   Once you've updated or created translation files, use this command to compile them into binary `.mo` files. The compiled files will be stored in the `translations` directory.