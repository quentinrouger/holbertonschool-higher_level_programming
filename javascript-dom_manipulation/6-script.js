const characterElement = document.getElementById('character');

        // URL for fetching character data
        const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

        // Use the Fetch API to fetch character data
        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                // Extract and display the character name
                const characterName = data.name;
                characterElement.textContent = characterName;
            })
            .catch(error => {
                console.error(error);
            })
