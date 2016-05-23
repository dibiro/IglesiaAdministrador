$('.datetimepicker').datetimepicker({format: "YYYY-MM-DD",locale: 'es',});
$("select").select2();

function add_evento() {
    $(".culto").click(function(event) {
        get_culto($(this).data('id'));
    });
    $(".eventos").click(function(event) {
        get_eventos($("#year").val(), $("#mes").val(), $(this).data('dia'));
    });
}

function Calendario(year, mouth) {
  $.ajax({
    url: 'calendario/',
    type: 'GET',
    dataType: 'json',
    data: {year: year, mouth: mouth},
  })
  .done(function(data) {
    $('#calendario').empty();
    var texto = '';
    $.each(data, function(index, val) {
      if (val.weekday=='0') {
        texto += '<tr><th class="'+val.class+' data-dia="'+val.dia+'">'+val.dia+'</th>';
      }else if (val.weekday=='6') {
        texto += '<th class="'+val.class+' data-dia="'+val.dia+'">'+val.dia+'</th>tr';
      }else {
        texto += '<th class="'+val.class+' data-dia="'+val.dia+'">'+val.dia+'</th>';
      };
        $('#calendario').html(texto);               
    });
  })
  .fail(function() {
  })
  .always(function() {
    add_evento();
  });
}

function get_eventos(year, mouth, day) {
  $.ajax({
    url: 'get_eventos/',
    type: 'GET',
    dataType: 'json',
    data: {year: year, mouth: mouth, day: day},
  })
  .done(function(data) {
    $('#visulizar_eventos').empty();
    $.each(data, function(index, val) {
      if (val.tipo=='1') {
        $('#visulizar_eventos').append('<div class="col-sm-6 col-xs-12 culto panel panel-info" data-toggle="modal" data-target="#modificar_culto" data-id="'+val.id+'"><div class="panel-heading">'+val.nombre+'</div><div class="panel-body"><p>'+val.direccion+'</p></div></div>')
      }else {
        $('#visulizar_eventos').append('<div class="col-sm-6 col-xs-12 evento panel panel-success" data-toggle="modal" data-target="#modificar_evento" data-id="'+val.id+'"><div class="panel-heading">'+val.nombre+'</div><div class="panel-body"><p>'+val.encargado+'</p><p>'+val.descripcion+'</p><p>'+val.hora+'</p></div></div>')
      };
    });
  })
  .fail(function() {
  })
  .always(function() {
    add_evento();
    $('#dia_vizualisado').html(day+'/'+mouth+'/'+year);               
    
  });
}

$("#year").change(function(event) {
    Calendario($("#year").val(), $("#mes").val())
});
$("#mes").change(function(event) {
    Calendario($("#year").val(), $("#mes").val())
});

Calendario($("#year").val(), $("#mes").val());

function crear_culto() {
    $.ajax({
    url: 'crear_culto/',
    type: 'POST',
    dataType: 'json',
    data: {
        'fecha': $("#Fecha").val(),
        'Direccion': $("#Direccion").val(),
        'lectura': $("#Lectura").val(),
        'recolecion': $("#Recolecion").val(),
        'oracion': $("#Oracion").val(),
        'coros': $("#Coros").val(),
        'predicacion': $("#Predicacion").val(),
        'tipo': $("#tipos_de_cultos").val(),
        'Escuela_De_ninos': $("#Escuela_De_ninos").val(),
        'Escuela_dominical': $("#Escuela_dominical").val(),
    },
    beforeSend: function(xhr) {xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));},
  })
  .done(function(data) {
    Calendario(data.year, data.month)
  })
  .fail(function() {
  })
  .always(function() {
  });
}

function get_culto(id) {
    $.ajax({
    url: 'get_culto/',
    type: 'GET',
    dataType: 'json',
    data: {
        'id': id
    },
  })
  .done(function(data) {
    $("#id_culto").val(data.id);
    $("#Modificar_Fecha").val(data.Fecha);
    $("#Modificar_Direccion").val(data.Direccion);
    $("#Modificar_Lectura").val(data.Lectura);
    $("#Modificar_Recolecion").val(data.Recolecion);
    $("#Modificar_Oracion").val(data.Oracion);
    $("#Modificar_Coros").val(data.Coros);
    $("#Modificar_Predicacion").val(data.Predicacion);
    $("#Modificar_tipos_de_cultos").val(data.tipos_de_cultos);
    $("#Modificar_Escuela_De_ninos").val(data.escuela_de_nino);
    $("#Modificar_Escuela_dominical").val(data.escuela_dominical);
  })
  .fail(function() {
  })
  .always(function() {
    $("select").select2();
  });
}

$("#crear_culto_btn").click(function(event) {
    crear_culto();
    $('#crear_culto').modal('hide');
});
