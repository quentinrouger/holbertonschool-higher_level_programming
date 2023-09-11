const toggleHeaderElement = document.getElementById('toggle_header');

// Add a click event listener to the "toggle_header" element
toggleHeaderElement.addEventListener('click', function() {
    // Select the header element using document.querySelector
    const headerElement = document.querySelector('header');

    // Check if the header has the "red" class
    if (headerElement.classList.contains('red')) {
        // If it has the "red" class, remove it and add the "green" class
        headerElement.classList.remove('red');
        headerElement.classList.add('green');
    } else {
        // If it has the "green" class or no class, remove it and add the "red" class
        headerElement.classList.remove('green');
        headerElement.classList.add('red');
    }
});
