from django.shortcuts import render
# import requests to get websites
import requests

# Create your views here.
def Movies_list(request):
# to add the base website that we will request information from.
	query = request.GET.get("q")
	url = "http://www.omdbapi.com/?apikey=37c1229d&s=king"
	if query:
		url = "http://www.omdbapi.com/?apikey=37c1229d&s=" + query	
	response = requests.get(url)
	print(response.json())

	context = {
		"movies": response.json()
	}

	return render(request, 'movies_list.html', context)

def movie_details(request, movie_id):
	url = "http://www.omdbapi.com/?apikey=37c1229d&i=" + movie_id
	response = requests.get(url)

	context = {
		"movie": response.json()
	}
	return render(request, 'movie_details.html', context)

# def movie_search(requests, movie_id):
