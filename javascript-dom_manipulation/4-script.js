const addItemElement = document.getElementById('add_item');

// Add a click event listener to the "add_item" element
addItemElement.addEventListener('click', function() {
    // Create a new <li> element
    const newItem = document.createElement('li');
    
    // Set the text content of the new <li> element
    newItem.textContent = 'Item';
    
    // Select the <ul> element with class "my_list"
    const myListElement = document.querySelector('.my_list');
    
    // Append the new <li> element to the <ul> element
    myListElement.appendChild(newItem);
});
