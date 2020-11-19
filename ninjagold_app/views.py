from django.shortcuts import render, redirect, HttpResponse
import random, datetime

# Create your views here.

Gold_Spots = {
    "farm": (10,20),
    "cave": (5,10),
    "house": (2,5),
    "casino": (0,50)
}
def index(request):
    if not 'gold' in request.session or 'activities' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []    
    print(request.session['activities'])
    return render(request, 'index.html')

def reset(request):
    request.session.clear()
    return redirect('/')

def process(request):
    if request.method == "GET":
        return redirect('/')
    building_name = request.POST["building"]
    building = Gold_Spots[building_name]
    building_name_upper = building_name[0].upper() + building_name[1:] 

    curr_gold = random.randint(building[0], building[1])

    now_formatted = datetime.datetime.now().strftime("%m/%d/%Y %I:%M%p")

    result = 'earn'

    message = f"Earned {curr_gold} from the {building_name_upper}! ({now_formatted})"

    if building_name == 'casino':
        if random.randint(0,1) > 0: 
            message = f"Entered a {building_name_upper} and lost {curr_gold} golds... Ouch... ({now_formatted})"
            curr_gold = curr_gold * -1
            result = 'lose'

    request.session['gold'] += curr_gold
    request.session['activities'].append({"message": message, "result": result})
    return redirect('/')
