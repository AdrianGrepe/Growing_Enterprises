
$(document).ready(function(){
    $('.ui-button.inactive').click(function(){
      e.preventDefault();
    });
    
    $('#close').click(function(){
      $('.ui-panel').removeClass('bounceInDown').addClass('bounceOutUp');
    });
  });