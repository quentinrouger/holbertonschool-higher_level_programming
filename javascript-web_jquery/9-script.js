// Make an AJAX GET request to the API URL
$.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function(data) {
  var hello = data.hello;

  $("#hello").append(hello);
});
