$(document).ready(function(){

    var adult_counter = 0;
    var total = 0;
    var passNum = 0
    var id = 0
    passNum = parseInt($("#passNum").text());

    $("#incrementAdult").click(function() {
        if ($("#adult_counter").val() >= 0) {
            adult_counter++;
            $("#adultnum").text(adult_counter);
            $("#adult_counter").val(adult_counter);
        }
      });
    
      $("#decrementAdult").click(function() {
        if ($("#adult_counter").val() > 0) {
            console.log("adult --");
            adult_counter--;
            $("#adultnum").text(adult_counter);
            $("#adult_counter").val(adult_counter);
        }
      });

      $('#economy').on('change', function() {
        if($("#economy").is(":checked")){
          total = $("#ecoPrice").text();
          total = parseFloat(total)
          $("#totalPrice").text("$"+(total*passNum));
          $("#total_price").val("$"+(total*passNum));
          id = $("#get_flight_id").val()
        }
     });
      
     $('#business').on('change', function() {
        if($("#business").is(":checked")){
          total = $("#busPrice").text();
          total = parseFloat(total)
          $("#totalPrice").html("$"+(total*passNum));
          $("#total_price").val("$"+(total*passNum));
          id = $("#get_flight_id").val()
        }
     });

     
      
});