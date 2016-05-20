var id_chat = 0

function Mensaje() {
  $.ajax({
    url: '/Culto/mensaje/',
    type: 'GET',
    dataType: 'json',
    data: {id: id_chat+1, culto: $("#id_culto").val()},
  })
  .done(function(data) {
    $.each(data, function(index, val) {
      if (val.user==1) {
        $(".chat-container").append('<div class="chat my-message animated fadeInUp">'+val.comentarios+'</div>')
      }else{
        $(".chat-container").append('<div class="chat other-message animated fadeInUp">'+val.comentarios+'</div>')
      };
      id_chat=val.id;
    });
  })
  .fail(function() {
  })
  .always(function() {
  });
}

setInterval(Mensaje, 1000)

function NuevoMensaje() {
  $.ajax({
    url: '/Culto/nuevo_mensaje/',
    type: 'POST',
    dataType: 'json',
    data: {comentario: $(".chat-input").val(), culto: $("#id_culto").val()},
    beforeSend: function(xhr) {xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));},
  })
  .done(function(data) {

  })
  .fail(function() {
  })
  .always(function() {
    $(".chat-input").val('')
  });
}

$(".chat-send-icon").on('click', function(event) {
  NuevoMensaje();
});