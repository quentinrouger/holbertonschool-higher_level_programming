const movieListElement = document.getElementById('list_movies');

        // URL for fetching movie data
        const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

        // Use the Fetch API to fetch movie data
        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                // Extract and list the movie titles
                const movies = data.results;
                movies.forEach(movie => {
                    const movieTitle = movie.title;
                    const listItem = document.createElement('li');
                    listItem.textContent = movieTitle;
                    movieListElement.appendChild(listItem);
                });
            })
            .catch(error => {
                console.error(error);
            });
