﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():
    catalog= model.newCatalog()

    return catalog
# Funciones para la carga de datos

def loadData(catalog):
    loadArtist(catalog)
    loadArtWork(catalog)
    loadMedium(catalog)
def loadArtist(catalog):
    booksfile = cf.data_dir + 'Artists-utf8-large.csv'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for Artist in input_file:
        model.addArtist(catalog, Artist)

def loadArtWork(catalog):
    booksfile = cf.data_dir + 'Artworks-utf8-large.csv'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for ArtWorks in input_file:
        model.addArtwork(catalog, ArtWorks)



def loadArtWork(catalog):
    booksfile = cf.data_dir + 'Artworks-utf8-large.csv'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for ArtWorks in input_file:
        model.addArtwork(catalog, ArtWorks)


def loadMedium(catalog):
    booksfile = cf.data_dir + 'Artworks-utf8-large.csv'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for Medium in input_file:
        model.addMedium(catalog, Medium)
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def ArtistSize(catalog):

    return model.AuthorsSize(catalog)

def ArtworkSize(catalog):
    return model.ArtworkSize(catalog) 

def artistas(catalog):
    inicio = int(input("Inserte fecha inicial : "))
    final = int(input("Inserte fecha final: "))

    return model.ordenarEdadAutores(catalog, inicio, final)



def c3(catalog):
    return model.asignarArtista(catalog)
