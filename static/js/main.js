function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          if (cookie.substring(0, name.length + 1) == (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}


function save_cliente() {
  var lista_telefonos = [];
  var lista_direcciones = [];
  $.each($("#clienes_telefono input"), function(index, val) {
    lista_telefonos.push($(this).val());
  });
  $.each($("#clienes_direccion input"), function(index, val) {
    lista_direcciones.push($(this).val());
  });
  $.ajax({
    url: 'crear_cliente/',
    type: 'POST',
    dataType: 'json',
    data: {cedula: $("#cedula").val(),
            nombre: $("#nombre").val(),
            apellido: $("#apellido").val(),
            sexo: $("#sexo").val(),
            fecha_de_nacimiento: $("#fecha_de_nacimiento").val(),
            telefonos: lista_telefonos,
            direcciones: lista_direcciones,
    },
    beforeSend: function(xhr) {xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));},
  })
  .done(function(data) {
    llenar_select_clientes(data);
    OmegaNotify.success('Guardado Exitosamente');
    vaciar_telefonos_direcciones();
  })
  .fail(function() {
  })
  .always(function() {
  });
  
}

function buscar_equipos() {
  $.ajax({
    url: 'get_equipos/',
    type: 'POST',
    dataType: 'json',
    data: {cliente: $("#cliente").val(), tipo: $("#tipo").val()},
    beforeSend: function(xhr) {xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));},
  })
  .done(function(data) {
    $('#equipo').empty();
    $.each(data, function(index, val) {
      $('#equipo').append($('<option>', {
        value: val.id,
        text: val.name
      }));
    });
    $('#equipo').select2('val','');
  })
  .fail(function() {
  })
  .always(function() {
  });
  
}
