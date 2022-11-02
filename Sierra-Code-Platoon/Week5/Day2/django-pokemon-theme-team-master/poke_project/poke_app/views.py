from unittest import result
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse 
import requests as Httprequest
import random


def index(request):
    
    req = Httprequest.get( "https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0" )
    
    pokemons = req.json()
    rand_index = random.randint(0, len(pokemons["results"]))
    print(rand_index)
    pokemon = pokemons["results"][rand_index]
    poke_url = pokemon['url']
    
    poke_img = get_img(poke_url)
    req2 = Httprequest.get(poke_url)
    poke_info = req2.json()
    # poke_img = poke_info['sprites']['other']['official-artwork']['front_default']
    poke_type_url = poke_info['types'][0]['type']['url']
    similar_pokemon = similar_poke(poke_type_url)
    return render(request, 'index.html', {'poke_name':pokemon['name'], 'poke_img':poke_img, 'similar_pokemon':similar_pokemon})


def similar_poke(url):
    req = Httprequest.get(url)
    poke_info = req.json()
    similar_poke = poke_info['pokemon'][:5]
    poke_arr = []
    poke_url_arr = []
    for poke in similar_poke:
        poke_arr.append(poke['pokemon']['name'])
        
        img_url = poke['pokemon']['url']
        poke_url_arr.append(get_img(img_url))
        
        
    # print(poke_arr)
    # print(poke_url_arr)

    return poke_url_arr
    
def get_img(url):
    req2 = Httprequest.get(url)
    poke_info = req2.json()
    poke_img = poke_info['sprites']['other']['official-artwork']['front_default']
    return poke_img
    
def detail(request, poke_id):
    
    url = f"https://pokeapi.co/api/v2/pokemon/{poke_id}"
    poke_img = get_img(url)
    
    return render(request, 'detail.html', {'poke_img':poke_img})
    
# Create your views here.
