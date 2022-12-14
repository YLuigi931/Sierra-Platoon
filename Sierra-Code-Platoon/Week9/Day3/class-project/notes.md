# Connecting Django and React :coffee:

## Content
---
##### [Step 1](https://github.com/YLuigi931/Sierra-Platoon/edit/main/Sierra-Code-Platoon/Week9/Day3/class-project/notes.md#step-1-create-the-front-end-dumpling)
##### [Step 2](https://github.com/YLuigi931/Sierra-Platoon/edit/main/Sierra-Code-Platoon/Week9/Day3/class-project/notes.md#step-2-create-the-environment-spaghetti)
##### [Step 3](https://github.com/YLuigi931/Sierra-Platoon/edit/main/Sierra-Code-Platoon/Week9/Day3/class-project/notes.md#step-3-create-the-project-rice_ball)
##### [Step 4](https://github.com/YLuigi931/Sierra-Platoon/edit/main/Sierra-Code-Platoon/Week9/Day3/class-project/notes.md#step-4-modify-the-front-ends-viteconfigjs-house)
##### [Step 5](https://github.com/YLuigi931/Sierra-Platoon/edit/main/Sierra-Code-Platoon/Week9/Day3/class-project/notes.md#step-5-modify-settingspy-sunrise_over_mountains)
##### [Step 6](https://github.com/YLuigi931/Sierra-Platoon/edit/main/Sierra-Code-Platoon/Week9/Day3/class-project/notes.md#step-6-make-sure-to-finish-build-on-front-end-roller_coaster)
##### [Step 7](https://github.com/YLuigi931/Sierra-Platoon/edit/main/Sierra-Code-Platoon/Week9/Day3/class-project/notes.md#step-7-test-biohazard)
---

### Step 1: create the front-end :dumpling: 
        
#### commands :fish_cake:
```
npm create vite
```
- add a name for project call it client
- pick react and javascript

### Step 2: create the environment :spaghetti:

#### commands :fish_cake:
```
python3 - m venv .venv
source .venv/bin/activate
pip install django
```
#### This command will help check the requirements
```
pip freeze
```
#### This will create the requirements file
```
pip freeze > requirements.txt
```

### Step 3: create the project :rice_ball:
        
#### command :fish_cake:
```
python3 -m startproject {project_Name}
```
- cd to project folder
- Add static folder in the project folder

### Step 4: modify the front-end's vite.config.js :house:
    
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

### Step 5: modify settings.py :sunrise_over_mountains:
    
#### Add this under lines 118
    
```python
    STATICFILES_DIRS = [BASE_DIR/'static']
```

### Step 6: make sure to finish build on front-end :roller_coaster:
        
- go to the directory
#### commands :fish_cake:
```
npm install
npm run build
```

### Step 7: Test :biohazard:
    
- check the static folder if its populated
- run the server
    - go to server directory
#### command :fish_cake:
```
python3 manage.py runserver
```