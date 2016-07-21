# Lista skladnikow i ich wlasciwosci

jed = ['A','A','A']
dwa = ['A','A','B']
trz = ['A','B','B']
czt = ['B','B','B']
pie = ['B','B','C']
sze = ['B','C','C']
sie = ['C','C','C']
osi = ['C','C','A']
dzi = ['C','A','A']

Ingr = [jed, dwa, trz, czt, pie, sze, sie, osi, dzi]

# Przelaczniki

ingrcheck = True
ingrextract = True

# Sprawdzarka skladnikow

ingredient = ''

if ingrcheck == True:
    print 'Ingredients: 1, 2, 3, 4, 5, 6, 7, 8, 9'
    print 'Choose Ingredient'

while ingrcheck == True:
    ingredient = raw_input()
    if ingredient == '1' or ingredient == '2' or ingredient == '3' or ingredient == '4' or ingredient == '5' or ingredient == '6' or ingredient == '7' or ingredient == '8' or ingredient == '9':
        ingrcheck = False
        print 'You chose', str(ingredient)

# Sprawdzarka wlasciwosci

if ingredient == '1':
    prop = jed
    print 'Ingredient property:', prop[0], prop[1], prop[2]
if ingredient == '2':
    prop = dwa
    print 'Ingredient property:', prop[0], prop[1], prop[2]
if ingredient == '3':
    prop = trz
    print 'Ingredient property:', prop[0], prop[1], prop[2]
if ingredient == '4':
    prop = czt
    print 'Ingredient property:', prop[0], prop[1], prop[2]
if ingredient == '5':
    prop = pie
    print 'Ingredient property:', prop[0], prop[1], prop[2]
if ingredient == '6':
    prop = sze
    print 'Ingredient property:', prop[0], prop[1], prop[2]
if ingredient == '7':
    prop = sie
    print 'Ingredient property:', prop[0], prop[1], prop[2]
if ingredient == '8':
    prop = osi
    print 'Ingredient property:', prop[0], prop[1], prop[2]
if ingredient == '9':
    prop = dzi
    print 'Ingredient property:', prop[0], prop[1], prop[2]

# Wydobywanie ze skladnikow

if ingrextract == True:
    print ''
    print 'Methods: 1, 2, 3'
    print 'Choose extraction method'

while ingrextract == True:
    method = raw_input()
    if method == '1' or method == '2' or method == '3':
        print 'You chose method:', str(method)
# Methods when X X X
    if method == '1' and prop[0] == prop[1] == prop[2]:
        print 'Successfuly extracted', str(prop[0])
        ingrextract = False
    if method == '2' and prop[0] == prop[1] == prop[2]:
        print 'Extraction Failed'
        print ''
        ingrextract = True
    if method == '3' and prop[0] == prop[1] == prop[2]:
        print 'Extraction Failed'
        print ''
        ingrextract = True
# Methods when Y X X or X X Y
    if method == '1' and prop[0] != prop[1] == prop[2] or method == '1' and prop[0] == prop[1] != prop[2]:
        print 'Extraction Failed'
        print ''
        ingrextract = True
    if method == '2' and prop[0] != prop[1] == prop[2]:
        print 'Successfuly extracted', str(prop[0])
        ingrextract = False
    if method == '2' and prop[0] == prop[1] != prop[2]:
        print 'Successfuly extracted', str(prop[2])
        ingrextract = False
    if method == '3' and prop[0] == prop[1] != prop[2]:
        print 'Successfuly extracted', str(prop[1])
        ingrextract = False
    if method == '3' and prop[0] != prop[1] == prop[2]:
        print 'Successfuly extracted', str(prop[1])
        ingrextract = False

