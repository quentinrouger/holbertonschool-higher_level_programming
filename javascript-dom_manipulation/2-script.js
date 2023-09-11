const redHeaderElement = document.getElementById('red_header');

redHeaderElement.addEventListener('click', function() {
    const headerElement = document.querySelector('header');

    // Add the "red" class to the header element
    headerElement.classList.add('red');
});
