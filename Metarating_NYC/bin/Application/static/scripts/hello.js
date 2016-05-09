var coords;

$(document).ready(function(){      

  if (navigator.userAgent.match(/(iPhone|iPod|iPad|Android|BlackBerry)/)){
      $('#homeimage').addClass('homeimageiPhone');
  } else {
      $('#homeimage').addClass('homeimageDesktop');
  }

  if (navigator.geolocation){
    navigator.geolocation.getCurrentPosition(function(position){
       coords = position.coords;
       var latitude = coords.latitude;
       var longitude = coords.longitude;
       $('form')
         .append('<input class="hidden" value="'+ longitude + '" name="longitude">')
         .append('<input class="hidden" value="'+ latitude + '" name="latitude">')
       console.log(coords);
    },
    function (error) { 
      if (error){
         console.log("Permission Denied");
         $('form')
          .append('<input class="hidden" value="'+ "None" + '" name="longitude">')
          .append('<input class="hidden" value="'+ "None" + '" name="latitude">')
      };
  }, {timeout:10000});
} else {
  error('not supported');
  console.log("Browser doesn't support geolocation.");
  $('form')
      .append('<input class="hidden" value="'+ "None" + '" name="longitude">')
      .append('<input class="hidden" value="'+ "None" + '" name="latitude">')
}

  $(".pull-me").text($(this).is(':visible') ? "tap to specify location" : "tap to specify location");

  $('.pull-me').click(function(){
    $('.panel').slideToggle('fast', function(){;
      $(".pull-me").text($(this).is(':visible') ? "tap to use current location" : "tap to specify location");
    });
  });

});