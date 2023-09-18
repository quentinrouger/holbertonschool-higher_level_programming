// Make an AJAX GET request to the API URL
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  // Extract the movie titles from the response JSON
  const movieTitles = data.results;
  // Loop through each movie title
  for (let i = 0; i < movieTitles.length; i++) {
    // Display the movie title in the HTML <ul id="list_movies">
    $('#list_movies').append('<li>' + movieTitles[i].title + '</li>');
  }
});
