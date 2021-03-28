from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory='templates')

async def homepage(request):
  return templates.TemplateResponse('index.html', {'request': request})

async def findrecipe(request):
    preferences = await request.form()
    dietp = preferences['dietp']
    time_required = preferences['time']
    calories = preferences['calories']
    course = preferences['course']
    ingredients = preferences['ingredients']
    
    if course == "main course":
        course = "main-dish"
        
    if time_required == 1:
        min_time = 0
        max_time = 30
    elif time_required == 2:
        min_time = 30
        max_time = 60
    elif time_required == 3:
        min_time = 60
        max_time = 90
    elif time_required == 4:
        min_time = 90
        max_time = 120
    else:
        min_time = 120
        max_time = 10000000
        
    if calories == 1:
        max_calories = 250
        min_calories = 0
    else:
        min_calories = 300
        max_calories = 1000000
    
    min_time = str(min_time)
    max_time = str(max_time)
    min_calories = str(min_calories)
    max_calories = str(max_calories)
    
    if dietp == 'non-vegetarian': 
        data = request.state.db.recipes.find({
            '$and:' [
                {'tags': {'$all': ingredients}},
                {'$not': {'tags': 'vegetarian'}},
                {'tags': course},
                {'$and': [{'minutes': {'$lt': max_time}}, {'minutes': {'$gte': min_time}}]},
                {'$and': [{'nutrition.0': {'$lt': max_calories}}, {'nutrition.0': {'$gt': min_calories}}]}
            ]
        }, limit=10)
    else:
        data = request.state.db.recipes.find({
            '$and:' [
                {'tags': {'$all': ingredients}},
                {'tags': 'dietp'},
                {'tags': course},
                {'$and': [{'minutes': {'$lt': max_time}},
                            {'minutes': {'$gte': min_time}}]},
                {'$and': [{'nutrition.0': {'$lt': max_calories}},
                            {'nutrition.0': {'$gt': min_calories}}]}
            ]
        }, limit=10)


    response = []

    return templates.TemplateResponse('recipe.html', {'request': request, 'response': response})
