$(document).ready(function () {
  function TranslateHello () {
    // Get the language code entered by the user
    const languageCode = $('#language_code').val();

    // Make an AJAX GET request to fetch the translation
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`, function (data) {
      // Extract the translation from the response
      const translation = data.hello;

      // Display the translation in the HTML <div id="hello">
      $('#hello').text(translation);
    });
  }
  // Attach a click event handler to the "Translate" button
  $('#btn_translate').click(TranslateHello);

  // Attach a keypress event handler to the input field for Enter key
  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      TranslateHello();
    }
  });
});
