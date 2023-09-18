$(document).ready(function () {
  $('#add_item').click(function () {
    // Create a new list item element
    const newItem = $('<li>Item</li>');

    // Add the new item to the list
    $('ul.my_list').append(newItem);
  });

  // Event handler for removing the last item
  $('#remove_item').click(function () {
    // Select and remove the last list item
    $('ul.my_list li:last-child').remove();
  });

  // Event handler for clearing the entire list
  $('#clear_list').click(function () {
    // Remove all list items
    $('ul.my_list').empty();
  });
});
