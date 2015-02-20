$(function() {

  function redirectOnHeartbeat(ipAddr) {
    $.get("http://" + ipAddr + ":18570/_heartbeat")
    .done(function(data){
      if (data.response == 'ok') {
        redirUrl = "http://" + ipAddr + "/admin";
        console.log("Received heartbeat. Redirecting to " + redirUrl);
        window.location.replace(redirUrl);
      }
    })
    .fail(function() {
      console.log("Failed to receive heartbeat");
    })
  }

  function poll() {
    var poll_frequency = 2 * 1000; // seconds
    $.get("http://api.ailurus.ca/ping")
    .done(function(data) {
      if (data.ip_map_to != null) {
        console.log("Received map to: " + data.ip_map_to);
        redirectOnHeartbeat(data.ip_map_to);
      } else {
        console.log("Received null map");
      }
    })
    .fail(function() {
      console.log("Failed to connect to ailurus service");
    })
    .always(function() {
      setTimeout(poll, poll_frequency);
    })
  }

  poll();
});
