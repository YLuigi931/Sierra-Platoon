# Make Full Stack

### Setup frontend
#### Name it client if you want
```
npm create vite
    - react
    - javascript
```
### Make the environment
```
python3 -m venv .venv
```

### Then activate the env
```
python3 .venv/bin/activate
```

### Add a .gitignore file
- include .venv

### Install django
```
pip install django
```

### Make the projects file (name it server if possible)
```
python3 -m django startproject server
```

### cd to the project folder and make the app
```
python3 -m django startapp server_app
```

### Run a test if both sides can run individually
```
npm run dev
python3 manage.py runserver
```

### Install the requirements for the back-end
```
pip install psycopg2
pip install djangorestframework
```

### Modify settings.py
- add the rest framework in the apps ass well as the app
    - 'rest_framework',
    - 'server_app',
- add this lines under 120
    - STATICFILES_DIRS = [BASE_DIR/'static']

- make the data base too 
    - go to terminal
        - creatdb {database name}

- Include the our created database to settings.py
    - add this
```python
        DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'assessment_4',
    }
    }
```

### Modify vite.config.js
- replace defineConfig with this
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
### Modify package.json

- add this line of code underline 8

```
"build:watch": "vite build --watch",
```

### run the rebuild for the frontend

```
npm run build:watch
```
