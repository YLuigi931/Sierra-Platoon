## Step 1: create the front-end:
        
### commands
    - 'npm create vite'
        - add a name for project call it client
        - pick react and javascript
                
## Step 2: create the environment
something here[^1].
### commands
```
python3 - m venv .venv[^1].
source .venv/bin/activate
pip install django
pip freeze
pip freeze > requirements.txt
```
[^1]: My reference.


## Step 3: create the project
        
### commands
```
python3 -m startproject {project_Name}
```
- cd to project folder
- Add static folder in the project folder

## Step 4: modify the front-end's vite.config.js
    
```javascript
    export default defineConfig({
        // vite uses this as a prefix for href and src URLs
        base: '/static/',
        build: {
            //where vite puts the bundled application
            outDir:'../server/static',
            // delete old build when creating new
            emptyOutDir: true,
            sourcemap: true,
        },
        plugins: [react()]
        })
```

## Step 5: modify settings.py
    
### Add this under lines 118
    
```python
    STATICFILES_DIRS = [BASE_DIR/'static']
```

## Step 6: make sure to finish build on front-end
        
- go to the directory
### commands
```
npm install
npm run build
```

## Step 7: Test
    
- check the static folder if its populated
- run the server
    - go to server directory and type this command
    * commands
        - 'python3 manage.py runserver'

