Required Technologies:
    - Readwrite to csv files
    - Django
    - Bootstrap(highly recomended)
        - Navbar component
        - Grid
        - Another component
    
    - Required Features
        - Homepage
            - Links to other pages
        - Each product gets its own page - "Individual Product Page"
            - user can add one or more of the product Qty to the shopping cart
        - A page for each category (pet food, birds, mamals, etc) for product - "Category Page"
        - Shopping cart/ Checkout Page
            - user can see whats in the shopping cart
    ================================================================
    products.csv:
        - id, product_name, product_category, image_url,    cost
    ex     0, mittens,      cat,            {some web url}, 20
           1, litterbox,    accessories,    {some web url}, 10

    shopping_cart.csv:
        - product_id , quantity
     ex.    0        ,    1     #cat
            1        ,    2     #accessories


================= Implementation ===========================
1. setup
    - create environment
        - activate it
    - create django project
        - edit settings.py and urls.py
        - create app
            -add urls.py
            -templates folder
                -create index.html
        
    - create static

2. create csv files
    
3. implement read and write on csv files
    - prototype
    - print something
4. create homepage
    - Route
    - Templates
5. Display csv homepage
    - prototype
6. Use bootstrap on homepage
    - grid
    - bar


    


