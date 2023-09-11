const updateHeaderElement = document.getElementById('update_header');

// Add a click event listener to the "update_header" element
updateHeaderElement.addEventListener('click', function() {
    // Select the <header> element
    const headerElement = document.querySelector('header');

    // Update the text content of the header element
    headerElement.textContent = 'New Header!!!';
});
