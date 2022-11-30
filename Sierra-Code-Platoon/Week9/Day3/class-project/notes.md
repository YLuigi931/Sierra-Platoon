Step 1: create the front-end:
        
        * commands
            - 'npm create vite'
                - add a name for project call it client
                - pick react and javascript
                
Step 2: create the environment
        
        * commands
            - 'python3 - m venv .venv'
            - and activate 'source .venv/bin/activate'
            - install django 'pip install django'
            - check the dependence 'pip freeze'
            - add requirements 'pip freeze > requirements.txt'

Step 3: create the project
        
        * commands
            - 'python3 -m startproject {project_Name}'

Step 4: modify the front-end's vite.config.js
    
    Markup : ```javascript
                * export default defineConfig({
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

Step 5: modify settings.py
    
    * Add this under lines 118
    
        - Markup :  ```python
                        STATICFILES_DIRS = [BASE_DIR/'static']
                    ```

Step 6: make sure to finish build on front-end
        
        - go to the directory
            * commands
                - 'npm install'

Step 7: