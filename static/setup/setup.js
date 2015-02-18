$(function() {

  (function poll() {
    var poll_frequency = 2 * 1000; // seconds
    $.get("http://api.ailurus.ca/ping")
    .done(function(data) {
      console.log(data);
      if (data.ip_map_to != null) {
        console.log(data.ip_map_to);
        window.location.replace("http://" + data.ip_map_to);
      }
    })
    .fail(function() {
    })
    .always(function() {
      setTimeout(poll, poll_frequency);
    })
  })();

});
