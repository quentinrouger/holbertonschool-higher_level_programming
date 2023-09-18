$(document).ready(function () {
  $('#btn_translate').click(function () {
    // Get the language code entered by the user
    const languageCode = $('#language_code').val();

    // Make an AJAX GET request to fetch the translation
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`, function (data) {
      // Extract the translation from the response
      const translation = data.hello;

      // Display the translation in the HTML <div id="hello">
      $('#hello').text(translation);
    });
  });
});
